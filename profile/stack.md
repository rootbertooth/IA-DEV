# Stack Tecnológico del Equipo (Stack)

Este documento describe el conjunto de tecnologías, frameworks, herramientas y servicios que componen el ecosistema de desarrollo. Está basado en la evidencia recopilada durante las auditorías de los VPS1, VPS2 y VPS3, y refleja tanto las tecnologías consolidadas como las emergentes.

---

## 1. Lenguajes Principales

| Lenguaje | Versión | Uso Principal |
|----------|---------|---------------|
| **Python** | 3.11+ | Lenguaje principal para backends, APIs, procesamiento de datos, pipelines de IA y sistemas de automatización. |
| **JavaScript/TypeScript** | ES2022+ / TS 5.x | Frontend con React y Vite. Backend con Node.js en proyectos específicos. |
| **PHP** | 8.x | Proyectos WordPress (blogs corporativos). |
| **Bash** | - | Scripts de automatización, backups y despliegues. |

---

## 2. Frameworks Web y APIs

### Python - Flask
- **Versión:** 3.x
- **Uso:** APIs REST, aplicaciones web ligeras, bots de Telegram y WhatsApp.
- **Proyectos:** VPS1 (`benjamin`, `cocina-con-ia`, `ofericios`, `way`), VPS2 (`sfs.respuestasinteligentes.com`, `nexus`), VPS3 (`respuestasinteligentes`, `tenant-bot`).
- **Patrón:** Blueprints para modularidad.
- **Servidor:** Gunicorn (WSGI).
- **Dependencias típicas:** `flask-cors`, `flask-sqlalchemy`, `python-dotenv`, `PyJWT`, `bcrypt`.

### Python - FastAPI
- **Versión:** 0.115+
- **Uso:** APIs asíncronas de alto rendimiento con validación automática (Pydantic).
- **Proyectos:** VPS3 (`/opt/API` - BabyWonder Motor).
- **Servidor:** Uvicorn (ASGI).
- **Dependencias típicas:** `pydantic-settings`, `python-multipart`, `httpx`.

### JavaScript - Node.js (Express)
- **Uso:** Backend para aplicaciones de negocio (stock, ventas, señales financieras).
- **Proyectos:** VPS2 (`gorillamansion.xyz`, `jfxsignals.com`, `stock.respuestasinteligentes.com`, `ventas.respuestasinteligentes.com`).
- **Dependencias típicas:** `express`, `cors`, `dotenv`, `jsonwebtoken`.

### PHP - WordPress
- **Uso:** Blogs corporativos.
- **Proyectos:** VPS2 (`blog.gorillamansion.xyz`, `blog.jfxsignals.com`).
- **Servidor:** PHP-FPM con Nginx.

---

## 3. Frontend

### React
- **Versión:** 18/19
- **Uso:** SPA con Vite y TypeScript.
- **Proyectos:** VPS1 (`benjamin`, `cocina-con-ia`, `ofericios`, `tarracokey-app`, `way`), VPS2 (`gorillamansion.xyz`, `jfxsignals.com`, `stock`, `ventas`, `nexus/farmacia1`), VPS3 (`tenant-bot`).
- **Librerías comunes:**
  - **Rutas:** `react-router-dom`
  - **Cliente HTTP:** `axios`
  - **Internacionalización:** `i18next`, `react-i18next`
  - **Estilos:** `tailwind-merge`, `tw-animate-css`, `class-variance-authority`
  - **UI:** `lucide-react`, `@radix-ui/*`, `@base-ui/react`
  - **Estado:** Context API (no se ha detectado Redux/Zustand)
  - **Formularios:** `react-hook-form`, `@hookform/resolvers`

### Vite
- **Versión:** 5+
- **Uso:** Bundler y servidor de desarrollo.
- **Proyectos:** Todos los proyectos React.

### TypeScript
- **Uso:** Tipado estático en proyectos modernos (los más recientes de VPS2 y VPS3).
- **Configuración:** `tsconfig.json` con `"strict": true`.

---

## 4. Bases de Datos

| Base de Datos | Uso | Proyectos |
|---------------|-----|-----------|
| **PostgreSQL 16** | Base de datos principal (relacional) | VPS2 (`nexus`), VPS3 (`/opt/API`) |
| **MySQL** | Base de datos legacy y proyectos antiguos | VPS1, VPS2 (`sfs`, `blogs`, `stock`, `ventas`) |
| **Redis** | Caché, colas de mensajería | VPS2 (`nexus`), VPS3 (potencial) |

### Librerías de Conexión
| Librería | Uso | Proyectos |
|----------|-----|-----------|
| **psycopg2-binary** | Conector PostgreSQL | VPS2 (`nexus`), VPS3 (`/opt/API`) |
| **PyMySQL** | Conector MySQL | VPS1, VPS2, VPS3 (`respuestasinteligentes`, `signalsbot`) |
| **mysql-connector-python (pooling)** | Pool de conexiones para alto rendimiento | VPS3 (`responsebot`) |
| **SQLAlchemy** | ORM para Flask (Flask-SQLAlchemy) | VPS1, VPS2 (`sfs`) |

---

## 5. Inteligencia Artificial y Machine Learning

### Modelos y APIs
| Modelo/API | Uso | Proyectos |
|------------|-----|-----------|
| **OpenAI GPT** (gpt-4o, text-embedding-3-small) | Generación de texto, embeddings, caché semántico | VPS1 (`cocina-con-ia`), VPS3 (`respuestasinteligentes`, `responsebot`) |
| **Anthropic Claude** (claude-sonnet-4-5) | Análisis técnico, generación de señales de trading | VPS1 (`cocina-con-ia`), VPS3 (`signalsbot`, `tenant-bot`) |
| **Google Gemini 3.5 Flash** | Detección de rostros en ecografías | VPS3 (`/opt/API` - BabyWonder) |
| **Ollama (local)** | Modelos open-source (qwen2.5-coder:7b) | VPS3 (`/opt/ai`) |
| **Replicate (GPT Image 2.0)** | Renderizado fotorrealista de ecografías | VPS3 (`/opt/API` - BabyWonder) |
| **Perplexity AI** | Búsqueda y generación (detectado en `tenant-bot`) | VPS3 (`tenant-bot`) |

### Librerías de IA/ML
| Librería | Uso | Proyectos |
|----------|-----|-----------|
| **openai** | Cliente para APIs de OpenAI | Todos los proyectos Python con IA |
| **anthropic** | Cliente para APIs de Anthropic | VPS1, VPS3 (`signalsbot`) |
| **sentence-transformers** | Embeddings y caché semántico (`paraphrase-multilingual-MiniLM-L12-v2`) | VPS3 (`responsebot`) |
| **MediaPipe** | Detección facial offline (478 landmarks) | VPS3 (`/opt/API` - BabyWonder) |
| **opencv-python-headless** | Procesamiento de imágenes (CLAHE, crop, máscaras) | VPS3 (`/opt/API`) |
| **pandas / pandas-ta** | Análisis técnico de datos financieros | VPS3 (`signalsbot`) |
| **Pillow** | Manipulación de imágenes | VPS3 (`/opt/API`) |
| **NumPy / SciPy** | Computación numérica | VPS3 (`/opt/API`) |

---

## 6. Procesamiento de Imagen y Video

| Componente | Uso | Proyectos |
|------------|-----|-----------|
| **OpenCV (headless)** | CLAHE, crop, máscaras, transformaciones geométricas | VPS3 (`/opt/API`) |
| **Pillow** | Lectura/escritura de imágenes, redimensionado | VPS3 (`/opt/API`) |
| **imageio / imageio-ffmpeg** | Soporte de video (generación de transiciones MP4) | VPS3 (`/opt/API`) |
| **MediaPipe** | Landmarks faciales para alineación anatómica | VPS3 (`/opt/API`) |

---

## 7. Infraestructura y Despliegue

### Contenerización
| Tecnología | Uso | Proyectos |
|------------|-----|-----------|
| **Docker** | Contenerización de servicios (backend, frontend, DB, Redis) | VPS2 (`nexus`), VPS3 (`/opt/ai`) |
| **Docker Compose** | Orquestación multi-servicio | VPS2 (`nexus`), VPS3 (`/opt/ai`) |
| **Traefik** | Proxy inverso con detección automática de contenedores | VPS2 (`nexus`) |

### Gestión de Procesos
| Tecnología | Uso | Proyectos |
|------------|-----|-----------|
| **Gunicorn** | Servidor WSGI para Flask | VPS1, VPS2, VPS3 (`respuestasinteligentes`) |
| **Uvicorn** | Servidor ASGI para FastAPI | VPS3 (`/opt/API`) |
| **PM2** | Gestor de procesos para Node.js | VPS2 (`tarracokey-app`, `stock`, `ventas`) |
| **systemd** | Servicios del sistema (babywonder-api.service) | VPS3 (`/opt/API`) |

### Proxy y Web Server
| Tecnología | Uso | Proyectos |
|------------|-----|-----------|
| **Nginx** | Servidor web, TLS termination, proxy inverso | VPS1, VPS2, VPS3 |

---

## 8. Automatización y Backups

### Backups
| Tecnología | Uso | Proyectos |
|------------|-----|-----------|
| **Scripts Bash** | Backups automáticos de bases de datos y código | VPS2 (`nexus`), VPS3 (`respuestasinteligentes`) |
| **Backups con timestamp** | Estructura de carpetas con fecha/hora | VPS2 (`nexus`), VPS3 (`respuestasinteligentes`) |
| **Rotación de backups** | Política de retención (diaria) | VPS2 (`nexus`) |

### CI/CD (Evidencia detectada)
| Tecnología | Uso | Proyectos |
|------------|-----|-----------|
| **Scripts manuales** | SCP + SSH + PM2 para despliegues | VPS2 (`tarracokey-app`) |
| **Worklog.md** | Historial de cambios documentado | VPS3 (`respuestasinteligentes`, `/opt/API`) |

---

## 9. Seguridad y Autenticación

### Autenticación
| Tecnología | Uso | Proyectos |
|------------|-----|-----------|
| **JWT (PyJWT / python-jose)** | Autenticación sin estado | VPS1, VPS2, VPS3 (`tenant-bot`, `/opt/API`) |
| **JWT RS256** | Firma asimétrica con clave privada local | VPS3 (`/opt/API` - BabyWonder) |
| **Firebase Service Account** | Verificación de tokens | VPS3 (`/opt/API`) |
| **bcrypt** | Hash de contraseñas | VPS1, VPS2, VPS3 (`tenant-bot`) |

### Rate Limiting y Protección
| Tecnología | Uso | Proyectos |
|------------|-----|-----------|
| **Tenacity** | Reintentos y backoff para APIs externas | VPS3 (`responsebot`) |
| **Rate limiting custom** | Protección contra flood en Telegram | VPS3 (`responsebot`) |
| **CORS** | Restricción de orígenes en APIs | VPS1, VPS2, VPS3 |

---

## 10. Integraciones con Servicios Externos

| Servicio | Uso | Proyectos |
|----------|-----|-----------|
| **Binance API** | Datos de mercado (precios, volumen, order book) | VPS3 (`signalsbot`) |
| **CoinMarketCap API** | Precios de criptomonedas | VPS3 (`responsebot`) |
| **Meta Cloud API** | WhatsApp Business | VPS3 (`respuestasinteligentes`) |
| **Twilio API** | WhatsApp (alternativa) | VPS3 (`respuestasinteligentes`) |
| **Resend API** | Email | VPS3 (`respuestasinteligentes`) |
| **Supabase** | Backend-as-a-service (autenticación, DB) | VPS2 (`gorillamansion.xyz`, `stock`, `ventas`) |
| **Firebase** | Autenticación y notificaciones | VPS3 (`/opt/API`, `respuestasinteligentes`) |
| **Stripe** | Pagos (detectado en `ofericios`) | VPS1 (`ofericios`) |

---

## 11. Herramientas de Desarrollo

| Herramienta | Uso | Proyectos |
|-------------|-----|-----------|
| **Git** | Control de versiones | Proyectos maduros |
| **venv** | Entornos virtuales Python | Todos los proyectos Python |
| **pip** | Gestión de dependencias Python | Todos los proyectos Python |
| **npm / yarn** | Gestión de dependencias Node.js | Todos los proyectos frontend |
| **ESLint** | Linting para JavaScript/TypeScript | Proyectos frontend |
| **Prettier** | Formateo de código (detectado en `tarracokey-app`) | VPS2 (`tarracokey-app`) |
| **Oxlint** | Linter alternativo (detectado en `ventas`) | VPS2 (`ventas`) |

---

## 12. Logs y Auditoría

| Componente | Uso | Proyectos |
|------------|-----|-----------|
| **Logging estándar (Python)** | Registro de eventos | Todos los proyectos Python |
| **Auditoría estructurada** | UUID + timestamp + metadatos | VPS3 (`/opt/API`) |
| **Rotación de logs** | `RotatingFileHandler` (recomendado) | - |

---

## 13. Frameworks y Librerías No Detectadas (pero compatibles)

- **LangChain / LlamaIndex** (no detectados, pero podrían añadirse para orquestación avanzada).
- **Celery / RQ** (no detectados, pero se recomiendan para tareas asíncronas pesadas).
- **Prometheus / Grafana** (no detectados, pero se sugieren para monitoreo).

---

*Este documento se actualiza a medida que se incorporan nuevas tecnologías. Revisión periódica recomendada.*
