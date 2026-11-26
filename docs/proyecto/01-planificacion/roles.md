# 2. Equipo, roles y ceremonias

## 2.1 Composición del equipo

El proyecto es individual. Para reproducir las condiciones de un equipo real, el responsable asume
los tres roles de Scrum y los ejecuta en sesiones separadas, con registro de cada ceremonia. El
cliente y el comité evaluador son stakeholders externos simulados o reales.

| Rol | Quién | Responsabilidad principal | Entregable asociado |
|---|---|---|---|
| **Product Owner (PO)** | Nicolás Lucero | Definir el problema, priorizar el backlog y aceptar los incrementos | `proyecto.md`, `product-backlog.md` |
| **Scrum Master (SM)** | Nicolás Lucero | Facilitar ceremonias, eliminar impedimentos y cuidar el proceso | `bitacora.md`, retrospectivas |
| **Equipo de desarrollo** | Nicolás Lucero | Diseñar, implementar, testear y documentar | repositorio, dashboard, informe |
| **Cliente (ACBB)** | Entidad simulada | Validar que el producto responda a la necesidad | criterios de aceptación |
| **Comité evaluador** | Docente y pares | Auditar proceso, herramientas y ética | rúbrica de la consigna |

### Riesgo de concentración de roles y mitigación

Que una misma persona sea PO, SM y desarrollo elimina la separación de intereses que Scrum busca
proteger: el PO podría aceptar un incremento incompleto para cumplir el plazo. La mitigación es
explícita:

1. **Criterios de aceptación escritos antes de codificar.** El PO no puede cambiar la definición de
   "terminado" a mitad del sprint.
2. **Sesiones separadas por rol.** El planning y la review se registran como reuniones con fecha,
   hora y decisión, no como una nota informal.
3. **Revisión externa.** Al cierre, se pide lectura crítica a un par y se registra el feedback.
4. **Congelamiento de alcance.** Lo que no está en el sprint backlog no se desarrolla hasta la
   retrospectiva.

---

## 2.2 Matriz RACI

**R** = responsable de ejecutar · **A** = aprueba · **C** = consultado · **I** = informado

| Actividad | PO | SM | Dev | Cliente | Comité |
|---|---|---|---|---|---|
| Definir problema y objetivos | A/R | C | C | C | I |
| Priorizar el product backlog | A/R | C | C | C | I |
| Estimar historias | C | I | A/R | I | I |
| Planificar el sprint | A | R | R | I | I |
| Implementar historias | I | I | A/R | I | I |
| Ejecutar tests y control de calidad | I | I | A/R | I | I |
| Aceptar el incremento | A/R | I | C | C | I |
| Gestionar impedimentos | C | A/R | C | I | I |
| Documentar y publicar | C | C | A/R | I | I |
| Informe de ética | A/R | C | C | C | I |
| Presentación final | R | R | R | I | A |

---

## 2.3 Ceremonias y cadencia

| Ceremonia | Cuándo | Duración | Objetivo | Evidencia |
|---|---|---|---|---|
| Sprint Planning | inicio de cada sprint | 30 min | seleccionar historias y armar el sprint backlog | acta en `sprint-planning.md` |
| Daily Scrum | cada día de trabajo | 10 min | sincronizar avance e impedimentos | línea en `bitacora.md` |
| Sprint Review | fin de cada sprint | 20 min | demostrar el incremento y aceptarlo o rechazarlo | acta + captura |
| Sprint Retrospective | después de la review | 15 min | identificar mejoras del proceso | acta en `bitacora.md` |
| Refinamiento del backlog | antes de cada planning | 20 min | aclarar criterios y estimaciones | cambios en el backlog |

### Calendario de ceremonias

| Fecha | Ceremonia | Resultado esperado |
|---|---|---|
| 16/11 | Sprint 0 — Planning inicial | planificación y tablero listos |
| 17/11 09:00 | Sprint Planning 1 | sprint backlog 1 comprometido |
| 17–20/11 | Daily Scrum | bitácora diaria |
| 20/11 18:00 | Sprint Review 1 + Retrospective 1 | incremento 1 aceptado |
| 21/11 09:00 | Sprint Planning 2 | sprint backlog 2 comprometido |
| 21–23/11 | Daily Scrum | bitácora diaria |
| 23/11 18:00 | Sprint Review 2 + Retrospective 2 | MVP aceptado |
| 24/11 | Ensayo de defensa | presentación cronometrada |

---

## 2.4 Artefactos de Scrum

| Artefacto | Dónde vive | Regla de uso |
|---|---|---|
| **Product Backlog** | `product-backlog.md` + lista Trello "Product Backlog" | solo el PO prioriza; toda historia tiene criterios de aceptación |
| **Sprint Backlog** | `sprint-planning.md` + listas Trello "Sprint 1" y "Sprint 2" | se congela al inicio del sprint |
| **Incremento** | repositorio GitHub (tag por sprint) | debe cumplir la DoD |
| **Tablero** | Trello (listas: Backlog, Sprint, En curso, En revisión, Hecho, Impedimentos) | se actualiza a diario |

### Definición de Preparado (Definition of Ready)

Una historia entra al sprint solo si:

- tiene un objetivo de negocio claro;
- tiene criterios de aceptación verificables;
- está estimada en puntos;
- no depende de una historia no terminada del mismo sprint;
- tiene identificados los datos o insumos necesarios.

### Definición de Terminado (Definition of Done)

Una historia se considera terminada solo si:

1. el código corre sin errores en el entorno local;
2. tiene al menos un test automatizado que la cubre;
3. la documentación afectada está actualizada;
4. el cambio está commiteado con mensaje descriptivo;
5. el PO revisó el criterio de aceptación y lo marcó como cumplido.

---

## 2.5 Comunicación y gestión de conflictos

Aunque el equipo sea unipersonal, se documenta el protocolo porque la consigna evalúa trabajo en
equipo y gestión de conflictos (Clase 12):

| Situación | Estrategia | Registro |
|---|---|---|
| Presión por ampliar alcance ("una funcionalidad más") | negociar con MoSCoW; si no entra, va al backlog futuro | decisión en `bitacora.md` |
| Dos alternativas técnicas válidas | evaluar por criterio escrito: menor riesgo, menor costo, mayor valor | ADR breve en el repo |
| Error propio detectado tarde | reconocerlo, registrar el impacto y corregir sin ocultarlo | entrada de impedimento |
| Desacuerdo con el "cliente" simulado | volver al problema y a los criterios de aceptación, no a la preferencia personal | acta de review |

**Criterio de desempate:** ante un conflicto de prioridades, gana la opción que reduce el riesgo de
publicar una conclusión incorrecta. En un observatorio de precios, un dato mal presentado es peor
que un dato faltante.

---

## 2.6 Herramientas

| Herramienta | Uso en el proyecto |
|---|---|
| **Trello** | tablero de flujo (backlog, sprint, en curso, en revisión, hecho, impedimentos) |
| **GitHub** | repositorio, commits, issues, tag por sprint, README |
| **Git** | control de versiones local y ramas por historia |
| **Python + SQL Server** | pipeline de datos y persistencia |
| **pytest** | pruebas automatizadas |
| **Markdown** | documentación y bitácora |
