# Proyecto Integrador Final — Prácticas Profesionalizantes I

**Proyecto:** Observatorio de Precios de la Canasta Básica (OPCB)
**Estudiante:** Nicolás Lucero
**Carrera:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial — Instituto Nuevos Aires (INA)
**Materia:** Prácticas Profesionalizantes I
**Docente:** MSc. Ángel Daniel Fuentes S.
**Asignación:** 14/11/2026 · **Entrega:** 24/11/2026, 23:59 h
**Peso:** 40 % de la nota final

---

## 1. Qué es este proyecto

El OPCB es un proyecto **simulado** de ciencia de datos que reproduce el trabajo de un equipo
profesional: un cliente ficticio (la Asociación de Consumidores de Bahía Blanca, ACBB) necesita
medir y comunicar la evolución del costo de la canasta básica en supermercados de la ciudad.

El proyecto no inventa datos: reutiliza el ETL de catálogos y precios de supermercados
desarrollado en el TP II y lo lleva a un producto mínimo viable (MVP) con dashboard, informe
automático y reglas de calidad. Sobre esa base se documenta la planificación ágil, el uso de
herramientas colaborativas y la reflexión ética que exige esta consigna.

> **Aclaración de alcance académico:** la entidad cliente y el equipo son simulados. Los datos
> son reales y públicos; el código es propio. Se indica en cada artefacto qué está
> `implementado`, qué está `parcial` y qué está `previsto`.

---

## 2. Mapa de la entrega

La consigna califica cuatro componentes. Esta carpeta los resuelve así:

| Componente | Peso | Artefacto(s) | Estado |
|---|---|---|---|
| **A. Planificación del proyecto** | 25 % | `01-planificacion/proyecto.md` (problema, objetivos, alcance, stakeholders, riesgos, cronograma) · `01-planificacion/roles.md` · `01-planificacion/product-backlog.md` · `01-planificacion/sprint-planning.md` | implementado |
| **B. Ejecución y herramientas** | 25 % | **Tablero Trello publicado** ([trello.com/b/8kXtbi62](https://trello.com/b/8kXtbi62/opcb-observatorio-de-precios-de-la-canasta-basica)) · **repositorio de la entrega** [github.com/Nicaleluc/tp-final-opcb](https://github.com/Nicaleluc/tp-final-opcb) · **repositorio de código** [github.com/Nicaleluc/tp2-precios-supermercados-etl](https://github.com/Nicaleluc/tp2-precios-supermercados-etl) · `03-trello/tablero-import.csv` + `tablero.md` (estructura y respaldo) · `02-documentacion/bitacora.md` | implementado (tablero público, repo de entrega y repo de código) |
| **C. Documentación profesional** | 20 % | `README.md` del repositorio (publicado; borrador en `02-documentacion/README-repositorio.md`) · `02-documentacion/informe-etica.md` · este índice | implementado |
| **D. Presentación final** | 30 % | `04-presentacion/guion.md` (estructura, tiempos y preguntas anticipadas) · `04-presentacion/presentacion-opcb-completa.pptx` (8 diapositivas, con logo del INA) · `04-presentacion/diapositiva-opcb-sintesis.pptx` (síntesis del marco de trabajo) · `04-presentacion/TP_Final_OPCB_Resumen_Lucero.docx` (resumen de 2 páginas) | implementado (falta ensayo cronometrado) |

---

## 3. Estado real por artefacto

| Artefacto | Estado | Qué falta |
|---|---|---|
| Definición del proyecto, objetivos y alcance | implementado | — |
| Equipo, roles y ceremonias | implementado | — |
| Product backlog priorizado y estimado | implementado | — |
| Sprint planning (Sprint 0, 1 y 2) | implementado | — |
| Tablero Trello (7 listas, 21 tarjetas) | implementado | tablero **público**: link en `03-trello/README.md` 7.0; etiquetas, fechas y descripciones se cargan desde `tablero-import.csv` |
| Repositorio GitHub con código y commits | implementado | entrega publicada en `tp-final-opcb`; código en `tp2-precios-supermercados-etl` (9 commits) |
| README del repositorio | implementado | publicado en el repo; borrador en `02-documentacion/README-repositorio.md` |
| Informe de ética | implementado | revisión final de citas |
| Bitácora de trabajo | implementado | registro de Sprint 0, 1 y 2 en `02-documentacion/bitacora.md` |
| Presentación oral | implementado (deck) · parcial (ensayo) | 8 diapositivas listas; falta ensayo cronometrado |

---

## 4. Cómo leer esta entrega

1. **Empezar por** `01-planificacion/proyecto.md`: ahí está el problema, el objetivo y los límites.
2. **Seguir por** `01-planificacion/product-backlog.md` y `sprint-planning.md`: qué se construye,
   en qué orden y con qué capacidad.
3. **Verificar la ejecución** en `03-trello/`, en el tablero
   ([trello.com/b/8kXtbi62](https://trello.com/b/8kXtbi62/opcb-observatorio-de-precios-de-la-canasta-basica))
   y en los repositorios de GitHub
   ([`tp-final-opcb`](https://github.com/Nicaleluc/tp-final-opcb) y
   [`tp2-precios-supermercados-etl`](https://github.com/Nicaleluc/tp2-precios-supermercados-etl)).
4. **Cerrar** con `02-documentacion/informe-etica.md` y `04-presentacion/guion.md`.

---

## 5. Cronograma resumido

| Fecha | Etapa | Entregable |
|---|---|---|
| 14–16 nov | Sprint 0 — planificación | definición, roles, backlog, tablero, repo creado |
| 17–20 nov | Sprint 1 — ingesta y canasta | dataset normalizado + costo de canasta + tests |
| 21–23 nov | Sprint 2 — producto y cierre | dashboard, informe, README, ética, presentación |
| 24 nov | Entrega y ensayo | PDF/links en el aula virtual |
| Semana 16 | Defensa oral | presentación y respuestas al comité |

---

## 6. Checklist de la consigna

- [x] Definición clara del problema y del objetivo.
- [x] Identificación de roles y responsabilidades.
- [x] Backlog priorizado y estimado.
- [x] Planificación de sprints (planning, review, retrospective).
- [x] Tablero Trello publicado y con actividad real (7 listas, 21 tarjetas; [trello.com/b/8kXtbi62](https://trello.com/b/8kXtbi62/opcb-observatorio-de-precios-de-la-canasta-basica)).
- [x] Repositorio GitHub público con documentación y commits significativos (entrega en `tp-final-opcb`; código en `tp2-precios-supermercados-etl`).
- [x] Informe breve de ética.
- [x] Lenguaje técnico y profesional.
- [ ] Presentación final ensayada (deck de 8 diapositivas armado; falta ensayo cronometrado).
