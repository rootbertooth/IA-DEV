# Arquitectura Técnica: ¿Qué Cocino Hoy? (QCH)

## Stack Tecnológico
| Componente | Tecnología | Versión |
|------------|------------|---------|
| **Backend** | Flask | 3.1.3 |
| **Servidor** | Gunicorn | 25.1.0 |
| **Frontend** | React + Vite | 18/5+ |
| **Base de Datos** | MySQL (PyMySQL) | - |
| **IA Principal** | Anthropic Claude | claude-sonnet-4-5 |
| **Embeddings** | OpenAI | text-embedding-3-small |
| **Cache** | MySQL (BLOB) + similitud coseno | - |

## Estructura de Directorios
/var/www/cocina-con-ia/
├── backend/
│ ├── app.py # Punto de entrada Flask
│ ├── config.py # Configuración
│ ├── database.py # Conexión MySQL
│ ├── blueprints/ # Módulos Flask
│ │ ├── auth.py # Autenticación JWT
│ │ ├── chat.py # Conversaciones con IA
│ │ ├── menu.py # Generación de menús
│ │ ├── recetas.py # Lógica de recetas + RAG
│ │ └── ...
│ ├── prompts/ # Archivos de prompt externalizados
│ │ ├── base.txt
│ │ ├── modo_apetece.txt
│ │ ├── modo_coccion.txt
│ │ ├── modo_clasica.txt
│ │ ├── modo_ingredientes.txt
│ │ ├── modo_menu.txt
│ │ ├── modo_mundo.txt
│ │ ├── modo_rapido.txt
│ │ ├── modo_tiempo.txt
│ │ └── modo_vision.txt
│ └── requirements.txt
├── frontend/
│ ├── src/
│ ├── package.json
│ └── vite.config.js
└── backups/ # Backups de código y config

text

## Lógica de IA (RAG + Caché Semántico)
1. **Embeddings:** 	ext-embedding-3-small de OpenAI.
2. **Almacenamiento:** BLOB en MySQL (tabla ecetas_cache).
3. **Búsqueda:** Similitud coseno con umbral 0.85.
4. **Caché:** Si la consulta es similar a una ya procesada, se reutiliza la respuesta.

## Prompts Externalizados
- Cada modo tiene su propio archivo .txt en ackend/prompts/.
- Los prompts incluyen:
  - **Role-Playing:** "Eres Miga, asistente culinaria..."
  - **Few-shot:** Ejemplos dentro del prompt.
  - **JSON Mode:** Salida estructurada para integración con frontend.
  - **Variables dinámicas:** {titulo_receta}, {paso_actual}, etc.

## Autenticación
- **JWT** con PyJWT.
- **Middleware:** equire_auth, check_acceso_soft, consumir_credito.

## Seguridad
- .env para claves API (OpenAI, Anthropic, DB).
- CORS restringido.
