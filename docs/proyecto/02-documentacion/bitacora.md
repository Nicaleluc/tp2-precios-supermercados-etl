# 6. Bitácora de trabajo y registro de decisiones

> Registro cronológico del proyecto. Cada entrada indica fecha, ceremonia o actividad, decisión y
> evidencia. Este documento es la evidencia de "actualización real del trabajo" del componente B.
> Los impedimentos anotados al final salieron de la revisión de los datos cargados y quedaron
> corregidos en el código o en la documentación.

---

## 6.1 Sprint 0 — Planificación (14–16/11/2026)

### 14/11/2026 — Recepción de la consigna

- **Actividad:** lectura del enunciado del Proyecto Integrador Final.
- **Decisión:** usar el ETL de precios de supermercados del TP II como base del proyecto, en lugar
  de empezar un proyecto nuevo.
- **Fundamento:** ya existe un pipeline funcionando, lo que reduce el riesgo técnico y permite
  dedicar el tiempo a lo que evalúa esta consigna: planificación, herramientas y documentación.
  Además, el problema es real y verificable.
- **Evidencia:** `TP FINAL/Proyecto integrador-final.pdf`.

### 15/11/2026 — Definición del problema y alcance

- **Ceremonia:** sesión de Product Owner.
- **Decisión:** el alcance del MVP se limita a tres cadenas, una canasta de 30 productos, dashboard
  e informe. Se excluyen predicción, alertas, app móvil e integración con ERP.
- **Fundamento:** 32 horas disponibles y un solo responsable. Ampliar el alcance compromete la
  calidad y la fecha.
- **Evidencia:** `01-planificacion/proyecto.md` (secciones 1.4 y 1.8).

### 16/11/2026 — Backlog, tablero y artefactos iniciales

- **Ceremonia:** Sprint 0 Review + armado del backlog.
- **Decisiones:**
  1. El backlog queda en 24 puntos Must (12 + 12) y 12 puntos de backlog futuro.
  2. La escala es 1 punto ≈ 1 hora, calibrable en la retrospectiva del Sprint 1.
  3. El tablero Trello se estructura en siete listas: Product Backlog, Sprint 1, Sprint 2, En
     curso (límite 1), En revisión (límite 2), Hecho e Impedimentos.
  4. Las listas se separan por sprint para que el compromiso de cada uno sea visible; el trabajo
     real se sigue por "En curso" y "En revisión".
- **Fundamento:** priorizar la cadena de datos antes que la presentación evita construir un
  dashboard sobre datos sin normalizar.
- **Evidencia:** `01-planificacion/product-backlog.md`, `01-planificacion/sprint-planning.md`,
  `03-trello/` y el tablero publicado.

### Revisión del Sprint 0

| Pregunta | Respuesta |
|---|---|
| ¿Se cumplió el objetivo? | Sí: problema, alcance, roles, backlog y tablero definidos. |
| ¿Qué quedó pendiente? | Crear el repositorio GitHub y publicar la estructura. |
| ¿Qué riesgo apareció? | La fecha de entrega (24/11) deja poco margen para corregir. |
| Acción | Congelar alcance y reservar el 24/11 solo para revisión y ensayo. |

---

## 6.2 Sprint 1 — Datos y canasta (17–20/11/2026)

> **Estado:** implementado. Incremento: catálogos de las tres cadenas cargados, productos
> normalizados por EAN y canasta de 30 productos con costo y variación.

### 17/11/2026 — Sprint Planning 1

- **Asistentes:** PO, SM y Dev (misma persona, sesiones separadas).
- **Sprint Goal:** calcular el costo de la canasta de 30 productos para tres cadenas, con datos
  normalizados y trazables.
- **Compromiso:** HU-01, HU-02, HU-03, HU-04 y HU-05 (12 puntos).
- **Riesgos asumidos:** cambio de formato de una cadena; disponibilidad de SQL Server local.
- **Decisión de planificación:** cada conector queda aislado; si una cadena falla, las otras dos
  siguen y el error se registra. Se ejecuta primero la ingesta completa y recién después la
  normalización, para no reprocesar lo que falta.
- **Evidencia:** tarjetas HU-01 a HU-05 en la lista "Sprint 1" del tablero.

### 17–20/11/2026 — Daily Scrum

| Fecha | Ayer | Hoy | Impedimento |
|---|---|---|---|
| 17/11 | — | planning + conector SEPA | ninguno |
| 18/11 | ingesta VTEX y Coope | normalización de nombres, unidades y EAN | cadenas con el mismo producto escrito distinto (ver I-01) |
| 19/11 | normalización | armado de la canasta de 30 productos y su criterio de inclusión | productos sin EAN en el catálogo de una cadena (ver I-02) |
| 20/11 | canasta | costo, variación y casos de prueba; review del sprint | sachet y botella de 1 L con nombres casi iguales (ver I-03) |

### 20/11/2026 — Sprint Review 1

- **Incremento demostrado:** catálogos de las tres cadenas en la base, con fecha, sucursal y
  origen de cada precio; productos normalizados; canasta de 30 productos con costo total y
  variación contra la carga anterior.
- **Criterios de aceptación verificados:** cada precio conserva fecha y origen; los descartes
  (precio ≤ 0, EAN inválido) quedan registrados; la canasta se recalcula con un comando.
- **Aceptado:** sí, con el pendiente de ampliar la cobertura de matching en el Sprint 2.
- **Feedback del cliente simulado:** "sirve, pero necesito ver la comparación entre cadenas, no
  solo el total".

### 20/11/2026 — Retrospective 1

| Qué funcionó (continuar) | Qué no funcionó (detener) | Qué probamos (empezar) |
|---|---|---|
| Aislar los conectores por cadena | Cargar catálogos completos para probar (tarda y ensucia la base) | Probar con un término y un EAN antes de la carga completa |
| Guardar el origen y la fecha de cada precio | Comparar por nombre antes de normalizar | Fijar el EAN como llave y dejar el texto como desempate |

**Acción concreta:** usar el EAN como criterio principal de matching y reservar la similitud de
texto para los faltantes (responsable: Dev; desde el 21/11).

---

## 6.3 Sprint 2 — Producto y cierre (21–24/11/2026)

> **Estado:** implementado. Incremento: matching entre cadenas, comparación con brecha, dashboard,
> informe automático y documentación de la entrega.

### 21/11/2026 — Sprint Planning 2

- **Sprint Goal:** entregar un MVP demostrable con comparación entre cadenas, dashboard, informe
  automático y documentación completa.
- **Compromiso:** HU-06, HU-07, HU-08, HU-09 y HU-10 (12 puntos).
- **Decisiones de ajuste según retrospectiva 1:** el matching prioriza EAN exacto y solo después
  similitud de texto con umbral ≥ 70 %; toda comparación automática pasa por revisión manual de
  la canasta antes de publicarse.

### 21–24/11/2026 — Daily Scrum

| Fecha | Ayer | Hoy | Impedimento |
|---|---|---|---|
| 21/11 | — | planning + matching entre cadenas | el mismo EAN con precios distintos por sucursal (ver I-04) |
| 22/11 | matching | comparación por producto y cálculo de brecha | ninguno |
| 23/11 | comparación | dashboard, informe automático y documentación | ninguno |
| 24/11 | documentación | cierre, revisión de la entrega y armado de la presentación | ninguno |

### 23/11/2026 — Sprint Review 2

- **Incremento demostrado:** comparación del mismo producto entre cadenas con mínimo, máximo y
  brecha; caso de prueba sobre la leche Protein 1 L (nueve góndolas, +22,7 %); informe con
  metodología y límites; tablero y documentación de la entrega.
- **Aceptado:** sí.
- **Pendientes menores:** etiquetas, fechas y descripciones de las tarjetas del tablero (quedan
  cargadas en `03-trello/tablero-import.csv` para completarlas).

### 23/11/2026 — Retrospective 2

| Qué funcionó | Qué no funcionó | Qué aprendimos |
|---|---|---|
| El EAN como llave del matching | Estimación por puntos sin calibrar contra horas reales | Sin normalización previa, cualquier comparación es una suposición |
| Congelar el alcance a mitad del Sprint 2 | Documentar al final en vez de durante | La definición de terminado (código + test + documentación + commit) evita rehacer |

---

## 6.4 Registro de decisiones (ADR breve)

| ID | Fecha | Decisión | Alternativas evaluadas | Motivo |
|---|---|---|---|---|
| ADR-01 | 14/11 | Reutilizar el ETL del TP II | proyecto nuevo desde cero | menor riesgo técnico y foco en lo evaluado |
| ADR-02 | 15/11 | MVP de 24 puntos en 2 sprints | 3 sprints o alcance mayor | capacidad real de 32 h |
| ADR-03 | 16/11 | Matching por EAN primero, texto después | solo fuzzy o solo EAN | el EAN es determinístico; el texto cubre faltantes |
| ADR-04 | 16/11 | Sin predicción en el MVP | incluir modelo de series | el alcance y los datos no lo justifican |
| ADR-05 | 16/11 | Datos de precios separados de datos de compras | tabla única | privacidad y minimización |
| ADR-06 | 21/11 | La comparación automática se revisa antes de publicar | publicar directo desde la consulta | un error de identificación se lee como aumento de precio |

---

## 6.5 Impedimentos

| ID | Fecha | Impedimento | Impacto | Acción tomada | Estado |
|---|---|---|---|---|---|
| I-01 | 18/11 | La misma botella aparece con siete nombres distintos entre cadenas | sin normalizar, la comparación es imposible | normalización de nombres, unidades y EAN | resuelto |
| I-02 | 19/11 | Productos sin EAN en el catálogo de una cadena (ej. suplementos) | no se pueden emparejar por código | quedan fuera de la canasta y se registran como descarte | resuelto (documentado) |
| I-03 | 20/11 | Sachet y botella de 1 L con nombres casi idénticos (La Banderita: $2.750 vs. $2.699) | riesgo de comparar presentaciones distintas | EAN como llave + revisión manual de la canasta | resuelto |
| I-04 | 21/11 | El mismo EAN con precios distintos según sucursal (Express: $3.179 a $3.275) | la "brecha" puede ser interna a la cadena | se toma el último precio cargado y se declara la regla en el informe | resuelto (regla documentada) |

---

## 6.6 Trazabilidad de la entrega

| Artefacto | Versión | Fecha | Autor |
|---|---|---|---|
| Definición del proyecto | 1.0 | 16/11/2026 | Nicolás Lucero |
| Roles y ceremonias | 1.0 | 16/11/2026 | Nicolás Lucero |
| Product backlog | 1.0 | 16/11/2026 | Nicolás Lucero |
| Sprint planning | 1.0 | 16/11/2026 | Nicolás Lucero |
| Informe de ética | 1.0 | 16/11/2026 | Nicolás Lucero |
| Tablero Trello | 1.0 | 16/11/2026 | Nicolás Lucero |
| Tablero publicado (7 listas, 21 tarjetas) | 1.1 | 24/11/2026 | Nicolás Lucero |
| README del repositorio | 1.0 | 23/11/2026 | Nicolás Lucero |
| Presentación final (8 diapositivas) | 1.0 | 24/11/2026 | Nicolás Lucero |
