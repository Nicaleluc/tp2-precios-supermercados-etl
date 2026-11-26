# 4. Planificación de sprints

> **Estado:** Sprint 0, 1 y 2 `implementado` (registro de cada ceremonia en
> `02-documentacion/bitacora.md`).

## 4.1 Capacidad y velocidad

| Parámetro | Valor | Fundamento |
|---|---|---|
| Duración del sprint | 4 días | proyecto total de 10 días |
| Dedicación diaria | 3,5 h | compatible con el trabajo full-time |
| Capacidad por sprint | 14 h | 4 × 3,5 h |
| Velocidad estimada | 12 puntos | 1 punto ≈ 1 h; 2 h de reserva para imprevistos |
| Reserva de riesgo | 2 h/sprint | cambios de formato, bloqueos de acceso |

**Calibración:** la equivalencia 1 punto = 1 hora es una hipótesis inicial. Se corrige en la
retrospectiva del Sprint 1 comparando estimado contra real.

---

## 4.2 Sprint 0 — Planificación (14–16/11/2026)

**Objetivo:** dejar el proyecto listo para ejecutar: problema definido, alcance cerrado, backlog
priorizado, tablero y repositorio creados.

| Tarea | Resultado | Estado |
|---|---|---|
| Redactar definición del proyecto | `proyecto.md` | implementado |
| Definir roles, RACI y ceremonias | `roles.md` | implementado |
| Construir y estimar el product backlog | `product-backlog.md` | implementado |
| Planificar sprints y capacidad | `sprint-planning.md` | implementado |
| Diseñar la estructura del tablero Trello | `03-trello/` | implementado |
| Crear el repositorio y el README base | [github.com/Nicaleluc/tp2-precios-supermercados-etl](https://github.com/Nicaleluc/tp2-precios-supermercados-etl) | implementado |
| Redactar el borrador del informe de ética | `02-documentacion/informe-etica.md` | implementado |

**Revisión del Sprint 0:** el alcance quedó cerrado en 24 puntos Must. Se excluyeron predicción,
alertas y aplicación móvil para proteger la fecha de entrega.

---

## 4.3 Sprint 1 — Datos y canasta (17–20/11/2026)

**Sprint Goal:** *Al final del Sprint 1, el repositorio calcula el costo de una canasta de 30
productos para tres cadenas, con datos normalizados y trazables, verificado por tests.*

**Sprint Backlog (12 puntos):**

| ID | Historia | Puntos | Tareas técnicas |
|---|---|---|---|
| HU-01 | Ingesta de tres cadenas | 3 | adaptar conectores del TP II · comando de carga · reporte por cadena |
| HU-02 | Histórico con fecha y origen | 2 | esquema con `fecha_relevamiento` y `origen` · upsert idempotente · test de duplicados |
| HU-03 | Normalización | 3 | reglas de texto y unidades · validación de EAN · tests de casos |
| HU-04 | Canasta de 30 productos | 2 | documento de criterio · archivo `canasta.csv` · test de 30 ítems |
| HU-05 | Costo y variación | 2 | cálculo por cadena · fórmula de variación · test contra cálculo manual |

**Riesgos del sprint:**

- R1 (cambio de formato): se mitiga con un conector aislado por cadena y datos del TP II de respaldo.
- R2 (matching bajo): se mide recién en Sprint 2; en Sprint 1 se valida la calidad del EAN.

**Criterio de aceptación del sprint:** los 5 tests pasan y el reporte muestra 3 cadenas cargadas.

### Ceremonias del Sprint 1

| Fecha | Ceremonia | Resultado |
|---|---|---|
| 17/11 09:00 | Sprint Planning 1 | sprint backlog comprometido (12 pts) |
| 17–20/11 | Daily Scrum | 4 entradas en la bitácora |
| 20/11 18:00 | Sprint Review 1 | demostración del cálculo de canasta |
| 20/11 18:30 | Retrospective 1 | acciones de mejora para el Sprint 2 |

---

## 4.4 Sprint 2 — Producto y cierre (21–24/11/2026)

**Sprint Goal:** *Al final del Sprint 2, el OPCB entrega un MVP demostrable: comparación entre
cadenas, dashboard, informe automático y documentación técnica y ética completa.*

**Sprint Backlog (12 puntos):**

| ID | Historia | Puntos | Tareas técnicas |
|---|---|---|---|
| HU-06 | Matching entre cadenas | 3 | matching por EAN · similitud de texto · reporte de cobertura · tests de pares |
| HU-07 | Comparación y brecha | 2 | ordenamiento por costo · brecha en $ y % · test de cálculo |
| HU-08 | Dashboard | 3 | vista de evolución · comparación por fecha · nota metodológica · prueba de performance |
| HU-09 | Informe automático | 2 | plantilla Markdown · generación por comando · inclusión de fuentes y limitaciones |
| HU-10 | Calidad y trazabilidad | 2 | validaciones · log de descartes · tests de integridad |

**Riesgos del sprint:**

- R3 (tiempo): el cierre documental compite con el desarrollo; se reserva el 24/11 solo para
  revisión y ensayo.
- R5 (conclusiones erróneas): revisión del informe contra los criterios de aceptación antes de
  publicar.

**Criterio de aceptación del sprint:** dashboard e informe generados desde el mismo dataset, README
y ética completos, checklist de la entrega al 100 %.

### Ceremonias del Sprint 2

| Fecha | Ceremonia | Resultado |
|---|---|---|
| 21/11 09:00 | Sprint Planning 2 | sprint backlog comprometido (12 pts) |
| 21–23/11 | Daily Scrum | 3 entradas en la bitácora |
| 23/11 18:00 | Sprint Review 2 | MVP demostrado y aceptado |
| 23/11 18:30 | Retrospective 2 | cierre y lecciones aprendidas |
| 24/11 | Ensayo de defensa | presentación cronometrada (12 min) |

---

## 4.5 Registro de impedimentos

| Fecha | Impedimento | Impacto | Acción | Estado |
|---|---|---|---|---|
| — | (se completa durante la ejecución) | — | — | — |

---

## 4.6 Formato de retrospectiva

Cada retrospectiva responde tres preguntas y deja **una acción concreta con responsable y fecha**:

1. **Qué funcionó** (continuar).
2. **Qué no funcionó** (detener).
3. **Qué probamos en el próximo sprint** (empezar).

Las conclusiones se registran en `02-documentacion/bitacora.md` y se reflejan en el tablero.
