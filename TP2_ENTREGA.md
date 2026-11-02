# Trabajo Práctico II — Prácticas Profesionalizantes I

**Estudiante:** Nicolás Lucero
**Carrera:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial — INA
**Materia:** Prácticas Profesionalizantes I
**Docente:** MSc. Ángel Daniel Fuentes S.
**Fecha de entrega:** 26/10/2026

---

## Qué incluye esta entrega

| Parte | Entregable | Estado |
|---|---|---|
| Parte 1 | Repositorio con el proyecto `precios-supermercados-etl` | Listo para publicar |
| Parte 2 | `respuestas_scrum.md` con las 5 preguntas | Completo |

## Parte 1 — Proyecto práctico

- **Proyecto:** ETL de catálogos, precios y sucursales de supermercados argentinos a
  SQL Server, con comparador de canasta y registro de compras.
- **Nombre de repositorio sugerido:** `tp2-precios-supermercados-etl`
- **Enlace público:** `https://github.com/Nicaleluc/tp2-precios-supermercados-etl` (reemplazar al publicar)
- **Stack:** Python 3.12, SQL Server, `pyodbc`, `pytest`.
- **Documentación:** `README.md` (descripción, fuentes, arquitectura, instalación,
  uso, tests, solución de problemas y conclusiones personales).

> El ETL completo requiere una instancia de SQL Server y las credenciales en `.env`.
> Las pruebas unitarias (`test_normalizar.py`, `test_matching.py`) corren sin base de
> datos; la de integración se salta si no hay conexión.

## Parte 2 — Reflexión teórica

`respuestas_scrum.md` responde las cinco preguntas con un máximo de 10 líneas cada
una, apoyándose en la Guía de Scrum (Schwaber & Sutherland, 2020) y en las clases 8
a 10 de la materia.

## Checklist de la consigna

- [x] Repositorio con nombre descriptivo (definir al publicar).
- [x] Proyecto desarrollado con Python y datos.
- [x] `README.md` con descripción, tecnologías, instrucciones, ejemplos y
      conclusiones personales.
- [x] Al menos 3 commits significativos (secuencia sugerida abajo).
- [ ] Enlace público al repositorio (reemplazar `https://github.com/Nicaleluc/tp2-precios-supermercados-etl`).
- [x] `respuestas_scrum.md` con las 5 preguntas.

## Cómo publicar el repositorio (Git)

La entrega se preparó localmente. **No se hicieron commits ni push** desde el agente.
Crear un repositorio **nuevo** en GitHub (vacío, sin README) y ejecutar desde esta
carpeta:

```bash
git init
git branch -M main

# Commit 1 — base del proyecto
git add .env.template .gitattributes .gitignore LICENSE pyproject.toml README.md
git commit -m "chore: estructura base y documentacion del proyecto"

# Commit 2 — ETL
git add config/ etl/ sql/
git commit -m "feat: ETL de catalogos, precios y sucursales a SQL Server"

# Commit 3 — comparador, compras y automatización
git add cli/ *.bat
git commit -m "feat: comparador de canasta, registro de compras y automatizacion"

# Commit 4 — pruebas
git add tests/
git commit -m "test: pruebas de normalizacion, matching e integracion"

# Commit 5 — entrega del TP
git add respuestas_scrum.md TP2_ENTREGA.md
git commit -m "docs: respuestas de Scrum y portada del TP II"

# Publicación
git remote add origin https://github.com/<usuario>/tp2-precios-supermercados-etl.git
git push -u origin main
```

> Reemplazar `<usuario>` y `https://github.com/Nicaleluc/tp2-precios-supermercados-etl` por el usuario y la URL reales de GitHub.
> No subir `.env` (contiene credenciales); el repo incluye `.env.template`.

## Cómo se entrega

1. Crear el repositorio público nuevo en GitHub.
2. Subir el proyecto con la secuencia de commits de arriba.
3. Verificar que el README se vea completo y que `respuestas_scrum.md` esté en la raíz.
4. Entregar el **enlace público** en el aula virtual / formulario que indique el
   docente (es el entregable final de la consigna).
