# 8. Presentación final — guion y preparación

**Duración objetivo:** 12 minutos de exposición + 5–8 minutos de preguntas
**Formato:** `presentacion-opcb-completa.pptx` — 8 diapositivas (16:9, con logo del INA)
**Apoyo:** `diapositiva-opcb-sintesis.pptx` (síntesis formal del marco de trabajo, se puede insertar como diapositiva 5) · `TP_Final_OPCB_Resumen_Lucero.docx` (resumen de 2 páginas para el comité)
**Regla:** no leer la diapositiva; la diapositiva es el ancla visual, la explicación es oral.

**Correspondencia entre este guion (13 ideas) y el deck de 8 diapositivas:**

| Deck | Diapositiva | Ideas del guion que cubre |
|---|---|---|
| 1 | Portada | 1 |
| 2 | El ejemplo real (nueve góndolas, siete nombres) | 2 |
| 3 | Cómo el sistema lo convierte en un precio comparable | 9 |
| 4 | Metodología (Scrum en una persona) | 5 y 6 |
| 5 | El resultado: de $2.669 a $3.275 | 7, 8 y 10 |
| 6 | El riesgo real (botella vs. sachet) | 11 |
| 7 | La escala real (33.900 precios, 1.491 comparables) | 10 |
| 8 | Cierre | 12 y 13 |

Si el tiempo aprieta, la diapositiva 7 es la primera que se saltea: su contenido está en la 5.
Las ideas 3 (objetivo y alcance) y 4 (cliente y stakeholders) se dicen oralmente en la 2 y la 7.

---

## 8.1 Estructura y tiempos

| # | Diapositiva | Idea central | Tiempo | Acumulado |
|---|---|---|---|---|
| 1 | Portada | quién soy, qué proyecto presento | 0:30 | 0:30 |
| 2 | El problema | comparar una canasta hoy es manual y no verificable | 1:00 | 1:30 |
| 3 | Objetivo y alcance | qué sí y qué no promete el MVP | 1:00 | 2:30 |
| 4 | Cliente y stakeholders | a quién sirve y quién lo audita | 0:45 | 3:15 |
| 5 | Metodología | Scrum adaptado a un equipo unipersonal | 1:15 | 4:30 |
| 6 | Planificación | backlog, priorización y capacidad | 1:15 | 5:45 |
| 7 | Sprint 1 | datos y canasta: el incremento | 1:15 | 7:00 |
| 8 | Sprint 2 | producto: dashboard e informe | 1:15 | 8:15 |
| 9 | Arquitectura | cómo fluye el dato de la fuente al tablero | 0:45 | 9:00 |
| 10 | Resultados | métricas contra los criterios de éxito | 0:45 | 9:45 |
| 11 | Ética | los cinco riesgos y sus controles | 1:15 | 11:00 |
| 12 | Aprendizajes | qué me llevo y qué haría distinto | 0:45 | 11:45 |
| 13 | Cierre | una frase + invitación a preguntar | 0:15 | 12:00 |

---

## 8.2 Contenido y notas por diapositiva

### 1. Portada

- Nombre, carrera, materia, docente, fecha.
- Título: *Observatorio de Precios de la Canasta Básica*.
- **Frase de apertura:** "Voy a mostrar cómo convertí un ETL académico en un producto con cliente,
  backlog, tablero y una discusión ética sobre qué se publica."

### 2. El problema

- Mostrar tres capturas: el mismo producto con tres nombres y tres precios distintos.
- Dato clave: comparar 30 productos en 3 cadenas son 90 búsquedas manuales por semana.
- **No** empezar por la tecnología. Empezar por el costo de no tener el dato.

### 3. Objetivo y alcance

- Objetivo general en una línea.
- Dos columnas: **Incluye** (3 cadenas, 30 productos, dashboard, informe) / **No incluye**
  (predicción, app, integración ERP).
- **Mensaje:** el alcance recortado es una decisión profesional, no una falta.

### 4. Cliente y stakeholders

- Cliente simulado: Asociación de Consumidores de Bahía Blanca.
- Stakeholders: consumidores, cadenas (terceros afectados), comité, comunidad open source.
- **Mensaje:** las cadenas son terceros: un error nuestro las daña y nos expone.

### 5. Metodología

- Tres roles de Scrum asumidos por una persona.
- Cómo se evita el conflicto de intereses: criterios escritos antes de codificar, sesiones
  separadas, revisión externa.
- Sprints de 4 días, ceremonias reducidas.
- **Frase:** "Scrum no es una ceremonia; es una forma de hacer visible el costo de cambiar de
  opinión."

### 6. Planificación

- Product backlog: 10 historias MVP (24 pts) + 4 futuras.
- Priorización MoSCoW; primero la cadena de datos, después la presentación.
- Capacidad: 14 h por sprint, velocidad estimada 12 pts.
- Mostrar captura del tablero Trello.
- **Mensaje:** se planificó con la restricción real (32 h), no con la deseada.

### 7. Sprint 1 — Datos y canasta

- Incremento: catálogos de 3 cadenas cargados, productos normalizados, canasta de 30 calculada.
- Mostrar una tabla antes/después de la normalización.
- Mencionar los tests: cuántos, qué cubren.
- **Mensaje:** sin normalización no hay comparación; el dashboard viene después a propósito.

### 8. Sprint 2 — Producto

- Dashboard: evolución, comparación, nota metodológica.
- Informe automático: metodología, resultados, limitaciones.
- Demo en vivo de 60 segundos (o captura si falla internet).
- **Mensaje:** el producto no es el gráfico; es la decisión que habilita.

### 9. Arquitectura

- Diagrama de flujo: conectores → normalización → matching → SQL Server → canasta → dashboard.
- Explicar el aislamiento por cadena: si una falla, las otras siguen.
- **Mensaje:** la resiliencia se diseña, no se improvisa.

### 10. Resultados

- Tabla de criterios de éxito: cobertura, matching, calidad, reproducibilidad, plazo.
- Ser honesto con lo que no se alcanzó y por qué.
- **Mensaje:** un resultado con su límite explícito vale más que un número sin contexto.

### 11. Ética

- Los cinco riesgos: representatividad, identificación errónea, condiciones de uso, sobrepromesa,
  privacidad futura.
- Un control por riesgo, en una tabla de dos columnas.
- **Frase:** "En un observatorio de precios, un dato mal presentado es peor que un dato faltante."

### 12. Aprendizajes

- Tres aprendizajes concretos (técnico, de proceso y personal).
- Qué haría distinto con otra semana.
- **Mensaje:** capacidad de autocrítica, no catálogo de logros.

### 13. Cierre

- Una frase que resuma el aporte: "Pasé de administrar bases a construir un producto de datos con
  criterio profesional y límites explícitos."
- "Gracias. Quedo a disposición para las preguntas."

---

## 8.3 Preguntas anticipadas del comité

| Pregunta probable | Respuesta preparada (síntesis) |
|---|---|
| ¿Por qué solo tres cadenas? | Por capacidad y coherencia: tres permiten comparación real y son verificables. Menos sería anécdota; más, inviable en 32 h. |
| ¿Cómo evitan el sesgo de la canasta? | La canasta es una decisión explícita: se documenta su composición, se declara a quién representa y se listan las limitaciones. |
| ¿Qué pasa si una cadena cambia su sitio? | Cada conector está aislado; si falla, las otras siguen y el error queda registrado. Además hay datos del TP II como respaldo. |
| ¿Cómo garantizan que dos productos son el mismo? | EAN como llave primaria; similitud de texto y unidad como respaldo; umbral de confianza y revisión manual de la canasta. |
| ¿Por qué no predicen precios? | Sin serie histórica suficiente, predecir sería sobrepromesa. Está en el roadmap, no en el MVP. |
| ¿Qué rol te resultó más difícil? | El de Scrum Master: frenar el impulso de ampliar alcance. Lo resolví con el criterio de congelamiento y el registro de decisiones. |
| ¿Cómo gestionaste conflictos si trabajaste solo? | Documenté el protocolo de la Clase 12: separar el problema de la persona, registro de decisiones y criterio de desempate por riesgo. |
| ¿Qué harías con una semana más? | Cerrar la serie de 12 meses, programar la carga diaria y agregar alertas; el backlog futuro ya está priorizado. |
| ¿Cómo verificás que el dato es correcto? | Tests de normalización e integridad, log de descartes y revisión manual de una muestra contra el sitio. |
| ¿Qué aprendiste de Scrum que no sabías? | Que el valor está en hacer visible el trabajo y el costo de cambiar; no en las reuniones. |

---

## 8.4 Checklist de ensayo

- [ ] Cronometrar dos ensayos completos (objetivo: 11:30–12:00).
- [ ] Probar la demo en el equipo donde se va a presentar.
- [ ] Tener capturas de respaldo del dashboard y del tablero.
- [ ] Revisar que las cifras de la presentación coincidan con el informe final.
- [ ] Preparar una respuesta de 30 segundos para cada pregunta de la tabla.
- [ ] Cerrar el celular y las notificaciones.
