# Arquitectura Técnica: Bots

## Stack Tecnológico Común (Versiones VPS1 y VPS3)

| Componente | Tecnología | Versión | Uso |
|------------|------------|---------|-----|
| **Framework Bot (Telegram)** | python-telegram-bot / Telethon | - | Bot API de Telegram (python-telegram-bot) o cliente MTProto (Telethon) |
| **Framework Web** | Flask | 3.x | APIs REST y webhooks |
| **IA / LLM** | OpenAI (AsyncOpenAI) | 2.29.0 | Generación de respuestas (responsebot, respuestasinteligentes) |
| **IA / LLM** | Anthropic Claude | claude-sonnet-4-5 | Análisis técnico y señales (signalsbot, tenant-bot) |
| **Embeddings** | Sentence Transformers | paraphrase-multilingual-MiniLM-L12-v2 | Caché semántico (responsebot) |
| **Base de Datos** | MySQL (PyMySQL / mysql.connector) | - | Almacenamiento de señales, historial, contexto |
| **Análisis Técnico** | pandas, pandas-ta | - | Indicadores técnicos (signalsbot) |
| **Datos Mercado** | Binance API, Fear & Greed Index | - | Precios, volumen, sentimiento (signalsbot) |

---

## Bots Individuales (Detalle Técnico)

### 1. signalsbot (Trading Crypto)
**Ruta original:** /var/www/api/signalsbot/  
**Ruta migrada:** /opt/BOTS/signalsbot/

- **IA:** Anthropic Claude (claude-sonnet-4-20250514)
- **Datos:** Binance API (REST) + Fear & Greed Index
- **Análisis técnico:** pandas, pandas-ta (RSI, MACD, ATR, soportes/resistencias, ondas de Elliott, Fibonacci)
- **Monedas soportadas:** 20 (BTC, ETH, SOL, BNB, XRP, DOGE, ADA, AVAX, LINK, DOT, SUI, TON, NEAR, APT, INJ, OP, ARB, WIF, RENDER, FET)
- **Lógica de scoring:** Score 1-10, umbral mínimo 4 para publicar
- **Límite:** Máximo 2 señales por día por moneda
- **Base de datos:** Tablas signals, signals_history, signals_discarded, signal_context
- **Prompt:** Extremadamente detallado (metodología de tendencia, ondas de Elliott, Fibonacci, figuras chartistas)

### 2. respuestasinteligentes (WhatsApp Business AI)
**Ruta original:** /var/www/api/respuestasinteligentes/  
**Ruta migrada:** /opt/BOTS/respuestasinteligentes/

- **IA:** OpenAI GPT (gpt-4o o similar)
- **Canales:** Meta Cloud API (primario) + Twilio API (alternativa)
- **Webhooks:** /wsp (Meta), /wsp_twilio (Twilio), /wsp360 (integración 360)
- **Flujo de conversación:**
  1. Webhook recibe mensaje
  2. Resolver empresa por número de teléfono
  3. Obtener historial (últimas 24h, max 10 mensajes)
  4. Construir contexto para OpenAI (system + history + mensaje actual)
  5. Llamada a OpenAI con prompt personalizado por empresa
  6. Guardar en DB y enviar respuesta vía API
- **Prompts por empresa:** Personalizados (ej. Notaría Alcanar con onboarding estricto y reglas de cierre)
- **Backups:** Estructura completa en ackups/ con 15 sesiones de briefing, prompts de empresas, SQL dumps, migraciones
- **Web push:** Notificaciones browser con py-vapid + pywebpush
- **Email:** Resend API

### 3. responsebot (Telegram IA)
**Ruta original:** /var/www/api/responsebot/  
**Ruta migrada:** /opt/BOTS/responsebot/

- **Cliente Telegram:** Telethon (MTProto) — control de cuenta de usuario, no bot API
- **IA:** OpenAI AsyncOpenAI para generación de respuestas
- **Embeddings:** Sentence Transformers (paraphrase-multilingual-MiniLM-L12-v2)
- **Caché semántico:** Similitud coseno con umbral 0.85 (reutiliza respuestas para ahorrar tokens)
- **Personalidad:** "Bob" — 32 años, Buenos Aires/Valencia, crypto trader, humor natural, responde en el idioma del usuario
- **Protección Anti-Flood:** Delay base 2.0s, grupos prioritarios con 0.5s, reintentos con Tenacity
- **Workers:** worker_brain_ai.py (cerebro principal), worker_utils.py, egister_session.py
- **Session activa:** +34694225803.session (172KB)
- **Flask API:** :5005 para gestión de cuentas y códigos de verificación

### 4. tenant-bot (Multi-Tenant Signals)
**Ruta original:** /var/www/api/tenant-bot/  
**Ruta migrada:** /opt/BOTS/tenant-bot/

- **Backend:** Flask :5002 con JWT + bcrypt
- **Frontend:** React + Vite con i18n (ES/EN), SweetAlert2, ESLint
- **Multi-tenant:** Clientes con configuración propia (coins, min_score, daily_limit, idioma, timezone)
- **Roles:** Superadmin (gestiona clientes) + Client (ve sus datos)
- **Score Factors:** Análisis de señales históricas para optimizar scoring (discretización de RSI, Fear&Greed)
- **Base de datos:** Tablas clients, client_config, signals (con tenant_id)
- **Backups incluidos:** 	enant-bot_code_20260602.tar.gz, signals_db_dev_20260602.sql

---

## Migración VPS1 → VPS3 (Detalles)
- **Ruta origen:** /var/www/api/
- **Ruta destino:** /opt/BOTS/
- **Estructura:** Cada bot mantiene su propia carpeta con código, .env y dependencias.
- **Estado:** Código migrado completamente, pero **ningún bot está en ejecución en VPS3** (sin servicios systemd ni procesos activos).
- **Motivo de la migración:** Consolidación de infraestructura, preparación para contenerización y separación de entornos.
