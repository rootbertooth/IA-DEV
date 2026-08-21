# Arquitectura Técnica: Web Apps (Flask + React)

## Stack Tecnológico Común
| Componente | Tecnología | Versión |
|------------|------------|---------|
| **Backend** | Flask | 3.x |
| **Servidor** | Gunicorn | 25.x |
| **Frontend** | React + Vite | 18/5+ |
| **Base de Datos** | MySQL (PyMySQL) | - |
| **IA (algunos)** | OpenAI / Anthropic | - |

## Estructura de Directorios (Común)
/proyecto/
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ ├── .env
│ ├── blueprints/
│ └── models/
├── frontend/
│ ├── src/
│ ├── package.json
│ └── vite.config.js
└── backups/

text

## Despliegue
- **Gunicorn** con workers configurables.
- **PM2** (en algunos casos) para gestión de procesos.
- **Nginx** como proxy inverso.

## Seguridad
- .env para secretos.
- JWT para autenticación (en algunos).
