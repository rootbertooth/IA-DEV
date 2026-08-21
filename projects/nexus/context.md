# Contexto del Proyecto: Nexus

## Propósito y Visión
Nexus es una plataforma multi-tenant contenerizada que aloja aplicaciones (tenants) de forma aislada. Cada tenant tiene su propio backend (Flask) y frontend (React), y todos comparten una infraestructura común (Traefik, PostgreSQL, Redis).

## Dominio y Alcance
- **Área:** Infraestructura SaaS.
- **Propósito:** Proveer una base para aplicaciones multi-tenant con aislamiento y escalabilidad.
- **Estructura:** Cada tenant en /opt/nexus/tenants/{tenant}/ con su propio docker-compose.yml y código.

## Actores
- **Superadmin:** Gestiona tenants, configuración global.
- **Tenant Admin:** Gestiona usuarios y datos de su tenant.
- **Usuarios:** Usuarios finales que acceden a las aplicaciones de los tenants.

## Entorno
- **Servidor:** VPS2 (204.168.228.41)
- **Estado:** ⏸️ Inactivo (no hay contenedores corriendo)
- **Acceso:** Traefik en puerto 8080 (proxy inverso) con detección automática de contenedores.
- **Base de datos:** PostgreSQL 16 (compartida o por tenant).
- **Caché/Colas:** Redis.

## Relaciones con Otros Proyectos
- **Babywonder (VPS3):** Independiente. Nexus no tiene relación con BabyWonder.
- **Bots (VPS3):** Independiente.

## Estado Actual
- **Desarrollo:** Estructura multi-tenant definida, pero inactiva.
- **Backups:** Automáticos diarios en /opt/nexus/backups/ con timestamp.
- **Próximos pasos:** Activar contenedores, añadir más tenants, implementar CI/CD, conectar lector de tags NFC
