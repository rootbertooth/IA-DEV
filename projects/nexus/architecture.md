# Arquitectura Técnica: Nexus

## Stack Tecnológico
| Componente | Tecnología | Versión |
|------------|------------|---------|
| **Orquestación** | Docker Compose | - |
| **Proxy Inverso** | Traefik | latest |
| **Base de Datos** | PostgreSQL | 16-alpine |
| **Caché/Colas** | Redis | - |
| **Backend** | Flask + Python | 3.11 |
| **Frontend** | React + Node.js | 18 |

## Estructura de Directorios
/opt/nexus/
├── docker-compose.yml # Servicios compartidos (Traefik, PostgreSQL, Redis)
├── .env # Variables globales (DB, Redis, puertos)
├── config/ # Configuración de Traefik (traefik.yml, dynamic.yml)
├── logs/ # Logs centralizados
├── scripts/ # Scripts de backup y mantenimiento
├── backups/ # Backups diarios (timestamp)
│ └── {YYYYMMDD_020001}/ # Backup de cada día
└── tenants/ # Cada tenant es una carpeta
└── farmacia1/ # Ejemplo: farmacia1
├── backend/
│ ├── Dockerfile
│ ├── requirements.txt
│ ├── app.py
│ ├── auth.py
│ └── i18n.py
├── frontend/
│ ├── Dockerfile (multi-stage)
│ ├── package.json
│ └── src/
└── docker-compose.yml (opcional, si tenant tiene servicios propios)

text

## Servicios Compartidos (docker-compose.yml)
| Servicio | Imagen | Puerto | Propósito |
|----------|--------|--------|-----------|
| **Traefik** | traefik:latest | 8080 (HTTP) | Proxy inverso con detección de contenedores |
| **PostgreSQL** | postgres:16-alpine | 5432 | Base de datos principal |
| **Redis** | redis:alpine | 6379 | Caché y colas |

## Traefik Configuración
- **Configuración estática:** config/traefik.yml (puertos, proveedores Docker).
- **Configuración dinámica:** config/traefik-dynamic.yml (middlewares, routers).
- **Detección de contenedores:** Traefik escucha el socket Docker y enruta automáticamente los servicios.

## Backend (Flask por Tenant)
- **Dockerfile:** FROM python:3.11-slim.
- **Puerto:** 8000 (por defecto, expuesto al proxy).
- **Variables de entorno:** Inyectadas desde /opt/nexus/.env.
- **Volumen:** Montaje de /opt/nexus/backups en /backups para escribir backups.

## Frontend (React por Tenant)
- **Multi-stage Dockerfile:**
  1. 
ode:18-alpine para build de React.
  2. 
ginx:alpine para servir los archivos estáticos.
- **Puerto:** 3000.

## Backups Automatizados
- **Frecuencia:** Diaria a las 02:00.
- **Script:** /opt/nexus/scripts/backup_db.sh (dumps PostgreSQL).
- **Rotación:** Estructura de carpetas con timestamp.

## Redes
- **nexus-net:** Red interna para comunicación entre servicios y tenants.
