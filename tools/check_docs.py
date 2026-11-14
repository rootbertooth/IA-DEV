#!/usr/bin/env python3
"""Verificacion de higiene de la documentacion: fences, BOM, control chars,
enlaces internos y datos sensibles (IPs publicas, telefonos, rutas locales)."""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WHITELIST_IP = {"127.0.0.1", "0.0.0.0", "255.255.255.255"}
GEN_IP = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
PHONE = re.compile(r"\+?3?4?\s?[678]\d{2}[\s.-]?\d{3}[\s.-]?\d{3}\b")
LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")
fail = []

for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d != ".git"]
    for f in sorted(fn):
        p = os.path.join(dp, f)
        rel = os.path.relpath(p, ROOT)
        if os.path.abspath(p) == os.path.abspath(__file__):
            continue
        raw = open(p, "rb").read()
        if raw.startswith(b"\xef\xbb\xbf"):
            fail.append(f"{rel}: BOM al inicio")
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            fail.append(f"{rel}: bytes no UTF-8")
            continue
        bad = [f"{hex(ord(c))}@{i}" for i, c in enumerate(text)
               if (ord(c) < 32 and c not in "\t\n") or (127 <= ord(c) < 160)]
        if bad:
            fail.append(f"{rel}: caracteres de control {bad[:5]}")
        if f.lower().endswith(".md"):
            n_fences = sum(1 for l in text.split("\n") if l.strip().startswith("```"))
            if n_fences % 2:
                fail.append(f"{rel}: fences sin cerrar ({n_fences})")
            base = os.path.dirname(p)
            for m in LINK.finditer(text):
                tgt = m.group(1)
                if tgt.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                if not os.path.exists(os.path.normpath(os.path.join(base, tgt))):
                    fail.append(f"{rel}: enlace interno roto -> {tgt}")
        for m in GEN_IP.finditer(text):
            ip = m.group(0)
            octs = ip.split(".")
            # Heuristica: IP publica si algun octeto >= 100 (versiones tipo 4.11.0.86 se excluyen)
            if ip not in WHITELIST_IP and any(int(o) >= 100 for o in octs):
                fail.append(f"{rel}: posible IP publica {ip}")
        for m in PHONE.finditer(text):
            digits = re.sub(r"\D", "", m.group(0))
            if len(digits) in (9, 11):
                fail.append(f"{rel}: posible numero de telefono {m.group(0)!r}")
        if "C:\\Users" in text or "C:/Users" in text:
            fail.append(f"{rel}: ruta local de Windows")

if fail:
    print("ERRORES DE HIGIENE:")
    for e in fail:
        print(" -", e)
    sys.exit(1)
print("OK: higiene de documentacion correcta")
