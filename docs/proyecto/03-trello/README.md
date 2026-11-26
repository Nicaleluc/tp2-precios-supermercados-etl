# 7. Tablero Trello — estructura, importación y evidencia

## 7.0 Tablero publicado

**Link:** https://trello.com/b/8kXtbi62/opcb-observatorio-de-precios-de-la-canasta-basica

Estado al 24/11/2026: **7 listas y 21 tarjetas** cargadas (4 en Product Backlog, 5 en Sprint 1,
5 en Sprint 2, 7 en Hecho; En curso, En revisión e Impedimentos vacías al cierre del proyecto).
El archivo `tablero-import.csv` es la versión del CSV optimizada para importar (listas con los
nombres definitivos, etiquetas separadas por coma y fecha de vencimiento por sprint).

## 7.1 Estructura del tablero

**Nombre del tablero:** `OPCB — Observatorio de Precios de la Canasta Básica`

| Lista | Para qué | Regla de WIP |
|---|---|---|
| **Product Backlog** | todo lo priorizado que no está comprometido | sin límite |
| **Sprint 1** | compromiso del primer sprint | 12 pts |
| **Sprint 2** | compromiso del segundo sprint | 12 pts |
| **En curso** | una sola tarjeta a la vez | límite 1 |
| **En revisión** | terminado técnicamente, pendiente de aceptación | límite 2 |
| **Hecho** | cumple la Definition of Done | — |
| **Impedimentos** | bloqueos que el SM debe resolver | — |

> El límite de una tarjeta en "En curso" es deliberado: con un solo responsable, el trabajo en
> paralelo es una ilusión que produce trabajo a medias. El tablero lo hace visible.

## 7.2 Etiquetas (labels)

| Etiqueta | Color sugerido | Uso |
|---|---|---|
| `must` | rojo | historia comprometida en el MVP |
| `should` | amarillo | backlog futuro prioritario |
| `wont` | gris | explícitamente fuera de esta release |
| `datos` | azul | ingesta, normalización, matching |
| `producto` | verde | canasta, comparación, dashboard |
| `calidad` | naranja | validaciones y tests |
| `documentacion` | violeta | README, ética, informe |
| `herramientas` | celeste | repo, tablero, CI |

## 7.3 Cómo recrear el tablero (respaldo)

El tablero **ya está publicado** (ver 7.0); esta sección queda como respaldo si hay que rehacerlo.

> **Nota:** Trello retiró la opción de importar CSV desde el menú del tablero. El tablero real se
> armó creando las 7 listas y cargando las 21 tarjetas una por una. `tablero-import.csv` conserva
> descripciones, etiquetas y fechas por si se cargan luego desde la API.

Columnas del CSV: `Card, List, Description, Labels, Due Date` (etiquetas separadas por coma;
`Due Date` en formato `AAAA-MM-DD`). Las descripciones incluyen criterios de aceptación y la
estimación en puntos.

## 7.4 Evidencia para la entrega (componente B)

La consigna pide "actualización real del trabajo". Para respaldarla, guardar en `03-trello/capturas/`:

| Captura | Cuándo | Qué debe mostrar |
|---|---|---|
| `01-tablero-inicial.png` | fin del Sprint 0 | las 7 listas y el backlog cargado |
| `02-sprint1-en-curso.png` | 18/11 | tarjetas en "En curso" y "En revisión" |
| `03-sprint1-review.png` | 20/11 | lista "Hecho" del Sprint 1 |
| `04-sprint2-en-curso.png` | 22/11 | avance del segundo sprint |
| `05-tablero-final.png` | 24/11 | estado final y tarjetas aceptadas |

Además, el historial de actividad de Trello (menú → **Actividad**) sirve como registro con fecha y
hora. Se puede exportar el tablero a JSON desde **Menú → Más → Imprimir, exportar y compartir →
Exportar como JSON** y guardarlo como `tablero-export.json`.

## 7.5 Tablero espejo (respaldo en Markdown)

`tablero.md` reproduce el estado del tablero sin depender de Trello. Sirve para dos cosas: dejar
evidencia versionable en el repositorio y permitir que el docente vea el flujo aunque el tablero
online cambie. **Debe actualizarse a la par del tablero real.**
