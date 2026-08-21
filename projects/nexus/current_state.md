# Estado Actual: Nexus

## Información General
| Métrica | Valor |
|---------|-------|
| **Estado** | ⏸️ Inactivo (contenedores no corriendo) |
| **Última modificación** | 21 Aug 2026 |
| **Tamaño total** | 3.1M |
| **Propietario** | root:rootbert |

## Directorios y Archivos Clave
| Archivo/Directorio | Tamaño | Propósito |
|--------------------|--------|-----------|
| ackups/ | 9 directorios | Backups diarios (13-21 Aug) |
| ackup_audit_hardening/ | 7 directorios | Backups de auditoría |
| config/ | 2 archivos | Configuración Traefik |
| data/postgres/ | - | Datos persistentes PostgreSQL |
| data/redis/ | - | Datos persistentes Redis |
| logs/ | - | Logs vacíos |
| 	enants/farmacia1/ | - | Un único tenant de ejemplo |
| .env | 739 bytes | Variables globales |
| docker-compose.yml | 1.3K | Servicios compartidos |
| worklog.md | 97K | Historial de desarrollo |

## Backups Realizados
| Fecha | Directorio | Tamaño |
|-------|------------|--------|
| 2026-08-13 | ackups/20260813_020001/ | - |
| 2026-08-14 | ackups/20260814_020001/ | - |
| ... | ... | ... |
| 2026-08-21 | ackups/20260821_020001/ | - |

## Procesos y Puertos
| Puerto | Estado | Servicio |
|--------|--------|----------|
| 8080 | En escucha | Traefik (esperando contenedores) |
| 5432 | No escucha | PostgreSQL (inactivo) |
| 6379 | No escucha | Redis (inactivo) |

## Problemas Conocidos
- Contenedores no están corriendo (inactivo).
- Sin CI/CD configurado.
- Solo un tenant de ejemplo (armacia1).

## Próximos Pasos
1. Activar contenedores con docker compose up -d.
2. Añadir más tenants.
3. Implementar CI/CD para despliegues.
