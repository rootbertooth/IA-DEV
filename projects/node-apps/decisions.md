# Decisiones Arquitectónicas: Node.js Apps

## 1. Uso de Node.js vs Python
- **Contexto:** Aplicaciones con frontend React y necesidad de backend ligero.
- **Decisión:** Node.js para proyectos donde el ecosistema JavaScript es más fuerte (ej. integración con Supabase).
- **Alternativas:** Python/Flask.
- **Rationale:** Node.js permite compartir código entre frontend y backend (TypeScript).

## 2. Supabase como Backend-as-a-Service
- **Contexto:** Necesidad de autenticación, base de datos y almacenamiento rápido.
- **Decisión:** Supabase para proyectos recientes (stock, ventas, gorillamansion).
- **Alternativas:** Firebase, AWS Amplify.
- **Rationale:** Supabase es open-source, usa PostgreSQL y tiene buen soporte para React.

## 3. Cloudflare Workers (tarracokey-app)
- **Contexto:** Despliegue serverless para API.
- **Decisión:** Usar Cloudflare Workers con Wrangler.
- **Alternativas:** AWS Lambda, Vercel.
- **Rationale:** Workers son rápidos y tienen buena integración con Cloudflare.

## 4. PM2 para Gestión de Procesos
- **Contexto:** Mantener aplicaciones Node.js en producción.
- **Decisión:** PM2 para reinicios automáticos y logs.
- **Alternativas:** systemd, forever.
- **Rationale:** PM2 es estándar en Node.js y fácil de configurar.
