"""Genera el informe automático del OPCB en Markdown.

Lee las tablas `D_Precio*` de SQL Server y escribe
`docs/proyecto/02-documentacion/informe-opcb.md`.

Uso:
    py -u -m cli.generar_informe
    py -u -m cli.generar_informe --salida informe.md

Todas las consultas son parametrizadas: no hay literales de valores en el SQL.
"""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

from config.settings import BASE_DIR
from etl.conn.db import get_connection

EAN_CASO = "7790742358608"
SALIDA_DEFAULT = BASE_DIR / "docs" / "proyecto" / "02-documentacion" / "informe-opcb.md"


def _escalar(cur, sql: str, params: tuple = ()):
    cur.execute(sql, params)
    fila = cur.fetchone()
    return fila[0] if fila else None


def recolectar() -> dict:
    with get_connection() as conn:
        cur = conn.cursor()

        cadenas = _escalar(cur, "SELECT COUNT(DISTINCT CadenaId) FROM dbo.D_PrecioCadena")
        precios = _escalar(cur, "SELECT COUNT(*) FROM dbo.D_PrecioOferta")
        productos = _escalar(cur, "SELECT COUNT(*) FROM dbo.D_PrecioProducto")
        eans = _escalar(
            cur,
            "SELECT COUNT(DISTINCT Ean) FROM dbo.D_PrecioProducto "
            "WHERE Ean IS NOT NULL AND Ean <> ?",
            ("",),
        )
        comparables = _escalar(
            cur,
            "SELECT COUNT(*) FROM ("
            "  SELECT p.Ean"
            "  FROM dbo.D_PrecioProducto p"
            "  JOIN dbo.D_PrecioOferta o ON o.ProductoId = p.ProductoId"
            "  WHERE p.Ean IS NOT NULL AND p.Ean <> ?"
            "  GROUP BY p.Ean"
            "  HAVING COUNT(DISTINCT p.CadenaId) >= 3"
            ") t",
            ("",),
        )

        cur.execute(
            "SELECT MIN(o.Precio), MAX(o.Precio),"
            "       COUNT(DISTINCT p.CadenaId), COUNT(DISTINCT p.Nombre)"
            " FROM dbo.D_PrecioProducto p"
            " JOIN dbo.D_PrecioOferta o ON o.ProductoId = p.ProductoId"
            " WHERE p.Ean = ? AND o.Precio > ?",
            (EAN_CASO, 0),
        )
        fila = cur.fetchone()
        minimo, maximo, gondolas, nombres = (fila or (None, None, None, None))

    brecha = (maximo - minimo) if (minimo and maximo) else None
    brecha_pct = (brecha / minimo * 100) if (brecha and minimo) else None

    return {
        "cadenas": cadenas,
        "precios": precios,
        "productos": productos,
        "eans": eans,
        "comparables": comparables,
        "minimo": minimo,
        "maximo": maximo,
        "brecha": brecha,
        "brecha_pct": brecha_pct,
        "gondolas": gondolas,
        "nombres": nombres,
    }


def _fmt(n, decimales: int = 0) -> str:
    if n is None:
        return "—"
    return f"{n:,.{decimales}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def render(d: dict) -> str:
    hoy = date.today().strftime("%d/%m/%Y")
    return f"""# Informe automático — Observatorio de Precios de la Canasta Básica (OPCB)

**Generado:** {hoy}
**Comando:** `py -u -m cli.generar_informe`

---

## 1. Metodología

1. **Ingesta:** catálogos públicos de las cadenas, con fecha de relevamiento, cadena, sucursal y origen.
2. **Normalización:** nombres, unidades y EAN (8 o 13 dígitos).
3. **Matching:** EAN exacto primero; similitud de nombre y unidad después, con revisión manual.
4. **Canasta:** 30 productos en almacén, frescos, limpieza y bebidas (criterio en `product-backlog.md`, HU-04).
5. **Cálculo:** costo por cadena y variación \((P_t - P_{{t-1}}) / P_{{t-1}}\).
6. **Calidad:** se descartan precios ≤ 0, EAN inválidos y duplicados; cada descarte se registra.

---

## 2. Resultados

| Métrica | Valor |
|---|---|
| Cadenas con datos cargados | {_fmt(d['cadenas'])} |
| Precios observados | {_fmt(d['precios'])} |
| Productos en catálogo | {_fmt(d['productos'])} |
| EAN distintos | {_fmt(d['eans'])} |
| Productos comparables en ≥ 3 cadenas | {_fmt(d['comparables'])} |
| Brecha máxima en el caso de prueba | {_fmt(d['brecha_pct'], 1)} % ({_fmt(d['brecha'])} $) |

---

## 3. Caso de prueba

La botella de 1 L de La Serenísima Protein (EAN `{EAN_CASO}`) aparece en **{_fmt(d['gondolas'])} góndolas**
con **{_fmt(d['nombres'])} nombres distintos** y precios de **${_fmt(d['minimo'])} a ${_fmt(d['maximo'])}**:
**${_fmt(d['brecha'])} de diferencia ({_fmt(d['brecha_pct'], 1)} %)** por el mismo producto.

---

## 4. Limitaciones

- La canasta de 30 productos representa un hogar urbano de ingresos medios; no cubre dietas
  regionales ni productos sin TACC.
- Solo se comparan cadenas con catálogo público.
- No se predice ni se atribuyen causas: se describen precios observados.

---

## 5. Fuentes

- Catálogos públicos de SEPA, La Banderita y Coope.
- Base `precios-supermercados-etl` (tablas `D_Precio*`).
- Repositorio de código: <https://github.com/Nicaleluc/tp2-precios-supermercados-etl>
- Repositorio de la entrega: <https://github.com/Nicaleluc/tp-final-opcb>
- Tablero: <https://trello.com/b/8kXtbi62/opcb-observatorio-de-precios-de-la-canasta-basica>
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Genera el informe automático del OPCB.")
    parser.add_argument("--salida", type=Path, default=SALIDA_DEFAULT)
    args = parser.parse_args(argv)

    try:
        datos = recolectar()
    except Exception as exc:  # conexión o consulta
        print(f"No se pudo leer la base: {exc}", file=sys.stderr)
        return 1

    args.salida.parent.mkdir(parents=True, exist_ok=True)
    args.salida.write_text(render(datos), encoding="utf-8")
    print(f"Informe generado: {args.salida}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
