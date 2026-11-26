# Tablero espejo — estado al 24/11/2026 (cierre del proyecto)

> Respaldo versionable del tablero Trello publicado:
> <https://trello.com/b/8kXtbi62/opcb-observatorio-de-precios-de-la-canasta-basica>
> Se actualiza al cierre de cada jornada.
> Leyenda: ✅ hecho · 🔄 en curso · 👀 en revisión · ⬜ pendiente · ⛔ impedimento.

---

## 🔄 En curso (WIP: 0/1)

| Tarjeta | Etiqueta | Responsable | Nota |
|---|---|---|---|
| — | — | — | sin trabajo en curso al cierre |

---

## 👀 En revisión (WIP: 0/2)

| Tarjeta | Etiqueta | Nota |
|---|---|---|
| — | — | — |

---

## ✅ Hecho (Sprint 0 y cierre)

| Tarjeta | Etiqueta | Evidencia |
|---|---|---|
| Definir problema y alcance | planificación | `01-planificacion/proyecto.md` |
| Definir roles y ceremonias | planificación | `01-planificacion/roles.md` |
| Armar product backlog | planificación | `01-planificacion/product-backlog.md` |
| Planificar sprints | planificación | `01-planificacion/sprint-planning.md` |
| Diseñar tablero Trello | herramientas | `03-trello/README.md` (7 listas) |
| Redactar informe de ética | documentación | `02-documentacion/informe-etica.md` |
| Crear repositorio GitHub | herramientas | github.com/Nicaleluc/tp2-precios-supermercados-etl |

---

## ✅ Sprint 1 (12 pts) — entregado 20/11

| Tarjeta | Etiqueta | Pts | Estado | Criterio de aceptación (resumen) |
|---|---|---|---|---|
| HU-01 Ingesta de tres cadenas | must · datos | 3 | ✅ | 3 cadenas; error aislado; reporte; test |
| HU-02 Histórico con fecha y origen | must · datos | 2 | ✅ | upsert idempotente; test de duplicados |
| HU-03 Normalización | must · datos | 3 | ✅ | 10 casos de test; EAN válido |
| HU-04 Canasta de 30 productos | must · producto | 2 | ✅ | 30 ítems; criterio documentado |
| HU-05 Costo y variación | must · producto | 2 | ✅ | fórmula documentada; test manual |

**Sprint Goal:** calcular el costo de la canasta de 30 productos para tres cadenas, con datos
normalizados y trazables.

---

## ✅ Sprint 2 (12 pts) — entregado 23/11

| Tarjeta | Etiqueta | Pts | Estado | Criterio de aceptación (resumen) |
|---|---|---|---|---|
| HU-06 Matching entre cadenas | must · datos | 3 | ✅ | ≥ 70 % en ≥ 2 cadenas; tests |
| HU-07 Comparación y brecha | must · producto | 2 | ✅ | brecha en $ y %; test |
| HU-08 Dashboard | must · producto | 3 | ✅ | carga < 3 s; nota metodológica |
| HU-09 Informe automático | must · documentación | 2 | ✅ | < 60 s; fuentes y limitaciones |
| HU-10 Calidad y trazabilidad | must · calidad | 2 | ✅ | tests de integridad; log de descartes |

**Sprint Goal:** entregar un MVP demostrable con comparación entre cadenas, dashboard, informe
automático y documentación completa.

---

## ⬜ Product Backlog (no comprometido)

| Tarjeta | Etiqueta | Pts | Prioridad |
|---|---|---|---|
| HU-11 Alertas por umbral | should | 3 | Should |
| HU-12 Ficha de producto | should | 2 | Should |
| HU-13 Carga diaria programada | should | 2 | Should |
| HU-14 Predicción de precios | wont | 5 | Won't (esta release) |

---

## ⛔ Impedimentos

| ID | Fecha | Impedimento | Estado |
|---|---|---|---|
| I-01 | 18/11 | Mismo producto con siete nombres distintos entre cadenas | ✅ resuelto (normalización + EAN) |
| I-02 | 19/11 | Productos sin EAN en el catálogo de una cadena | ✅ documentado (quedan fuera de la canasta) |
| I-03 | 20/11 | Sachet y botella de 1 L con nombres casi idénticos | ✅ resuelto (EAN + revisión manual) |
| I-04 | 21/11 | Mismo EAN con precios distintos por sucursal | ✅ regla declarada en el informe |

---

## Historial de movimientos

| Fecha | Tarjeta | De | A |
|---|---|---|---|
| 16/11 | Definir problema y alcance | En curso | Hecho |
| 16/11 | Definir roles y ceremonias | En curso | Hecho |
| 16/11 | Armar product backlog | En curso | Hecho |
| 16/11 | Planificar sprints | En curso | Hecho |
| 16/11 | Diseñar tablero Trello | En curso | Hecho |
| 16/11 | Redactar informe de ética | En curso | Hecho |
| 20/11 | HU-01 a HU-05 | Sprint 1 | ✅ aceptadas en la Review 1 |
| 23/11 | HU-06 a HU-10 | Sprint 2 | ✅ aceptadas en la Review 2 |
| 24/11 | Crear repositorio GitHub | En curso | Hecho |
