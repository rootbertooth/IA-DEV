# Decisiones Arquitectónicas: WordPress Blogs

## 1. WordPress como CMS
- **Contexto:** Necesidad de un blog rápido de implementar con gestión de contenido fácil.
- **Decisión:** WordPress por su ecosistema de plugins y facilidad de uso.
- **Alternativas:** Ghost, Strapi, Headless CMS.
- **Rationale:** WordPress es estándar, tiene buena compatibilidad con SEO y es fácil de mantener.

## 2. Usuarios Dedicados por Blog
- **Contexto:** Aislamiento de recursos y seguridad.
- **Decisión:** Crear usuarios Unix separados (wpblog, wpjfx).
- **Alternativas:** Un solo usuario para todos los blogs.
- **Rationale:** Previene que un blog comprometido afecte a los demás.

## 3. Nginx + PHP-FPM
- **Contexto:** Servir WordPress con buen rendimiento.
- **Decisión:** Nginx como servidor web y PHP-FPM para ejecutar PHP.
- **Alternativas:** Apache.
- **Rationale:** Nginx es más ligero y eficiente para sitios con tráfico.

## 4. WP-CLI para Mantenimiento
- **Contexto:** Tareas administrativas (actualizaciones, plugins).
- **Decisión:** Usar WP-CLI para gestionar WordPress desde línea de comandos.
- **Alternativas:** Panel de administración web.
- **Rationale:** WP-CLI permite automatizar tareas y es más rápido.
