# Decisiones Arquitectónicas: Bots

## 1. Uso de Telethon vs python-telegram-bot
- **Contexto:** Control de cuentas de usuario vs bots de Telegram.
- **Decisión:** Usar **Telethon** en esponsebot (control de cuenta de usuario) y **python-telegram-bot** en signalsbot (bot API).
- **Alternativas:** Todas con python-telegram-bot, todas con Telethon.
- **Rationale:** Telethon permite mayor control (sesiones persistentes, actuar como usuario real), python-telegram-bot es más sencillo para bots estándar.

## 2. Caché Semántico con Sentence Transformers (responsebot)
- **Contexto:** Reducir costes de API de OpenAI y mantener consistencia en respuestas.
- **Decisión:** Implementar caché semántico con embeddings de Sentence Transformers y similitud coseno (umbral 0.85).
- **Alternativas:** Caché exacta (hash de mensajes), Redis con TTL.
- **Rationale:** Permite reutilizar respuestas para preguntas similares pero no idénticas, ahorrando tokens y manteniendo coherencia.

## 3. Dual Provider: OpenAI + Anthropic (signalsbot y tenant-bot)
- **Contexto:** Señales de trading requieren análisis técnico profundo.
- **Decisión:** Usar **Anthropic Claude** para razonamiento y análisis técnico, y **OpenAI** en otros bots (respuestasinteligentes, responsebot).
- **Alternativas:** Solo OpenAI, solo Claude.
- **Rationale:** Claude tiene mejor razonamiento en tareas de análisis de datos y seguimiento de instrucciones complejas.

## 4. Migración VPS1 → VPS3 (Consolidación)
- **Contexto:** Centralizar bots en un solo servidor para facilitar mantenimiento y futura contenerización.
- **Decisión:** Migrar todo el código de /var/www/api/ a /opt/BOTS/ en VPS3.
- **Alternativas:** Mantener bots en VPS1 y VPS3 por separado.
- **Rationale:** Simplifica la gestión, permite una única base de datos y prepara el terreno para Docker.

## 5. Uso de Flask para Webhooks (respuestasinteligentes)
- **Contexto:** Necesidad de endpoints HTTP para recibir mensajes de WhatsApp.
- **Decisión:** Flask por su simplicidad y facilidad para manejar webhooks.
- **Alternativas:** FastAPI, Node.js/Express.
- **Rationale:** Flask es ligero y se integra bien con el resto del ecosistema (bases de datos MySQL, dotenv).

## 6. Multi-Tenant con JWT + bcrypt (tenant-bot)
- **Contexto:** SaaS de señales de trading con clientes independientes.
- **Decisión:** Autenticación JWT y hashing de contraseñas con bcrypt, aislamiento de datos por tenant_id.
- **Alternativas:** OAuth2, sesiones de Flask.
- **Rationale:** JWT es sin estado y escalable; bcrypt es estándar para contraseñas; tenant_id asegura aislamiento.

## 7. Rate Limiting y Anti-Flood (responsebot)
- **Contexto:** Evitar bans de Telegram por envío masivo de mensajes.
- **Decisión:** Delay base de 2.0s, grupos prioritarios con 0.5s, reintentos con Tenacity.
- **Alternativas:** Sin límites, usar proxies.
- **Rationale:** Protege la cuenta de usuario de Telegram de ser bloqueada, manteniendo fluidez en grupos activos.

## 8. Backups Estructurados (respuestasinteligentes)
- **Contexto:** Seguimiento de cambios y recuperación ante fallos en un bot crítico de atención al cliente.
- **Decisión:** Backups con timestamp, versionado de prompts por empresa, dumps SQL y migraciones.
- **Alternativas:** Git + Git LFS, backups en la nube.
- **Rationale:** Permite recuperar configuraciones y prompts específicos por empresa, muy útil en entornos multi-cliente.

## 9. Prompts Externalizados y por Empresa (respuestasinteligentes)
- **Contexto:** Cada empresa cliente tiene su propio flujo de conversación y datos.
- **Decisión:** Archivos .txt separados en ackend/prompts/empresas/.
- **Alternativas:** Prompts en base de datos, prompts en código.
- **Rationale:** Permite editar prompts sin reiniciar el servidor y facilita la personalización por cliente.

## 10. Uso de Workers en Segundo Plano (responsebot)
- **Contexto:** Tareas de IA pueden ser largas (llamadas a OpenAI).
- **Decisión:** Workers independientes (worker_brain_ai.py) para procesar mensajes en segundo plano.
- **Alternativas:** Colas con Celery, Redis RQ.
- **Rationale:** Workers son simples de implementar y mantienen la interfaz de usuario ágil.
