# 3. Product backlog

## 3.1 Criterio de priorización

Se usa una versión simple de **MoSCoW** combinada con valor y riesgo:

1. **Must (MVP):** sin esto no existe el producto. Va a Sprint 1 o 2.
2. **Should:** mejora el producto pero puede esperar a una segunda versión.
3. **Could:** deseable, se evalúa según capacidad.
4. **Won't (esta release):** explícitamente fuera del alcance actual.

Dentro de los Must, se prioriza primero la **cadena de datos** (ingesta → normalización → cálculo)
porque todo lo demás depende de ella, y después la **presentación** (dashboard → informe). No se
empieza por el dashboard: un tablero lindo sobre datos sucios es una conclusión incorrecta con
mejor diseño.

**Escala de estimación:** 1 punto ≈ 1 hora de trabajo efectivo. Calibración inicial para un equipo
unipersonal; se ajusta en la retrospectiva del Sprint 1.

---

## 3.2 Épicas

| Épica | Objetivo | Historias | Puntos |
|---|---|---|---|
| **EP-01 — Ingesta y persistencia** | Traer catálogos y guardar el histórico con trazabilidad | HU-01, HU-02 | 5 |
| **EP-02 — Normalización y matching** | Hacer comparables productos de distintas cadenas | HU-03, HU-06 | 6 |
| **EP-03 — Canasta y cálculo** | Definir la canasta y calcular su costo y variación | HU-04, HU-05, HU-07 | 6 |
| **EP-04 — Producto y comunicación** | Publicar dashboard e informe automático | HU-08, HU-09 | 5 |
| **EP-05 — Calidad** | Validar integridad y trazabilidad del dato | HU-10 | 2 |
| **Backlog futuro** | Mejoras posteriores al MVP | HU-11 a HU-14 | 12 |

**Total MVP: 24 puntos** (12 en Sprint 1, 12 en Sprint 2).

---

## 3.3 Backlog priorizado (MVP)

| ID | Historia | Épica | Prioridad | Puntos | Sprint |
|---|---|---|---|---|---|
| HU-01 | Como analista, quiero descargar el catálogo de tres cadenas para tener una base de precios | EP-01 | Must | 3 | 1 |
| HU-02 | Como analista, quiero guardar cada precio con fecha de relevamiento y origen para poder reconstruir la serie | EP-01 | Must | 2 | 1 |
| HU-03 | Como analista, quiero normalizar nombres, unidades y EAN para que los productos sean comparables | EP-02 | Must | 3 | 1 |
| HU-04 | Como PO, quiero definir una canasta de 30 productos con criterio explícito para que la medición sea representativa | EP-03 | Must | 2 | 1 |
| HU-05 | Como analista, quiero calcular el costo de la canasta por cadena y su variación para publicar la serie | EP-03 | Must | 2 | 1 |
| HU-06 | Como analista, quiero matchear productos entre cadenas por EAN y similitud de texto para comparar el mismo bien | EP-02 | Must | 3 | 2 |
| HU-07 | Como analista, quiero comparar el costo de la canasta entre cadenas y calcular la brecha para informar al consumidor | EP-03 | Must | 2 | 2 |
| HU-08 | Como usuario, quiero un dashboard con la evolución y la comparación para decidir dónde comprar | EP-04 | Must | 3 | 2 |
| HU-09 | Como cliente, quiero un informe automático con metodología, resultados y limitaciones para comunicar con respaldo | EP-04 | Must | 2 | 2 |
| HU-10 | Como SM, quiero reglas de calidad y tests para no publicar datos inválidos | EP-05 | Must | 2 | 2 |

### Backlog futuro (no comprometido)

| ID | Historia | Prioridad | Puntos | Motivo de exclusión |
|---|---|---|---|---|
| HU-11 | Alertas automáticas cuando la variación supera un umbral | Should | 3 | requiere infraestructura de envío |
| HU-12 | Ficha de producto con histórico individual | Should | 2 | valor secundario para el MVP |
| HU-13 | Programar la carga diaria con el programador de tareas | Should | 2 | el MVP corre manual |
| HU-14 | Modelo de predicción de precios | Won't | 5 | el alcance no incluye predicción; sin serie suficiente |

---

## 3.4 Criterios de aceptación (historias MVP)

### HU-01 — Ingesta de tres cadenas

- [ ] El comando de carga obtiene datos de SEPA, La Banderita y Coope.
- [ ] Ante error de una cadena, las otras dos continúan y el error queda registrado.
- [ ] El reporte final indica cantidad de productos por cadena.
- [ ] Test: la función de parseo devuelve una lista no vacía con un fixture de muestra.

### HU-02 — Histórico con fecha y origen

- [ ] Cada registro guarda `fecha_relevamiento`, `cadena`, `sucursal` y `ean`.
- [ ] Correr la carga dos veces el mismo día no duplica registros del mismo producto y cadena.
- [ ] Test: inserción repetida no incrementa el conteo.

### HU-03 — Normalización

- [ ] Se normalizan mayúsculas, acentos, espacios y unidades (g/kg, ml/l).
- [ ] El EAN se conserva como texto y se validan 8 o 13 dígitos.
- [ ] Test: 10 casos de nombres y unidades conocidos se normalizan al valor esperado.

### HU-04 — Canasta de 30 productos

- [ ] La canasta tiene 30 productos agrupados por rubro (almacén, frescos, limpieza, bebidas).
- [ ] El criterio de selección está escrito y justificado en el documento.
- [ ] Test: la canasta tiene exactamente 30 ítems y no hay duplicados.

### HU-05 — Costo y variación

- [ ] Se calcula el costo total por cadena para una fecha dada.
- [ ] La variación semanal se calcula con la misma fórmula documentada en el informe.
- [ ] Test: con un dataset de ejemplo, el total y la variación coinciden con el cálculo manual.

### HU-06 — Matching entre cadenas

- [ ] Se matchea primero por EAN exacto y luego por similitud de nombre + unidad.
- [ ] El reporte indica el porcentaje de matching por cadena.
- [ ] Umbral de aceptación: ≥ 70 % de la canasta matcheada en al menos dos cadenas.
- [ ] Test: pares conocidos se matchean; pares distintos no.

### HU-07 — Comparación y brecha

- [ ] El reporte muestra el costo por cadena ordenado de menor a mayor.
- [ ] La brecha se expresa en pesos y en porcentaje respecto de la cadena más barata.
- [ ] Test: la brecha calculada coincide con la diferencia verificada a mano.

### HU-08 — Dashboard

- [ ] Muestra la evolución del costo de la canasta en el tiempo.
- [ ] Permite comparar cadenas en una misma fecha.
- [ ] Incluye fecha de actualización y nota metodológica visible.
- [ ] Carga en menos de 3 segundos con los datos del período.

### HU-09 — Informe automático

- [ ] Se genera un archivo Markdown con metodología, resultados, limitaciones y fuentes.
- [ ] Se produce en menos de 60 segundos con un comando.
- [ ] Incluye la fecha de generación y la versión del dataset.

### HU-10 — Calidad y trazabilidad

- [ ] Se descartan precios ≤ 0, EAN inválidos y duplicados por día/producto/cadena.
- [ ] Cada descarte se registra con motivo y cantidad.
- [ ] Los tests de integridad fallan si aparece un registro inválido.

---

## 3.5 Historias de usuario: formato

Todas las historias usan el formato:

> **Como** [rol], **quiero** [acción], **para** [beneficio].

Y se aceptan solo si cumplen la Definición de Preparado de `roles.md`.
