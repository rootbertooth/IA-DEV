# Arquitectura Técnica: WordPress Blogs

## Stack Tecnológico Común
| Componente | Tecnología | Versión |
|------------|------------|---------|
| **CMS** | WordPress | - |
| **Servidor Web** | Nginx | - |
| **PHP** | PHP-FPM | 8.x |
| **Base de Datos** | MySQL | - |

## Estructura de Directorios
/var/www/blog.{dominio}/
├── public_html/ # Raíz de WordPress
│ ├── wp-admin/
│ ├── wp-content/
│ ├── wp-includes/
│ ├── index.php
│ └── wp-config.php
├── logs/ # Logs de acceso/error
└── .wp-cli/ # Configuración de WP-CLI

text

## Usuarios Dedicados
| Blog | Usuario | Grupo |
|------|---------|-------|
| blog.gorillamansion.xyz | wpblog | www-data |
| blog.jfxsignals.com | wpjfx | www-data |

## Seguridad
- Configuración de WordPress con claves secretas.
- PHP-FPM con usuarios dedicados para aislamiento.
