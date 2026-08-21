# Contexto del Proyecto: ¿Qué Cocino Hoy? (QCH)

## Propósito y Visión
Asistente culinario con inteligencia artificial que ayuda a los usuarios a decidir qué cocinar, generar recetas personalizadas y guiar en la cocina en tiempo real. Combina múltiples modos de interacción (antojos, menús semanales, cocina por pasos, etc.) con IA generativa.

## Dominio y Alcance
- **Área:** Cocina / Gastronomía / Nutrición.
- **Propósito:** Ofrecer recetas adaptadas al perfil del usuario (dieta, alergias, presupuesto, tiempo disponible).
- **Modos:** 8 modos de interacción (apetece, clásica, cocción, ingredientes, menú, mundo, rápido, tiempo, visión).

## Actores
- **Usuario final:** Persona que busca recetas o ayuda en la cocina.
- **Sistema (Miga):** Asistente IA con personalidad propia.
- **Administrador:** Gestiona prompts, configuración y créditos.

## Entorno
- **Servidor:** VPS1 (89.167.100.214)
- **Ruta:** /var/www/cocina-con-ia
- **Estado:** ✅ Activo (PID 855, 1058)
- **Backend:** Flask :5000 (Gunicorn)
- **Frontend:** React + Vite
- **Base de datos:** MySQL
- **IA:** OpenAI (embeddings, chat) + Anthropic Claude (razonamiento)

## Relaciones con Otros Proyectos
- **/opt/ai (VPS3):** No relacionado directamente (QCH usa APIs cloud, no modelos locales).
- **ots (VPS3):** No relacionado.

## Estado Actual
- **Desarrollo:** 8 modos de prompt implementados con RAG y caché semántico.
- **Rendimiento:** Depende de APIs externas (2-5s por llamada).
- **Próximos pasos:** Optimizar caché, añadir más modos, mejorar personalización.
