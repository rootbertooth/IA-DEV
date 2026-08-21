# Decisiones Arquitectónicas: Web Apps (Flask + React)

## 1. Flask como Backend
- **Contexto:** Proyectos web con requerimientos estándar.
- **Decisión:** Flask por su simplicidad y modularidad.
- **Alternativas:** Django, FastAPI.
- **Rationale:** Flask es ligero y permite añadir funcionalidades según necesidad.

## 2. React + Vite para Frontend
- **Contexto:** SPAs con interacción dinámica.
- **Decisión:** React con Vite por su velocidad de desarrollo y rendimiento.
- **Alternativas:** Vue, Angular, Create React App.
- **Rationale:** React es estándar en el ecosistema, Vite es más rápido que CRA.

## 3. Gunicorn para Producción
- **Contexto:** Servir aplicaciones Flask en producción.
- **Decisión:** Gunicorn con workers configurables.
- **Alternativas:** uWSGI, mod_wsgi.
- **Rationale:** Gunicorn es simple, fiable y ampliamente usado.

## 4. Separación Backend/Frontend
- **Contexto:** Desarrollo independiente y despliegues separados.
- **Decisión:** Backend y frontend en carpetas separadas.
- **Alternativas:** Monorepo con todo junto.
- **Rationale:** Facilita el mantenimiento y el despliegue por separado.
