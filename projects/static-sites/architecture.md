# Arquitectura Técnica: Sitios Estáticos

## Stack Tecnológico Común
| Componente | Tecnología | Versión |
|------------|------------|---------|
| **Lenguajes** | HTML, CSS, JavaScript | - |
| **Servidor Web** | Nginx | - |

## Estructura de Directorios

```text
/var/www/html/{dominio}/
├── index.html
├── assets/
│   ├── css/
│   ├── js/
│   └── images/
└── ...

## Seguridad
- Sin autenticación (páginas públicas).
- Archivos estáticos servidos directamente por Nginx.

## Despliegue
- Copia manual de archivos via SCP.
- Sin CI/CD.
