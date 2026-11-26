# 5. Informe de ética y responsabilidad profesional

**Proyecto:** Observatorio de Precios de la Canasta Básica (OPCB)
**Autor:** Nicolás Lucero
**Fecha:** 16/11/2026
**Extensión:** informe breve (≈ 900 palabras)

---

## 5.1 Por qué la ética es un requisito técnico y no un adorno

Un observatorio de precios parece una iniciativa de bajo riesgo: no diagnostica enfermedades ni
decide quién recibe un crédito. Sin embargo, publica afirmaciones sobre terceros —las cadenas— y
sobre el bolsillo de las personas. Un error de matching que atribuya el precio de un producto a la
cadena equivocada no es un bug cosmético: es una afirmación falsa con impacto reputacional y, en
Argentina, potencialmente alcanzada por el régimen de defensa del consumidor (Ley N.º 24.240). La
ética del proyecto se juega en tres decisiones concretas: qué se mide, cómo se mide y qué se dice
sobre lo medido.

## 5.2 Principios aplicados

| Principio | Traducción operativa en el OPCB |
|---|---|
| **Exactitud y no daño** | ningún precio se publica sin trazabilidad de origen; un dato dudoso se excluye, no se corrige a mano |
| **Transparencia** | metodología, fórmula de variación, criterio de canasta y limitaciones visibles en el dashboard y el informe |
| **Equidad** | la canasta no se limita a productos de una góndola ni a un barrio; se documenta su composición y a quién representa |
| **Privacidad** | el MVP no recolecta datos personales; si se incorpora registro de compras, se aplica minimización y Ley N.º 25.326 |
| **Responsabilidad** | cada versión del dataset y del informe queda identificada; hay un responsable explícito |
| **Humildad epistémica** | el sistema describe precios observados; no predice ni atribuye causas |

## 5.3 Riesgos identificados y mitigación

### Riesgo 1 — Sesgo de representatividad de la canasta

Toda canasta es una decisión política y estadística. Si se eligen 30 productos de marcas líderes y
de un solo tipo de comercio, el resultado sobrerrepresenta a un hogar urbano de ingresos medios y
excluye dietas regionales, productos sin TACC o alternativas de menor precio. Presentar ese número
como "el costo de la canasta" para toda la población sería una conclusión inválida.

**Mitigación:** publicar la composición exacta de la canasta, explicar el criterio de selección,
incluir la cobertura (cadenas y sucursales relevadas) y declarar en el informe a quién representa y
a quién no. El objetivo no es eliminar el sesgo —es inevitable— sino hacerlo visible y acotado.

### Riesgo 2 — Error de identificación y daño reputacional a terceros

El matching entre cadenas es la operación más frágil: dos productos con nombres parecidos pueden
tener unidades distintas (por ejemplo, 500 g contra 1 kg) y generar una diferencia de precio falsa.
Atribuir ese error a una cadena es una acusación infundada.

**Mitigación:** priorizar el EAN como llave, usar similitud de texto solo como respaldo, validar la
unidad antes de comparar y mantener un umbral de confianza. Los pares dudosos se excluyen y se
informan como "no comparables". Antes de publicar, se revisa manualmente la canasta completa. La
regla es explícita: **es preferible un dato faltante a un dato incorrecto**.

### Riesgo 3 — Condiciones de uso y extracción de datos

Los catálogos son públicos, pero público no significa libre de condiciones. Un relevamiento
automatizado intensivo puede violar términos de uso, sobrecargar servidores o quedar fuera de lo
que cada sitio autoriza.

**Mitigación:** bajo volumen de consultas, respeto de `robots.txt` y de los términos de cada sitio,
identificación del cliente y atribución de la fuente. Si una cadena no autoriza el relevamiento, se
la excluye y se documenta el motivo; no se disfraza la extracción.

### Riesgo 4 — Sobrepromesa y opacidad

Un tablero con líneas y porcentajes comunica certeza aunque el dato sea parcial. El riesgo aumenta
si se agregan predicciones o se infieren causas ("los precios suben por X") sin evidencia. La
literatura sobre modelos advierte que la autoridad visual de una métrica puede desactivar el
pensamiento crítico del usuario (Saltelli et al., 2020).

**Mitigación:** el dashboard muestra fecha de actualización, cantidad de productos relevados y nota
metodológica. El informe separa resultados de interpretación y no afirma causalidad. No se incluye
predicción en el MVP; si se incorpora más adelante, deberá declarar error y alcance.

### Riesgo 5 — Privacidad en la extensión futura

El MVP no procesa datos personales. Una versión con registro de compras sí lo haría: ticket, medio
de pago, ubicación y hábitos permiten identificar a una persona y perfilan su consumo. Ese
escenario exige consentimiento informado, minimización, plazo de conservación y seguridad, conforme
a la Ley N.º 25.326.

**Mitigación:** el diseño actual mantiene separado el dato de precios (público) del dato de compras
(personal). Cualquier extensión requiere una evaluación de impacto antes de implementarse.

## 5.4 Marco normativo de referencia

- **Ley N.º 25.326 (2000)** de Protección de los Datos Personales: aplica a cualquier dato que
  identifique o permita identificar personas.
- **Ley N.º 24.240 (1993)** de Defensa del Consumidor: la información difundida debe ser veraz y
  no inducir a error.
- **Reglamento (UE) 2024/1689** (Ley de IA): se toma como referencia de transparencia y
  clasificación de riesgo, aunque su aplicación territorial es europea.

El marco legal fija el mínimo; el criterio profesional decide el resto. Una publicación puede ser
legal y aun así ser engañosa.

## 5.5 Compromiso profesional

El OPCB adopta cinco reglas verificables:

1. **Trazabilidad:** todo precio publicado tiene fecha, cadena, sucursal y origen.
2. **Revisión antes de publicar:** ninguna conclusión sale sin revisar la canasta completa.
3. **Limitaciones visibles:** el informe declara cobertura, sesgos y productos no comparables.
4. **Sin causalidad sin evidencia:** se describe la variación, no se explica por causas no medidas.
5. **Corrección pública:** si se detecta un error, se corrige la serie y se deja registro del cambio.

En mi trabajo como administrador de bases de datos sostengo bases de producción con información
fiscal de terceros; ahí aprendí que la integridad no es un valor abstracto, es una condición de
operación. Este proyecto aplica el mismo criterio a un dato público: si no puedo explicar de dónde
sale un número, no lo publico.

---

## Referencias

Barocas, S., & Selbst, A. D. (2016). Big data's disparate impact. *California Law Review, 104*(3),
671–732.

Green, B. (2022). The flaws of policies requiring human oversight of government algorithms.
*Computer Law & Security Review, 45*, 105681. https://doi.org/10.1016/j.clsr.2022.105681

Ley N.º 24.240. (1993). *Defensa del consumidor*. Boletín Oficial de la República Argentina.
https://www.argentina.gob.ar/normativa/nacional/ley-24240-6383/texto

Ley N.º 25.326. (2000). *Protección de los datos personales*. Boletín Oficial de la República
Argentina. https://www.argentina.gob.ar/normativa/nacional/ley-25326-64629/texto

Saltelli, A., Bammer, G., Bruno, I., Charters, E., Di Fiore, M., Didier, E., Espeland, W. N., Kay,
J., Lo Piano, S., Mayo, D., Pielke, R., Portaluri, T., Porter, T. M., Puy, A., Rafols, I., Ravetz,
J. R., Reinert, E., Sarewitz, D., Stark, P. B., … Vineis, P. (2020). Five ways to ensure that
models serve society: A manifesto. *Nature, 582*(7813), 482–484.
https://doi.org/10.1038/d41586-020-01812-9

Unión Europea. (2024). Reglamento (UE) 2024/1689 por el que se establecen normas armonizadas en
materia de inteligencia artificial. *Diario Oficial de la Unión Europea*.
https://eur-lex.europa.eu/eli/reg/2024/1689/oj
