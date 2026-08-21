# Decisiones Arquitectónicas: Nexus

## 1. Docker Compose para Orquestación
- **Contexto:** Necesidad de desplegar múltiples servicios interconectados.
- **Decisión:** Usar Docker Compose para definir servicios compartidos (Traefik, PostgreSQL, Redis).
- **Alternativas:** Kubernetes, Swarm.
- **Rationale:** Docker Compose es más ligero y fácil de gestionar para un ecosistema pequeño/mediano.

## 2. Traefik como Proxy Inverso
- **Contexto:** Enrutamiento automático de tráfico a los tenants.
- **Decisión:** Usar Traefik con detección automática de contenedores via Docker socket.
- **Alternativas:** Nginx con configuración manual.
- **Rationale:** Traefik se integra nativamente con Docker y permite enrutamiento dinámico sin reinicios.

## 3. PostgreSQL como Base de Datos Compartida
- **Contexto:** Almacenamiento de datos de múltiples tenants.
- **Decisión:** Usar PostgreSQL con esquemas separados por tenant (o bases de datos separadas).
- **Alternativas:** MySQL, MongoDB.
- **Rationale:** PostgreSQL es robusto, soporta JSON, y tiene buen rendimiento para aplicaciones SaaS.

## 4. Redis para Caché y Colas
- **Contexto:** Necesidad de caché y mensajería entre servicios.
- **Decisión:** Usar Redis para caché y potencialmente para colas (RQ/Celery).
- **Alternativas:** Memcached, RabbitMQ.
- **Rationale:** Redis es versátil (caché + colas) y fácil de configurar.

## 5. Backups Automatizados con Scripts Bash
- **Contexto:** Garantizar la integridad de los datos de los tenants.
- **Decisión:** Scripts Bash que realizan dumps de PostgreSQL diarios a las 02:00.
- **Alternativas:** Herramientas de backup de PostgreSQL (pg_dumpall, etc.).
- **Rationale:** Los scripts son simples, portables y fáciles de modificar.

## 6. Aislamiento por Tenant (Carpetas Separadas)
- **Contexto:** Cada tenant debe tener su propio código y configuración.
- **Decisión:** Cada tenant tiene su propia carpeta en /opt/nexus/tenants/{tenant}/.
- **Alternativas:** Un solo código base con variables de entorno por tenant.
- **Rationale:** Aislamiento total, permite diferentes versiones por tenant y facilita la gestión.

## 7. Uso de Variables de Entorno (.env) para Configuración
- **Contexto:** Separación de configuración del código.
- **Decisión:** Usar .env en la raíz para variables globales (DB, Redis, puertos).
- **Alternativas:** Archivos de configuración en YAML/JSON.
- **Rationale:** .env es estándar en Docker y fácil de usar con python-dotenv.
