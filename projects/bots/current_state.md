# Estado Actual: Bots

## Versiones Originales (VPS1 - /var/www/api/)

| Bot | Puerto | PID | Estado | Última modificación |
|-----|--------|-----|--------|---------------------|
| **responsebot** | 5005 | 886 (worker) | ✅ Activo | Aug 2026 |
| **respuestasinteligentes** | 5006 | 860 | ✅ Activo | May 2026 |
| **signalsbot** | - | 859 | ✅ Activo | Apr 2026 |
| **tenant-bot** | 5002 | 887 | ✅ Activo | Jun 2026 |

**Nota:** Los PIDs pueden variar, pero los procesos están activos según el informe de auditoría.

---

## Credenciales Detectadas (solo nombres de variables, NO valores)

| Bot | Variables Sensibles |
|-----|---------------------|
| **signalsbot** | TELEGRAM_TOKEN, DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, ANTHROPIC_API_KEY |
| **respuestasinteligentes** | OPENAI_API_KEY, JWT_SECRET_KEY, META_ACCESS_TOKEN, META_PHONE_ID, META_VERIFY_TOKEN, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, RESEND_API_KEY, VAPID_* |
| **responsebot** | OPENAI_API_KEY, TELEGRAM_API_ID, TELEGRAM_API_HASH, BOT_TOKEN, COINMARKETCAP_API_KEY, DB_* |
| **tenant-bot** | TELEGRAM_TOKEN, DB_*, ANTHROPIC_API_KEY, PERPLEXITY_API_KEY |

---

## Backups y Versionado

### respuestasinteligentes (VPS3)
- **Backups:** 15 sesiones de briefing en ackups/sesiones/
- **Prompts por empresa:** Versionados en ackend/prompts/
- **SQL dumps:** En ackups/sql/dumps/
- **Migraciones:** En ackups/sql/migraciones/
- **Archivos de configuración:** ackups/config/ con versiones anteriores de .env y config.py

### signalsbot (VPS1)
- **Archivos de datos:** chat_ids.json, chat_langs.json, used_coins.json

### tenant-bot (VPS3)
- **Backup completo:** 	enant-bot_code_20260602.tar.gz
- **Dump de DB:** signals_db_dev_20260602.sql

---

## Problemas Conocidos

### Generales
- **Versiones VPS3 inactivas:** Código migrado pero sin ejecución.
- **Sin contenerización:** Ningún bot está en Docker (ni VPS1 ni VPS3).
- **Sin CI/CD:** Despliegues manuales vía SCP.

### Específicos
- **responsebot (VPS3):** Session file de Telethon expuesta (+34694225803.session, 172KB).
- **respuestasinteligentes (VPS3):** Múltiples API keys de pago (OpenAI, Meta, Twilio, Resend).
- **signalsbot (VPS3):** Dependencia de Binance API (latencia, rate limits).
- **tenant-bot (VPS3):** Solo un cliente de ejemplo configurado.

---

## Próximos Pasos
1. **Decidir estado:** ¿Los bots de VPS3 deben estar activos? ¿Reemplazarán a los de VPS1?
2. **Si se activan:** Crear servicios systemd para cada bot en VPS3.
3. **Seguridad:** Rotar keys expuestas en session files de Telethon.
4. **Contenerización:** Migrar a Docker para entornos consistentes.
5. **Monitorización:** Implementar health checks y alertas para los bots activos.
