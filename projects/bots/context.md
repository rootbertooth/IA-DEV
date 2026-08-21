# Contexto del Proyecto: Bots (Telegram / WhatsApp)

## Propósito y Visión
Colección de bots de mensajería con inteligencia artificial para automatizar tareas de comunicación, atención al cliente y trading de criptomonedas. Incluye versiones originales (VPS1) y versiones migradas (VPS3).

## Proyectos Incluidos

### Versiones Originales (VPS1 - /var/www/api/)
| Bot | Propósito | Tecnología | Estado |
|-----|-----------|------------|--------|
| **responsebot** | Bot de Telegram con personalidad IA (caché semántico) | Telethon + OpenAI + Sentence Transformers | ✅ Activo |
| **respuestasinteligentes** | Bot de WhatsApp Business para atención al cliente empresarial | Flask + OpenAI + Meta/Twilio API | ✅ Activo |
| **signalsbot** | Bot de trading crypto con análisis técnico y señales | Python + Telegram + Anthropic Claude | ✅ Activo |
| **tenant-bot** | Bot de trading con panel multi-tenant (SaaS) | Flask + React + MySQL | ✅ Activo |

## Relaciones con Otros Proyectos
- **Babywonder (VPS3):** Independiente. No comparten infraestructura ni dependencias.
- **Nexus (VPS2):** Independiente.
- **Que Cocino Hoy - qch (cocina-con-ia, VPS1):** Comparten stack (Flask + React) pero no hay comunicación directa.

## Estado General
- **Versiones VPS1:** ✅ 4 bots activos en producción.
- **Versiones VPS3:** ⏸️ 4 bots migrados pero sin ejecución (código listo).

## Migración VPS1 → VPS3
- **Origen:** /var/www/api/
- **Destino:** /opt/BOTS/
- **Fecha:** Agosto 2026
- **Motivo:** Consolidación de infraestructura y preparación para contenerización.
