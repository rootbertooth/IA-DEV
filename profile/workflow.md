# Flujo de Trabajo (Workflow)

Este documento describe el flujo de trabajo estándar para el desarrollo y operación de proyectos en tu ecosistema. Está basado en patrones observados en los proyectos auditados (VPS1, VPS2, VPS3) y refleja la evolución desde prototipos hasta sistemas de producción.

---

## 1. Ciclo de Vida del Desarrollo

### 1.1 Fase de Exploración / Prototipo
- **Objetivo:** Validar ideas rápidamente.
- **Características:**
  - Estructura mínima (backend y frontend en la misma raíz).
  - Uso de `venv` y `requirements.txt` para Python, `node_modules` y `package.json` para React.
  - Backups manuales (carpetas con timestamp, ej. `backup_20260731_111632`).
  - Despliegue manual: copia de archivos por SCP y reinicio de servicios (PM2, Gunicorn).
- **Ejemplos:** `benjamin`, `cocina-con-ia`, `ofericios` (VPS1).

### 1.2 Fase de Producto / Estabilización
- **Objetivo:** Convertir el prototipo en un producto usable.
- **Características:**
  - Separación clara de backend y frontend.
  - Gestión de variables de entorno con `.env` y `python-dotenv`.
  - Uso de Git para control de versiones (`.gitignore` excluye `.env`, `venv`, `node_modules`).
  - Backups estructurados con scripts y rotación.
  - Despliegue con scripts automatizados (SCP + SSH + reinicio).
- **Ejemplos:** `stock.respuestasinteligentes.com`, `ventas.respuestasinteligentes.com` (VPS2).

### 1.3 Fase de Producción / Escalabilidad
- **Objetivo:** Operar con alta disponibilidad, seguridad y trazabilidad.
- **Características:**
  - Contenerización con Docker y orquestación con Docker Compose.
  - Uso de proxy inverso (Traefik, Nginx).
  - Servicios gestionados con systemd.
  - Auditoría estructurada (UUID, timestamps, metadatos).
  - Tests automatizados (E2E, unitarios).
  - Documentación extensa (`README.md`, `AUTH.md`, `worklog.md`).
- **Ejemplos:** `/opt/API` (BabyWonder Motor), `/opt/nexus` (plataforma multi-tenant).

---

## 2. Entorno de Desarrollo

### 2.1 Configuración Local
- **Python:** Entorno virtual (`venv`) y dependencias en `requirements.txt`.
- **Node.js:** `npm install` para frontend y backend (si aplica).
- **Variables de entorno:** Archivo `.env` en la raíz del proyecto (o en `/backend`), nunca versionado. Se provee un `.env.example` como plantilla.

### 2.2 Herramientas Comunes
- **Editores/IDEs:** No especificado, pero se asume compatibilidad con VSCode, PyCharm, etc.
- **Linters:** ESLint para JavaScript/TypeScript, no se detectó linter específico para Python (pero se recomienda flake8 o pylint).
- **Gestión de paquetes:** `pip` para Python, `npm` o `yarn` para Node.js.

---

## 3. Control de Versiones (Git)

### 3.1 Uso de Git
- La mayoría de los proyectos maduros tienen un repositorio Git (`.git`).
- Archivos ignorados típicamente:
venv/
node_modules/
pycache/
.env
*.log
*.pyc

- No se ha detectado un flujo de branching definido (main/develop), pero se recomienda seguir Git Flow o GitHub Flow según la complejidad.

### 3.2 Commits
- Los mensajes de commit deben ser descriptivos. En `worklog.md` se registran cambios significativos con fecha y descripción, lo que sugiere que se prefiere un historial legible.

---

## 4. Pruebas

### 4.1 Tipos de Pruebas
- **Unitarias:** No se han detectado de forma extensiva, pero se recomienda implementar con `pytest` o `unittest`.
- **E2E:** Presentes en proyectos avanzados (ej. `e2e_test.py` en `/opt/API`).
- **Pruebas de fase:** En pipelines de procesamiento (ej. `test_fase8.py`).

### 4.2 Ejecución de Pruebas
- Las pruebas se ejecutan manualmente durante el desarrollo. No se ha detectado CI/CD automatizado (aunque algunos proyectos tienen scripts de deploy que podrían incluir pruebas).

---

## 5. Despliegue

### 5.1 Estrategias según Madurez

| Nivel | Método | Ejemplo |
|-------|--------|---------|
| **Prototipo** | Copia manual por SCP + reinicio de Gunicorn/PM2 | `benjamin`, `cocina-con-ia` |
| **Producto** | Script de deploy (SCP + SSH + PM2 restart) | `tarracokey-app` (script en `package.json`) |
| **Producción** | Docker Compose + systemd | `/opt/API` (babywonder-api.service), `/opt/nexus` |

### 5.2 Servidores y Puertos
- **Backend Flask:** Puerto 5002, 5005, 5006 (dependiendo del proyecto).
- **FastAPI:** Puerto 8000 (solo localhost, expuesto vía Nginx en 443).
- **Proxy inverso:** Nginx en VPS1 y VPS3, Traefik en VPS2 (`nexus`).
- **Gestión de procesos:** Gunicorn para Flask, Uvicorn para FastAPI, PM2 para Node.js, systemd para servicios críticos.

### 5.3 Despliegue con Docker
- **docker-compose.yml** define servicios (backend, frontend, DB, Redis, proxy).
- **Volúmenes:** Montajes para datos persistentes (ej. `/opt/nexus/backups`).
- **Redes:** Uso de redes internas (`nexus-net`) para comunicación entre servicios.

---

## 6. Backups y Recuperación

### 6.1 Estrategia de Backups
- **Backups manuales:** En fases tempranas, se copian carpetas enteras con timestamp.
- **Backups automatizados:** Scripts Bash (`backup_db.sh`, `nexus_backup.sh`) que generan copias diarias con fecha (ej. `20260821_020001`).
- **Backups de código:** Versionado en Git y backups de archivos críticos (`.env`, `config.py`) dentro de la estructura del proyecto.

### 6.2 Política de Retención
- No se ha definido una política explícita, pero se recomienda retener backups de al menos 7 días para producción.

---

## 7. Documentación

### 7.1 Archivos de Documentación Obligatorios
- **`README.md`**: Visión general, instalación, uso.
- **`worklog.md`**: Historial de cambios diarios con fecha y descripción.
- **`AUTH.md`**: Especificación de autenticación (si aplica).
- **`requirements.txt` / `package.json`**: Dependencias.

### 7.2 Actualización de Documentación
- Cada cambio significativo (nueva feature, bugfix, despliegue) debe reflejarse en `worklog.md` y, si es relevante, en `README.md`.

---

## 8. Flujo de Trabajo con Agentes de IA

### 8.1 Modos de Interacción
- **Plan:** El agente analiza, propone soluciones y hace preguntas. **NO** modifica archivos.
- **Build:** El agente ejecuta cambios aprobados. Puede modificar archivos, pero solo después de una aprobación explícita.

### 8.2 Protocolo
1. **Reconocimiento:** El agente examina el código y la infraestructura actual (usando los archivos `.ai/` como fuente de verdad).
2. **Planificación:** Propone un plan detallado en formato Markdown.
3. **Revisión:** Yo reviso el plan, lo apruebo, rechazo o pido ajustes.
4. **Ejecución:** Una vez aprobado, el agente implementa los cambios.
5. **Documentación:** Se actualizan los archivos relevantes (`.ai/project/current_state.md`, `worklog.md`).
6. **Commit:** Yo realizo el commit manualmente (si el proyecto usa Git), usando el mensaje sugerido por el agente.

### 8.3 Reglas de Seguridad
- Prohibido ejecutar comandos destructivos sin confirmación (`rm -rf`, `DROP TABLE`, etc.).
- Nunca se debe commitear código automáticamente.
- Las claves API y credenciales nunca se deben mostrar en texto plano.

---

## 9. Mejores Prácticas Recomendadas

Basado en la evolución observada, se recomienda:

- **Contenerización progresiva:** Migrar proyectos activos a Docker para entornos consistentes.
- **CI/CD:** Implementar pipelines (GitHub Actions, GitLab CI) para pruebas y despliegues automatizados.
- **Monitoreo:** Agregar healthchecks y métricas (Prometheus, Grafana) en proyectos críticos como `/opt/API`.
- **Política de backups:** Definir retención y almacenamiento externo para auditorías.
- **Centralización de logs:** Usar ELK o Loki para agregar logs de todos los proyectos.

---

*Este documento se actualiza conforme evolucionan los proyectos. La última revisión se basa en auditorías realizadas en agosto de 2026.*