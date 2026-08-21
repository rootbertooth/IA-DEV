# Decisiones Arquitectónicas: Sitios Estáticos

## 1. HTML/CSS/JS Vanilla en lugar de Frameworks
- **Contexto:** Sitios simples sin interacción compleja.
- **Decisión:** Usar HTML/CSS/JS puro.
- **Alternativas:** React, Vue, Tailwind.
- **Rationale:** Reduce peso, carga rápida, sin dependencias de build.

## 2. Nginx para Servir Archivos Estáticos
- **Contexto:** Servir sitios con alto rendimiento.
- **Decisión:** Nginx por su eficiencia en contenido estático.
- **Alternativas:** Apache, Caddy.
- **Rationale:** Nginx es el estándar en el VPS y maneja bien estáticos.

## 3. Sin Contenerización
- **Contexto:** Sitios estáticos sin necesidad de entornos complejos.
- **Decisión:** No usar Docker.
- **Alternativas:** Contenerización para portabilidad.
- **Rationale:** No es necesario, son solo archivos HTML/CSS/JS.
