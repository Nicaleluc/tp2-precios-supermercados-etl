<!--
README.md del repositorio GitHub del proyecto (precios-supermercados-etl).
Al publicar: subirlo a la raíz del repo como README.md y reemplazar las capturas por las reales.
-->

<h1 align="center">OPCB · Observatorio de Precios de la Canasta Básica</h1>

<p align="center">
  <em>Del catálogo disperso de cada supermercado a una serie comparable, trazable y publicable.</em>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white">
  <img alt="SQL Server" src="https://img.shields.io/badge/SQL%20Server-2019%2B-CC2927?logo=microsoftsqlserver&logoColor=white">
  <img alt="pytest" src="https://img.shields.io/badge/tests-pytest-0A9EDC?logo=pytest&logoColor=white">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-green">
  <img alt="Estado" src="https://img.shields.io/badge/estado-MVP-yellow">
  <img alt="Trello" src="https://img.shields.io/badge/tablero-Trello-0079BF?logo=trello&logoColor=white">
</p>

---

## Qué es esto

OPCB es un pipeline de datos que integra los catálogos públicos de cadenas de supermercados de
Bahía Blanca, normaliza productos y unidades, empareja el mismo producto entre cadenas y publica el
costo de una canasta básica con su variación semanal.

Nació como Proyecto Integrador Final de **Prácticas Profesionalizantes I** (INA, Tecnicatura en
Ciencia de Datos e IA) y se apoya en el ETL desarrollado en el TP II.

> **Alcance:** MVP académico. No predice precios ni reemplaza una medición oficial de inflación.
> La metodología y sus límites están documentados en
> [`docs/proyecto/01-planificacion/proyecto.md`](docs/proyecto/01-planificacion/proyecto.md).

---

## El problema en una frase

Comparar el costo de la misma canasta entre supermercados exige abrir tres sitios, buscar treinta
productos en cada uno y adivinar si "Arroz 1 kg" y "Arroz largo fino 1000 g" son el mismo bien.
OPCB convierte ese trabajo manual en una consulta reproducible.

**Caso concreto:** la botella de 1 L de La Serenísima Protein (EAN `7790742358608`) aparece en
nueve góndolas con **siete nombres distintos** y precios de **$2.669 a $3.275**: **22,7 %** de
diferencia por el mismo producto.

---

## Arquitectura

```text
              ┌──────────────┐   ┌───────────────┐   ┌──────────────┐
 Catálogos →  │   conectores │ → │ normalización │ → │   matching   │
 (cadenas)    └──────────────┘   └───────────────┘   └──────┬───────┘
                                                            │
                       ┌────────────────────────────────────┴────────┐
                       │                                             │
                ┌──────▼──────┐                             ┌────────▼────────┐
                │  SQL Server │                             │  canasta + KPIs │
                │  (histórico)│                             └────────┬────────┘
                └─────────────┘                                      │
                       │                                    ┌────────▼────────┐
                       └───────────────────────────────────►│  informe + CLI  │
                                                            └─────────────────┘
```

| Capa | Módulo | Responsabilidad |
|---|---|---|
| Conectores | `etl/conn/` | obtener catálogos por cadena, aislados entre sí (VTEX, Coope, La Banderita) |
| Normalización | `etl/dominios/precios/normalizar*.py` | nombres, unidades y EAN |
| Matching | `etl/dominios/comparador/matching.py` | identificar el mismo producto entre cadenas |
| Persistencia | `etl/dominios/precios/repository.py` | histórico idempotente en SQL Server (`D_Precio*`) |
| Canasta | `etl/dominios/comparador/canasta.py` | costo, variación y brecha |
| Producto | `cli/` | consultas, comparación y reportes |
| Calidad | `tests/` | normalización, matching e integridad |

---

## Stack

- **Python 3.12** — `requests`, `pyodbc`, `SQLAlchemy`, `beautifulsoup4`
- **SQL Server** — persistencia del histórico de precios
- **pytest** — pruebas unitarias e integridad
- **Markdown + HTML** — documentación
- **Trello** — gestión ágil del proyecto
- **GitHub** — control de versiones y trazabilidad

---

## Cómo correrlo

### 1. Requisitos

- Python 3.12+
- SQL Server con una base disponible
- Acceso a los catálogos públicos de las cadenas

### 2. Instalación

```bash
git clone https://github.com/Nicaleluc/tp2-precios-supermercados-etl.git
cd tp2-precios-supermercados-etl
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -e .
```

### 3. Configuración

```bash
copy .env.template .env       # completar credenciales locales
```

Variables principales (nunca subir `.env` al repo):

```text
DB_SERVER=localhost
DB_NAME=precios-supermercados-etl
DB_USER=...
DB_PASSWORD=...
```

### 4. Pipeline

Los `.bat` de la raíz son atajos de los comandos de abajo (doble clic o consola).

```bash
py -u -m cli.importar_precios --catalogo      # ingesta de catálogos (o cargar_todo.bat)
py -u -m cli.cargar_sucursales                # sucursales por cadena
py -u -m cli.cargar_sepa                      # cadena SEPA
py -u -m cli.comparar leche yerba aceite      # comparación sobre la base (o comparar.bat)
py -u -m cli.comparar --ean 7790742358608     # un producto en todas las cadenas
py -u -m cli.chequear_precio <termino>        # control puntual de precio
```

### 5. Tests

```bash
pytest -q
```

Las pruebas unitarias corren sin base de datos. Las de integración se saltean si no hay conexión.

---

## Metodología (resumen)

1. **Canasta:** 30 productos agrupados en almacén, frescos, limpieza y bebidas. El criterio de
   inclusión está en [`docs/proyecto/01-planificacion/product-backlog.md`](docs/proyecto/01-planificacion/product-backlog.md) (HU-04).
2. **Unidad de comparación:** precio por unidad de medida (kg, l, unidad), no precio de góndola.
3. **Matching:** EAN exacto primero; similitud de texto y unidad después, con umbral de confianza
   (≥ 70 %) y revisión manual de la canasta.
4. **Variación:** \((P_t - P_{t-1}) / P_{t-1}\), sobre el mismo conjunto de productos.
5. **Calidad:** se descartan precios ≤ 0, EAN inválidos y duplicados; cada descarte se registra.

---

## Resultados (dataset operativo del TP II, 13–20/10/2026)

| Métrica | Valor | Cómo se obtiene |
|---|---|---|
| Cadenas con datos cargados | 12 (16 configuradas) | `D_PrecioCadena` |
| Precios observados | 33.900 | `D_PrecioOferta` |
| Productos en catálogo | 21.235 | `D_PrecioProducto` |
| EAN distintos | 14.356 | `D_PrecioProducto.Ean` |
| Productos comparables en ≥ 3 cadenas | 1.491 | join por EAN entre cadenas |
| Brecha máxima en el caso de prueba | +22,7 % ($606) | `cli.comparar --ean` |

Las cifras se recalculan con los comandos de la sección 4: no hay valores escritos a mano en el
código.

El dataset operativo proviene del relevamiento del TP II; el MVP del OPCB se apoya en esa base y
restringe la canasta a tres cadenas (SEPA, La Banderita y Coope) para que la comparación sea
verificable. Las doce cadenas cargadas quedan disponibles para consultas puntuales.

<p align="center">
  <em>Capturas del tablero y de la comparación: carpeta <code>capturas/</code>.</em>
</p>

---

## Estructura del repositorio

```text
tp2-precios-supermercados-etl/
├── cli/                 # comandos de línea de comandos
├── config/              # configuración y rutas
├── etl/
│   ├── conn/            # conectores por cadena (vtex, coope, la_banderita, sepa)
│   └── dominios/
│       ├── precios/     # normalización, esquema, repositorio
│       └── comparador/  # matching y canasta
├── sql/                 # esquema y migraciones (D_Precio*, compras, vistas)
├── tests/               # pruebas
├── capturas/            # evidencias (comparaciones, tablero)
├── docs/proyecto/       # planificación, documentación, trello y presentación
├── *.bat                # atajos de ejecución
├── .env.template
├── pyproject.toml
├── pytest.ini
├── LICENSE
└── README.md
```

---

## Ética y datos

El proyecto publica precios de terceros y conclusiones sobre el costo de vida. Por eso:

- todo precio publicado tiene fecha, cadena, sucursal y origen;
- las limitaciones metodológicas son visibles en el informe y en la presentación;
- no se extraen datos personales;
- se respetan los términos de uso y el bajo volumen de consultas.

Informe completo:
[`docs/proyecto/02-documentacion/informe-etica.md`](docs/proyecto/02-documentacion/informe-etica.md).

---

## Gestión del proyecto

- Repositorio de la entrega: <https://github.com/Nicaleluc/tp-final-opcb>
- Repositorio de código: <https://github.com/Nicaleluc/tp2-precios-supermercados-etl>
- Tablero Trello: <https://trello.com/b/8kXtbi62/opcb-observatorio-de-precios-de-la-canasta-basica>
- Bitácora y decisiones:
  [`docs/proyecto/02-documentacion/bitacora.md`](docs/proyecto/02-documentacion/bitacora.md)
- Sprint planning:
  [`docs/proyecto/01-planificacion/sprint-planning.md`](docs/proyecto/01-planificacion/sprint-planning.md)

---

## Roadmap

- [x] Ingesta de cadenas (VTEX, Coope, La Banderita, SEPA)
- [x] Normalización y matching por EAN
- [x] Canasta y variación
- [x] Comparación por producto y brecha entre cadenas
- [ ] Alertas por umbral
- [ ] Carga diaria programada
- [ ] Serie histórica de 12 meses
- [ ] API pública de consulta

---

## Autor

**Nicolás Lucero** — Administrador de Bases de Datos y estudiante de Ciencia de Datos e IA.
[GitHub](https://github.com/Nicaleluc) · [LinkedIn](https://www.linkedin.com/in/nicolas-lucero)

Proyecto académico — Instituto Nuevos Aires, Prácticas Profesionalizantes I (2026).

## Licencia

MIT. Ver [`LICENSE`](LICENSE).
