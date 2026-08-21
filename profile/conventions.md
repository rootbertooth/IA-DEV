# Convenciones de Código y Proyecto (Conventions)

Este documento establece las reglas de estilo, estructura y organización que rigen todos los proyectos en tu ecosistema. Está basado en patrones observados en las auditorías (VPS1, VPS2, VPS3) y refleja tanto las prácticas consolidadas como las emergentes.

---

## 1. Estructura de Directorios

### 1.1 Proyecto Estándar (Python + React)
/proyecto/
├── backend/ # Código Python (Flask/FastAPI)
│ ├── app.py # Punto de entrada principal
│ ├── config.py # Configuración (clases o pydantic-settings)
│ ├── requirements.txt # Dependencias Python
│ ├── .env # Variables de entorno (NUNCA versionado)
│ ├── .env.example # Plantilla de variables (versionado)
│ ├── blueprints/ # Módulos Flask (blueprints)
│ │ ├── auth.py
│ │ ├── chat.py
│ │ └── ...
│ ├── models/ # Modelos de datos (SQLAlchemy, etc.)
│ ├── migrations/ # Migraciones de base de datos
│ ├── utils/ # Utilidades compartidas
│ ├── tests/ # Pruebas unitarias
│ └── venv/ # Entorno virtual (ignorado)
├── frontend/ # Código JavaScript/TypeScript (React)
│ ├── src/
│ │ ├── components/ # Componentes reutilizables
│ │ ├── pages/ # Vistas/páginas
│ │ ├── hooks/ # Hooks personalizados
│ │ ├── context/ # Context Providers
│ │ ├── lib/ # Utilidades y configuraciones
│ │ ├── assets/ # Imágenes, estilos, etc.
│ │ └── i18n/ # Internacionalización (si aplica)
│ ├── public/ # Archivos estáticos
│ ├── package.json # Dependencias Node.js
│ ├── vite.config.js # Configuración de Vite
│ └── node_modules/ # Dependencias (ignorado)
├── backups/ # Backups manuales o automatizados
├── docker-compose.yml # Orquestación (si aplica)
├── README.md # Documentación general
├── worklog.md # Historial de cambios diario
└── .gitignore # Archivos ignorados por Git

### 1.2 Proyecto Multi-Tenant (Nexus)
/opt/nexus/
├── docker-compose.yml # Servicios compartidos (Traefik, DB, Redis)
├── .env # Variables globales
├── config/ # Configuración de Traefik
├── logs/ # Logs centralizados
├── scripts/ # Scripts de backup y mantenimiento
├── backups/ # Backups diarios (timestamp)
├── tenants/ # Cada tenant es una carpeta
│ └── {tenant}/
│ ├── backend/
│ │ ├── Dockerfile
│ │ ├── requirements.txt
│ │ └── app.py
│ ├── frontend/
│ │ ├── Dockerfile (multi-stage)
│ │ ├── package.json
│ │ └── src/
│ └── docker-compose.yml (opcional)
└── worklog.md

---

## 2. Nomenclatura

### 2.1 Python
- **Archivos:** `snake_case.py` (ej. `auth.py`, `db_utils.py`).
- **Clases:** `PascalCase` (ej. `UserModel`, `SignalAnalyzer`).
- **Funciones y variables:** `snake_case` (ej. `get_user_by_id`, `total_signals`).
- **Constantes:** `UPPER_CASE` (ej. `MAX_RETRIES`, `DEFAULT_TIMEOUT`).
- **Blueprints de Flask:** Se nombran con sufijo `_bp` (ej. `auth_bp`, `chat_bp`).

### 2.2 JavaScript/TypeScript
- **Archivos:** `camelCase.js` o `PascalCase.jsx` para componentes (ej. `NavBar.jsx`, `useAuth.js`).
- **Componentes React:** `PascalCase` (ej. `Dashboard`, `SignalCard`).
- **Funciones y variables:** `camelCase` (ej. `fetchSignals`, `userData`).
- **Constantes:** `UPPER_CASE` o `camelCase` según contexto (ej. `API_BASE_URL`).

### 2.3 Bases de Datos
- **Tablas:** `snake_case` en plural (ej. `signals`, `clientes`, `conversaciones`).
- **Columnas:** `snake_case` (ej. `user_id`, `created_at`, `signal_type`).
- **Claves primarias:** `id` (autoincremental o UUID).
- **Claves foráneas:** `{tabla}_id` (ej. `client_id`, `tenant_id`).

---

## 3. Estilo de Código

### 3.1 Python (PEP 8)
- **Indentación:** 4 espacios (no tabs).
- **Líneas:** Máximo 79 caracteres (recomendado), 99 aceptable.
- **Imports:** Orden: estándar → terceros → locales. Agrupar por categoría.
- **Docstrings:** Usar triple comillas dobles (`"""`) para funciones y clases.
- **Tipado:** Anotaciones de tipo recomendadas (Type Hints).
- **Formateo:** Se recomienda `black` o `autopep8` para consistencia.

### 3.2 JavaScript/TypeScript (ESLint)
- **Indentación:** 2 espacios.
- **Comillas:** Usar comillas simples (`'`) para strings, dobles (`"`) para JSX.
- **Punto y coma:** Obligatorio al final de cada declaración.
- **Arrow functions:** Preferir `const fn = () => {}` sobre `function`.
- **Tipado:** TypeScript con tipos estrictos (`strict: true` en `tsconfig.json`).

---

## 4. Gestión de Dependencias

### 4.1 Python
- **requirements.txt:** Lista todas las dependencias con versiones fijas (ej. `Flask==3.1.3`).
- **Separación:** Usar `requirements-dev.txt` para dependencias de desarrollo (testing, linting).
- **Instalación:** `pip install -r requirements.txt` dentro del entorno virtual.

### 4.2 Node.js
- **package.json:** Incluir `name`, `version`, `scripts`, `dependencies`, `devDependencies`.
- **Lockfile:** Siempre versionar `package-lock.json` o `yarn.lock`.
- **Scripts comunes:**
  ```json
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "lint": "eslint ."
  }
5. Variables de Entorno
5.1 Gestión
Archivo .env: Siempre en la raíz del backend (o en la raíz del proyecto para Node.js).

NUNCA versionado: Incluido en .gitignore.

Plantilla: Proveer un archivo .env.example con todas las variables necesarias (valores ficticios o vacíos).

5.2 Variables Comunes
bash
# Base de datos
DB_HOST=localhost
DB_USER=user
DB_PASSWORD=password
DB_NAME=database

# API Keys (ejemplos)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GEMINI_API_KEY=AIza...

# Configuración de app
DEBUG=True
JWT_SECRET_KEY=super_secret_key
PORT=5000
6. Backups y Versionado
6.1 Backups de Código
Manuales: Crear carpetas con timestamp backup_YYYYMMDD_HHMMSS antes de cambios grandes.

Automatizados: Usar scripts en /scripts/ que compriman y roten backups (ej. backup_db.sh, nexus_backup.sh).

6.2 Backups de Base de Datos
Dumps SQL: Almacenar en backups/sql/ con formato {nombre}_YYYYMMDD.sql.

Frecuencia: Diaria en producción (vía cron o systemd timer).

7. Logs y Auditoría
7.1 Logs de Aplicación
Ubicación: Carpeta logs/ en la raíz del proyecto.

Formato: Incluir timestamp, nivel (INFO, WARNING, ERROR), mensaje.

Rotación: Configurar rotación diaria o por tamaño (usando RotatingFileHandler en Python).

7.2 Auditoría de Ejecuciones (Proyectos Avanzados)
Estructura: audit/{timestamp}_{uuid}/

Contenido: Inputs, outputs, metadatos en JSON, imágenes intermedias.

Propósito: Trazabilidad y depuración.

8. Control de Versiones (Git)
8.1 Archivos Ignorados (.gitignore)

# Python
venv/
__pycache__/
*.pyc
*.pyo
.env

# Node.js
node_modules/
dist/
build/

# Logs
*.log
logs/

# Backups locales
backups/
*.bak

# IDE
.vscode/
.idea/
*.swp
8.2 Mensajes de Commit
Formato: [tipo] descripción breve

Tipos: feat, fix, docs, style, refactor, test, chore.

Ejemplo: feat: add Gemini detection to pipeline

Cuerpo: Opcional, para explicar el "por qué".

9. Pruebas
9.1 Estructura de Tests
Unitarios: tests/ con archivos test_*.py (Python) o *.test.js (Node.js).

E2E: e2e_test.py o cypress/ para tests completos de flujo.

Datos: Usar fixtures o archivos de ejemplo en input/.

9.2 Ejecución
Python: pytest o python -m unittest

Node.js: npm test

10. Documentación
10.1 Archivos Obligatorios por Proyecto
README.md: Visión general, instalación, uso.

worklog.md: Historial de cambios diario (fecha, descripción, autor).

AUTH.md: Especificación de autenticación (si aplica).

requirements.txt / package.json: Dependencias.

10.2 Formato de worklog.md
markdown
# Worklog - [Nombre del Proyecto]

## 2026-08-22
- Añadida detección dual (Gemini + MediaPipe).
- Corregido bug en crop adaptativo.
- Actualizada documentación de autenticación.

## 2026-08-21
- Implementada fase 8 (enhance).
- Creado script de backup automático.
11. Despliegue
11.1 Entornos
Desarrollo: Local o VPS de pruebas. Variables DEBUG=True.

Staging: Servidor de validación (cuando exista).

Producción: VPS final. DEBUG=False, logs a archivo.

11.2 Gestión de Procesos
Flask: gunicorn --workers 1 --bind 127.0.0.1:5000 app:app

FastAPI: uvicorn app.main:app --host 127.0.0.1 --port 8000

Node.js: pm2 start npm --name "app" -- start

11.3 Proxy Inverso
Nginx: Configuración en /etc/nginx/sites-available/.

Traefik: Configuración dinámica via Docker labels.

12. Seguridad
12.1 Principios
Nunca versionar secretos (claves API, contraseñas, tokens).

Usar variables de entorno para toda configuración sensible.

Implementar autenticación (JWT, OAuth2) en todas las APIs expuestas.

Validar y sanitizar todos los inputs de usuario.

Habilitar CORS solo para orígenes autorizados.

12.2 Rate Limiting
Implementar en APIs con alto tráfico (ej. /opt/API).

Usar herramientas como flask-limiter o nginx limit_req.

Este documento se actualiza conforme evolucionan las prácticas. Versión basada en auditorías de agosto 2026.