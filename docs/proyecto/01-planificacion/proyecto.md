# 1. Definición del proyecto

**Proyecto:** Observatorio de Precios de la Canasta Básica (OPCB)
**Cliente simulado:** Asociación de Consumidores de Bahía Blanca (ACBB), entidad ficticia
**Responsable:** Nicolás Lucero (roles de Product Owner, Scrum Master y equipo de desarrollo)
**Período:** 14/11/2026 – 24/11/2026 (2 sprints de 4 días + Sprint 0)
**Metodología:** Scrum adaptado a un equipo unipersonal, con artefactos y ceremonias registradas

---

## 1.1 Resumen ejecutivo

El OPCB mide el costo de una canasta básica de 30 productos en las principales cadenas de
supermercados de Bahía Blanca y lo publica en un tablero público con su variación semanal. El
proyecto toma como base el ETL de catálogos, precios y sucursales ya construido en el TP II y lo
convierte en un producto mínimo viable: un dataset trazable, un dashboard, un informe automático y
un conjunto de reglas de calidad y de ética de publicación.

El alcance de esta entrega es el MVP. No incluye predicción de precios, aplicación móvil ni
publicación en producción: esas funcionalidades quedan en el backlog futuro, priorizadas y
documentadas, pero explícitamente fuera del compromiso de estos dos sprints.

---

## 1.2 Contexto y problema

En Argentina, la información de precios de supermercados existe pero está fragmentada: cada cadena
publica su catálogo en un formato distinto, con nombres de producto, unidades y códigos (EAN) que
no coinciden entre sí. Para un consumidor, comparar el costo de la misma canasta entre cadenas
exige revisar sitio por sitio, producto por producto. Para una asociación de consumidores, el
problema es mayor: sin una serie comparable y trazable, cualquier denuncia o recomendación pública
carece de respaldo verificable.

**Problema central:** no hay una fuente abierta, reproducible y actualizada que permita comparar el
costo de la misma canasta de productos entre cadenas de supermercados de la ciudad y seguir su
evolución en el tiempo.

**A quién afecta:**

- Consumidores que deciden dónde comprar y no pueden comparar una canasta completa.
- La ACBB, que necesita evidencia defendible para sus comunicaciones.
- Periodistas y docentes que requieren una serie de precios citable y metodológicamente explícita.

**Por qué importa:** una diferencia del 10–15 % en el costo de una canasta mensual tiene impacto
directo en el presupuesto de un hogar. La falta de comparabilidad no es un problema de datos
menor: es una barrera concreta para decidir mejor.

**Cómo ayuda la ciencia de datos:** integrando catálogos heterogéneos, normalizando nombres y
unidades, resolviendo el matching de productos entre cadenas y calculando una serie de precios
comparable, auditable y actualizable con automatización.

---

## 1.3 Objetivos

### Objetivo general

Construir un MVP reproducible que calcule el costo de una canasta básica de 30 productos en al
menos tres cadenas de supermercados de Bahía Blanca, lo publique en un dashboard y genere un informe
automático con su variación, en un plazo de diez días y con documentación completa.

### Objetivos específicos (SMART)

| N.º | Objetivo específico | Métrica de cumplimiento | Fecha |
|---|---|---|---|
| OE1 | Integrar los catálogos de tres cadenas y persistir el histórico de precios con fecha de relevamiento | 3 cadenas cargadas, 100 % de los registros con fecha y origen | 19/11 |
| OE2 | Normalizar nombres, unidades y EAN, y resolver el matching entre cadenas | ≥ 70 % de los productos de la canasta matcheados en ≥ 2 cadenas | 20/11 |
| OE3 | Definir y calcular la canasta de 30 productos con su variación semanal | canasta calculada para las 3 cadenas, variación con fórmula documentada | 20/11 |
| OE4 | Publicar el dashboard y el informe automático | dashboard operativo y informe generado en < 60 s sin intervención manual | 23/11 |
| OE5 | Documentar el proyecto con README, informe de ética y bitácora | 100 % de los artefactos de la consigna presentes | 24/11 |

> Los objetivos son medibles porque cada uno tiene una métrica binaria o numérica verificable en
> el repositorio (tests, reportes generados, capturas y registro de commits).

---

## 1.4 Alcance

### Incluye (MVP, 2 sprints)

- Ingesta de catálogos de tres cadenas (SEPA, La Banderita y Coope) y persistencia del histórico.
- Normalización de nombres, unidades y EAN; matching entre cadenas por EAN y similitud de texto.
- Canasta básica de 30 productos con criterio de selección documentado.
- Cálculo del costo de la canasta por cadena y de la variación semanal.
- Dashboard con evolución del costo, comparación entre cadenas y detalle por producto.
- Informe automático en Markdown con metodología, resultados y limitaciones.
- Tests de normalización, matching y reglas de calidad de datos.
- README profesional, informe de ética y bitácora de trabajo.

### No incluye (backlog futuro, fuera del compromiso)

- Predicción de precios o modelos de series temporales.
- Aplicación móvil o web pública autenticada.
- Integración con ERP, e-commerce o sistemas de terceros.
- Publicación en infraestructura cloud productiva con alta disponibilidad.
- Alertas automáticas por correo o mensajería.
- Cobertura de comercios minoristas que no publiquen catálogo online.

> **Por qué se recorta:** con 32 horas disponibles y un solo responsable, ampliar el alcance
> pondría en riesgo la calidad del MVP. La decisión se registra en el backlog como priorización
> MoSCoW y se revisa en la retrospectiva.

---

## 1.5 Stakeholders

| Stakeholder | Rol | Interés | Influencia | Expectativa |
|---|---|---|---|---|
| ACBB (cliente simulado) | Comitente | Evidencia pública y defendible | Alta | Informe claro, metodología explícita y sin sobrepromesas |
| Docente / comité evaluador | Auditor | Verificar proceso, herramientas y ética | Alta | Artefactos completos y coherentes |
| Consumidores | Usuarios finales | Comparar y decidir | Baja | Dashboard simple y datos actualizados |
| Cadenas de supermercados | Terceros afectados | Que sus precios se reporten correctamente | Media | Sin errores de atribución ni comparaciones inválidas |
| Comunidad open source | Revisores técnicos | Código reutilizable | Baja | README, tests y licencia |

---

## 1.6 Entregables

| ID | Entregable | Formato | Componente de la consigna |
|---|---|---|---|
| E-01 | Documento de definición del proyecto | Markdown | A |
| E-02 | Equipo, roles y matriz RACI | Markdown | A |
| E-03 | Product backlog priorizado y estimado | Markdown + Trello | A |
| E-04 | Planificación de sprints y sprint backlogs | Markdown + Trello | A |
| E-05 | Tablero Trello con flujo de trabajo | Tablero + capturas | B |
| E-06 | Repositorio GitHub con código y commits | Repositorio | B |
| E-07 | README profesional del repositorio | Markdown/HTML | C |
| E-08 | Informe de ética | Markdown/PDF | C |
| E-09 | Bitácora de trabajo y retrospectivas | Markdown | B/C |
| E-10 | Presentación final y guion | PDF/PPTX + Markdown | D |

---

## 1.7 Recursos

| Tipo | Detalle |
|---|---|
| **Humanos** | 1 responsable con roles de PO, SM y desarrollo (equipo simulado) |
| **Tecnológicos** | Python 3.12, SQL Server, `pyodbc`, `pytest`, Git/GitHub, Trello, VS Code |
| **Información** | Catálogos públicos de precios de SEPA, La Banderita y Coope; datos del TP II; documentación de las APIs |
| **Tiempo** | 32 horas estimadas: Sprint 0 (4 h), Sprint 1 (14 h), Sprint 2 (14 h) |
| **Económicos** | Sin presupuesto: herramientas gratuitas o de uso personal |

### Supuestos

- Las tres cadenas mantienen sus catálogos públicos accesibles durante el período del proyecto.
- La instancia de SQL Server local está disponible para pruebas de integración.
- El volumen de datos del período alcanza para calcular una variación semanal representativa.

### Restricciones

- Plazo fijo de entrega: 24/11/2026, 23:59 h.
- Un solo responsable: no hay capacidad para trabajo en paralelo real.
- Sin credenciales de producción: el MVP se ejecuta en entorno local.
- Los catálogos pueden cambiar de estructura sin aviso.

---

## 1.8 Riesgos

| ID | Riesgo | Prob. | Impacto | Mitigación | Responsable |
|---|---|---|---|---|---|
| R1 | Una cadena cambia el formato o bloquea el acceso | Media | Alto | Capa de conexión aislada por cadena + datos del TP II como respaldo | Dev |
| R2 | Matching entre cadenas por debajo del 70 % | Alta | Alto | EAN como llave primaria y similitud de texto como respaldo; revisión manual de la canasta | Dev |
| R3 | Falta de tiempo por superposición laboral | Alta | Alto | Alcance MoSCoW cerrado y recorte del backlog futuro | PO |
| R4 | Datos incompletos o precios en cero | Media | Medio | Reglas de validación y descarte documentado | Dev |
| R5 | Conclusiones erróneas por canasta poco representativa | Media | Alto | Criterio de selección explícito y sección de limitaciones en el informe | PO |
| R6 | Incumplimiento de condiciones de uso de los sitios | Baja | Alto | Revisión de términos, bajo volumen de consultas y atribución de la fuente | PO |

---

## 1.9 Criterios de éxito

| Criterio | Umbral | Cómo se verifica |
|---|---|---|
| Cobertura de cadenas | 3 de 3 | reporte de carga |
| Cobertura de la canasta | 30 de 30 productos | reporte de canasta |
| Matching entre cadenas | ≥ 70 % en ≥ 2 cadenas | test + reporte |
| Calidad de datos | 0 precios ≤ 0, 0 duplicados por día/producto | tests de integridad |
| Reproducibilidad | pipeline corre de punta a punta con un comando | README + ejecución |
| Documentación | 100 % de artefactos de la consigna | checklist de la entrega |
| Plazo | entrega antes del 24/11/2026 23:59 | fecha de commit/tag |

---

## 1.10 Cronograma

| Etapa | Fechas | Actividades principales | Hito verificable |
|---|---|---|---|
| **Sprint 0 — Planificación** | 14–16 nov | definición, objetivos, alcance, roles, backlog, tablero, repositorio | planificación aprobada |
| **Sprint 1 — Datos y canasta** | 17–20 nov | ingesta, normalización, canasta, cálculo, tests | dataset + canasta calculada |
| **Sprint 2 — Producto y cierre** | 21–24 nov | matching, comparación, dashboard, informe, README, ética | MVP + documentación |
| **Entrega** | 24 nov | revisión final, PDF, enlaces, ensayo | entrega en el aula virtual |
| **Defensa** | semana 16 | presentación y preguntas del comité | presentación oral |

### Detalle del Sprint 1 y 2

| Día | Fecha | Foco |
|---|---|---|
| 1 | 17/11 | Sprint Planning 1 + ingesta de catálogos |
| 2 | 18/11 | normalización de nombres, unidades y EAN |
| 3 | 19/11 | canasta de 30 productos + cálculo de costo |
| 4 | 20/11 | tests + Sprint Review y Retrospective 1 |
| 5 | 21/11 | Sprint Planning 2 + matching entre cadenas |
| 6 | 22/11 | comparación, brecha y dashboard |
| 7 | 23/11 | informe automático, README, ética + Review/Retro 2 |
| 8 | 24/11 | revisión final, empaquetado y ensayo de defensa |

---

## 1.11 Enfoque metodológico

Se adopta **Scrum** con las siguientes adaptaciones, justificadas por el tamaño del equipo:

1. **Un solo responsable** asume PO, SM y desarrollo. Para evitar el conflicto de intereses, cada
   ceremonia se registra por separado y las decisiones de alcance se documentan con su fundamento.
2. **Sprints de 4 días**, no de 2 semanas: el proyecto completo dura 10 días. Es la unidad mínima
   que permite un incremento demostrable.
3. **Ceremonias reducidas**: planning (30 min), daily (10 min), review (20 min) y retrospectiva
   (15 min). La reducción es proporcional a la duración del sprint.
4. **Definición de Terminado (DoD)** obligatoria para cada historia: código, test, documentación y
   commit. Una historia sin test no se considera terminada.

El detalle de roles, ceremonias y artefactos está en `roles.md`; el backlog, en
`product-backlog.md`; y la planificación de cada sprint, en `sprint-planning.md`.
