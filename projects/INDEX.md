# 📋 Índice de Proyectos del Ecosistema (Index)

Este documento es el **índice maestro** de todos los proyectos activos e inactivos del ecosistema. Contiene 25 proyectos documentados distribuidos en 2 VPS, con su ubicación, estado y una breve descripción de cada uno. Los despliegues adicionales en VPS3 (BabyWonder Motor y las versiones migradas de los bots) se detallan en las fichas de sus grupos.

---

## 1. VPS1 — Laboratorio / Entorno Legacy

| # | Proyecto | Ruta | Estado | Descripción Breve |
|---|----------|------|--------|-------------------|
| 1 | **cocina-con-ia** | `/var/www/cocina-con-ia` | ✅ Activo | Asistente culinario con IA. 8 modos de prompt, RAG con embeddings OpenAI y caché semántico en MySQL. |
| 2 | **benjamin** | `/var/www/benjamin` | ✅ Activo | Aplicación web con IA para gestión de contenido. Backend Flask, frontend React/Vite. |
| 3 | **ofericios** | `/var/www/ofericios` | ✅ Activo | Gestión de ofertas y promociones con IA. Backend Flask, frontend React/Vite. |
| 4 | **way** | `/var/www/way` | ⏸️ Inactivo | Aplicación web con IA para rutas y planificación. Backend Flask, frontend React/Vite. |
| 5 | **carrerags.org** | `/var/www/html/carrerags.org` | ⏸️ Inactivo | Sitio web corporativo con backend Node.js y frontend React. |
| 6 | **tarracokey-app** | `/var/www/tarracokey-app` | ✅ Activo | Aplicación de gestión de claves con Cloudflare Workers y frontend React. |
| 7 | **responsebot (VPS1)** | `/var/www/api/responsebot` | ✅ Activo | Bot de Telegram con IA y personalidad (versión original). Usa Telethon y OpenAI. |
| 8 | **respuestasinteligentes (VPS1)** | `/var/www/api/respuestasinteligentes` | ✅ Activo | Bot de WhatsApp Business con IA para atención al cliente (versión original). Flask + OpenAI + Meta Cloud API. |
| 9 | **signalsbot (VPS1)** | `/var/www/api/signalsbot` | ✅ Activo | Bot de trading crypto con análisis técnico y señales (versión original). Telegram + Anthropic Claude. |
| 10 | **tenant-bot (VPS1)** | `/var/www/api/tenant-bot` | ✅ Activo | Bot de trading con panel multi-tenant (versión original). Flask + React + MySQL. |
| 11 | **app.respuestasinteligentes.com** | `/var/www/html/app.respuestasinteligentes.com` | ✅ Activo | Landing page estática para aplicaciones. HTML/JS. |
| 12 | **ebro.delivery** | `/var/www/html/ebro.delivery` | ⏸️ Inactivo | Página promocional estática. HTML. |
| 13 | **fundacionvillanova.org** | `/var/www/html/fundacionvillanova.org` | ⏸️ Inactivo | Página institucional estática. HTML/JS. |
| 14 | **respuestasinteligentes.com** | `/var/www/html/respuestasinteligentes.com` | ✅ Activo | Página corporativa estática de Respuestas Inteligentes. HTML/JS. |
| 15 | **tarracokey.respuestasinteligentes.com** | `/var/www/html/tarracokey.respuestasinteligentes.com` | ✅ Activo | Página de aterrizaje para Tarracokey. HTML/JS. |
| 16 | **telegramusers.com** | `/var/www/html/telegramusers.com` | ⏸️ Inactivo | Página informativa sobre usuarios de Telegram. HTML/JS. |
| 17 | **way.respuestasinteligentes.com** | `/var/www/html/way.respuestasinteligentes.com` | ⏸️ Inactivo | Página de aterrizaje para Way. HTML/JS. |

---

## 2. VPS2 — Productos de Negocio

| # | Proyecto | Ruta | Estado | Descripción Breve |
|---|----------|------|--------|-------------------|
| 18 | **blog.gorillamansion.xyz** | `/var/www/blog.gorillamansion.xyz` | ✅ Activo | Blog corporativo de Gorilla Mansion. WordPress con PHP-FPM. |
| 19 | **blog.jfxsignals.com** | `/var/www/blog.jfxsignals.com` | ✅ Activo | Blog de señales financieras JFX Signals. WordPress con PHP-FPM. |
| 20 | **gorillamansion.xyz** | `/var/www/gorillamansion.xyz` | ✅ Activo | Sitio principal de Gorilla Mansion. Node.js/React + Supabase. |
| 21 | **jfxsignals.com** | `/var/www/jfxsignals.com` | ✅ Activo | Plataforma de señales financieras. Node.js/React. |
| 22 | **sfs.respuestasinteligentes.com** | `/var/www/sfs.respuestasinteligentes.com` | ✅ Activo | Sistema de gestión de facturación/stock. Python/Flask + React. |
| 23 | **stock.respuestasinteligentes.com** | `/var/www/stock.respuestasinteligentes.com` | ✅ Activo | Gestión de inventario. Node.js/React + Supabase. |
| 24 | **ventas.respuestasinteligentes.com** | `/var/www/ventas.respuestasinteligentes.com` | ✅ Activo | CRM y gestión de ventas. Node.js/React + Supabase. |
| 25 | **nexus** | `/opt/nexus` | ⏸️ Inactivo | Plataforma multi-tenant contenerizada. Docker + Traefik + Flask + React + PostgreSQL + Redis. |

---

## 3. Resumen Global

| VPS | Activos | Inactivos | Total |
|-----|---------|-----------|-------|
| **VPS1** | 11 | 6 | 17 |
| **VPS2** | 7 | 1 | 8 |
| **Total** | **18** | **7** | **25** |

---

*Este documento es el índice maestro del ecosistema. Se actualiza cada vez que se añade, modifica o elimina un proyecto.*
