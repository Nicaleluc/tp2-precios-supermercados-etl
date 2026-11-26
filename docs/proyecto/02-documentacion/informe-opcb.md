# Informe automático — Observatorio de Precios de la Canasta Básica (OPCB)

**Generado:** 26/11/2026
**Versión del dataset:** operativo TP II, relevamiento 13–20/10/2026
**Comando:** `py -u -m cli.generar_informe`

---

## 1. Metodología

1. **Ingesta:** se descargan los catálogos públicos de las cadenas y se persiste cada precio con
   fecha de relevamiento, cadena, sucursal y origen.
2. **Normalización:** se unifican mayúsculas, acentos, espacios y unidades (g/kg, ml/l); el EAN se
   conserva como texto y se validan 8 o 13 dígitos.
3. **Matching:** se empareja primero por EAN exacto y luego por similitud de nombre y unidad, con
   umbral de confianza y revisión manual de la canasta.
4. **Canasta:** 30 productos agrupados en almacén, frescos, limpieza y bebidas. El criterio de
   inclusión está documentado en `01-planificacion/product-backlog.md` (HU-04).
5. **Cálculo:** costo por cadena y variación semanal con la fórmula
   \((P_t - P_{t-1}) / P_{t-1}\) sobre el mismo conjunto de productos.
6. **Calidad:** se descartan precios ≤ 0, EAN inválidos y duplicados; cada descarte se registra.

---

## 2. Resultados

| Métrica | Valor |
|---|---|
| Cadenas con datos cargados | 12 (16 configuradas) |
| Precios observados | 33.900 |
| Productos en catálogo | 21.235 |
| EAN distintos | 14.356 |
| Productos comparables en ≥ 3 cadenas | 1.491 |
| Brecha máxima en el caso de prueba | +22,7 % ($606) |

Las cifras se recalculan desde las tablas `D_Precio*`; no hay valores escritos a mano en el código.

---

## 3. Caso de prueba

La botella de 1 L de La Serenísima Protein (EAN `7790742358608`) aparece en **nueve góndolas** con
**siete nombres distintos** y precios de **$2.669 a $3.275**: **$606 de diferencia (22,7 %)** por el
mismo producto.

Este caso justifica el proyecto: sin normalización y matching, la comparación sería una suposición.

---

## 4. Limitaciones

- El dataset operativo proviene del TP II (13–20/10/2026); el MVP se apoya en esa base.
- La canasta de 30 productos es una decisión explícita: representa un hogar urbano de ingresos
  medios y no cubre dietas regionales ni productos sin TACC.
- La comparación se limita a las cadenas con catálogo público; no incluye comercios minoristas.
- No se predice ni se atribuyen causas: el sistema describe precios observados.

---

## 5. Fuentes

- Catálogos públicos de SEPA, La Banderita y Coope (VTEX y sitios propios).
- Base `precios-supermercados-etl` (tablas `D_Precio*`).
- Repositorio de código: <https://github.com/Nicaleluc/tp2-precios-supermercados-etl>
- Repositorio de la entrega: <https://github.com/Nicaleluc/tp-final-opcb>
- Tablero: <https://trello.com/b/8kXtbi62/opcb-observatorio-de-precios-de-la-canasta-basica>

---

## 6. Reproducibilidad

```bash
py -u -m cli.generar_informe          # genera este informe en Markdown
py -u -m cli.comparar --ean 7790742358608
pytest -q
```
