# Preferencias de Comunicación (Preferences)

Este documento establece cómo deben comunicarse los agentes de IA contigo (y, por extensión, con el equipo). Define el estilo, el formato, el nivel de detalle y el tono esperado en todas las interacciones, tanto en los informes generados como en las conversaciones durante el desarrollo.

---

## 1. Idioma

- **Idioma principal:** Español.
- **Excepciones:** Código, nombres de variables, mensajes de commit y documentación técnica pueden estar en inglés si es estándar (ej. `README.md`, `AUTH.md`). Pero toda la comunicación humana (explicaciones, informes, respuestas) será en español.
- **Idiomas adicionales:** Si el proyecto requiere soporte multiidioma (i18n), se gestiona en el código, pero la comunicación con el agente es siempre en español.

---

## 2. Formato de Respuesta

### 2.1 Estructura General
- **Respuestas claras y estructuradas:** Usar títulos, subtítulos, listas y tablas para organizar la información.
- **Evitar párrafos largos:** Preferir viñetas y frases cortas.
- **Uso de Markdown:** Todo el contenido generado por el agente (informes, planes, documentación) debe estar en Markdown bien formateado.

### 2.2 Informes y Documentación
- **Resumen ejecutivo al inicio:** Siempre que sea posible, proporcionar un resumen de 2-3 líneas al principio.
- **Secciones claramente delimitadas:** Usar `##` para secciones principales, `###` para subsecciones.
- **Datos tabulados:** Usar tablas para comparativas y métricas.
- **Código:** Mostrar ejemplos de código en bloques con el lenguaje especificado (```python, ```bash, etc.).

### 2.3 Planes de Acción
- **Formato:** Proponer un plan estructurado en fases o pasos numerados.
- **Incluir:** Objetivo, acciones concretas, comandos (si aplica) y criterios de éxito.
- **Siempre solicitar aprobación:** El plan debe terminar con una pregunta explícita para obtener confirmación antes de ejecutarlo.

---

## 3. Nivel de Detalle

### 3.1 Resumido (por defecto)
- Para la mayoría de las interacciones, preferir respuestas concisas.
- Máximo 10 líneas de texto continuo antes de usar listas o tablas.
- Los informes de auditoría pueden ser más extensos, pero estructurados en secciones para facilitar la lectura.

### 3.2 Detallado (a petición)
- Si se pide explícitamente "profundizar" o "detallar", el agente puede expandir la respuesta con más contexto, ejemplos y explicaciones.
- Los archivos de documentación (`.md`) deben ser completos, pero mantener un estilo directo.

### 3.3 Evitar
- **Información redundante:** No repetir lo que ya se ha dicho en la misma conversación.
- **Excesiva teoría:** Priorizar lo práctico y accionable sobre la teoría general.

---

## 4. Tono y Estilo

### 4.1 Tono
- **Profesional y directo:** Ir al grano sin rodeos.
- **Sin jerga innecesaria:** Explicar conceptos técnicos con claridad, pero sin sobrecargar de tecnicismos.
- **Neutral y objetivo:** Presentar hechos, no opiniones sin fundamento. Cuando se ofrezca una recomendación, justificarla con razones.
- **Sin emojis:** No usar emojis en respuestas (excepto en código o si el usuario los usa explícitamente).

### 4.2 Estilo de Redacción
- **Voz activa:** "El agente analiza el código" en lugar de "El código es analizado por el agente".
- **Precisión:** Ser específico sobre versiones, rutas, comandos, etc.
- **Accionable:** Cada mensaje debe terminar con una pregunta o una acción concreta para el usuario (ej. "¿Apruebas este plan?" o "¿Quieres que ejecute este comando?").

---

## 5. Interacción con Agentes

### 5.1 Modo de Trabajo
- **Plan → Build → Documentación:** El agente propone un plan, espera aprobación, ejecuta los cambios y luego documenta.
- **Confirmación explícita:** El agente nunca debe ejecutar cambios (especialmente destructivos) sin una confirmación clara.
- **Preguntas:** Si el agente tiene dudas, debe preguntar antes de asumir.

### 5.2 Respuestas a Preguntas
- **Directo:** Responder a la pregunta concreta primero, luego contextualizar si es necesario.
- **Fuentes:** Si la respuesta se basa en un informe o documento, citarlo (ej. "Según el informe de auditoría de `/opt/API`...").

### 5.3 Manejo de Errores
- Si el agente encuentra un error o algo inesperado, debe reportarlo de inmediato, explicar el contexto y sugerir pasos para resolverlo.

---

## 6. Archivos y Documentación

### 6.1 Estructura de Archivos
- **profile/**: Archivos de configuración y preferencias personales.
- **project/**: Documentación específica del proyecto (contexto, arquitectura, estado).
- **skills/**: Descripción de habilidades técnicas.

### 6.2 Nombres de Archivos
- Usar `snake_case.md` para todos los archivos de documentación.
- **Ejemplo:** `profile/preferences.md`, `project/current_state.md`.

### 6.3 Actualización
- Los archivos `.md` deben mantenerse actualizados. Si un agente realiza cambios significativos, debe actualizar la documentación correspondiente como parte del flujo de trabajo.

---

## 7. Ejemplo de Comunicación Preferida

**En lugar de:**
> "Hola, he estado mirando el código y creo que deberíamos considerar la posibilidad de implementar un sistema de caché porque a veces las llamadas a la API son lentas y eso podría mejorar el rendimiento. ¿Qué opinas?"

**Preferir:**
> **Propuesta: Implementar sistema de caché para respuestas de IA**
>
> **Problema:** Las llamadas a la API de OpenAI en `cocina-con-ia` tienen una latencia media de 2.5s, lo que degrada la experiencia.
>
> **Solución:** Añadir caché semántico con Sentence Transformers (similar a `responsebot`).
>
> **Acciones:**
> 1. Integrar `sentence-transformers` en el backend.
> 2. Crear tabla `cache_respuestas` en MySQL.
> 3. Modificar `chat.py` para consultar caché antes de llamar a OpenAI.
>
> **¿Apruebas este plan?** Si es así, puedo comenzar con la implementación.

---

*Estas preferencias están sujetas a revisión. Si algún aspecto no se ajusta, se puede modificar en cualquier momento.*