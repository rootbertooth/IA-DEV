# Arquitectura Técnica: Node.js Apps

## Stack Tecnológico Común
| Componente | Tecnología | Versión |
|------------|------------|---------|
| **Backend** | Node.js | - |
| **Frontend** | React + Vite | 18/5+ |
| **Base de Datos** | Supabase (PostgreSQL) | - |
| **Autenticación** | Supabase Auth / JWT | - |

## Proyectos Destacados

### tarracokey-app (VPS1)
- **Cloudflare Workers:** Uso de Wrangler para despliegue.
- **PM2:** Gestión de procesos.

### gorillamansion.xyz, stock, ventas (VPS2)
- **Supabase:** Backend-as-a-Service (DB, Auth, Storage).
- **TypeScript:** Tipado estático.

### jfxsignals.com (VPS2)
- **API:** Backend en Node.js con módulo esend para emails.

### sfs.respuestasinteligentes.com (VPS2)
- **Python/Flask** (diferente al resto del grupo)

## Despliegue
- **PM2** para gestión de procesos.
- **Nginx** como proxy inverso.
