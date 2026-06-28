---
title: Analisi CAD con Hermes
aliases: [analisi-cad-con-hermes, CAD analysis, Fusion MCP, Hermes CAD, analisi CAD, Fusion 360 MCP]
created: 2026-06-15
updated: 2026-06-28
type: concept
tags: [cad, fusion-360, mcp, analysis, workflow, planning]
confidence: high
---

# Analisi CAD con Hermes

Come Hermes può analizzare e ottimizzare i progetti CAD del braccio robotico. Due modalità: Fusion MCP (parametrico) e trimesh (solo mesh STL).

---

## Metodo 1: Fusion MCP Server (Consigliato)

**Stato:** ✅ Disponibile (ufficiale Autodesk, GA)
**Richiede:** Fusion 360 aperto sul PC Windows + connessione LAN

### Come funziona
Fusion 360 (da aprile 2026) espone un server MCP locale quando è in esecuzione. Hermes su Proxmox si connette via rete locale all'IP del PC Windows.

### Cosa permette di fare
- Leggere feature e parametri del modello parametrico
- Estrarre dimensioni, quote, vincoli
- Analizzare interferenze tra componenti in un assieme
- Verificare spessori, angoli di svasatura, raggi di raccordo
- Modificare il progetto (aggiungere feature, modificare parametri)
- Esportare in STL/STEP/3MF

### Setup
1. Su PC Windows: attivare MCP Server in Fusion 360 (Preferences → MCP Server)
2. Identificare IP del PC in LAN (`ipconfig` su Windows)
3. Identificare porta del server Fusion MCP
4. Su Hermes (Proxmox): aggiungere in `~/.hermes/config.yaml`:
   ```yaml
   mcp_servers:
     fusion:
       url: "http://<IP-PC>:<PORTA>"
       timeout: 120
   ```
5. `hermes gateway restart` per aggiornare i tool

### Limiti
- Richiede PC acceso e Fusion 360 aperto
- Non disponibile 24/7
- Dipende dalla rete LAN

---

## Metodo 2: trimesh (STL Analysis)

**Stato:** ⬜ Non installato — valutazione: poco utile per il progetto
**Richiede:** Solo file STL, niente Fusion

### Cosa farebbe
- Calcolare volume e superficie
- Rilevare bordi non manifold
- Analizzare angoli di sbalzo per stampa FDM
- Verificare pareti sottili
- Controllare intersezioni tra parti in un assieme

### Perché non lo usiamo
Le stesse informazioni sono già visibili nel slicer (Cura, PrusaSlicer) in modo più immediato. trimesh non può fare analisi ingegneristica reale — non vede feature, non capisce intenzioni progettuali.

Installazione richiesta: `pip install trimesh numpy-stl`

---

## Metodo 3: Fusion Data MCP (Remoto)

**Stato:** ✅ Disponibile (ufficiale Autodesk)
**Richiede:** Account Autodesk, connessione internet

### Cosa fa
- Gestione progetti cloud Fusion
- Elenco file, versioni, collaboratori
- Operazioni amministrative

### Non fa
- Modellazione o analisi parametrica

Poco utile per revisioni di design.

---

## Metodo 4: Fusion Automation MCP (Cloud — In arrivo)

**Stato:** 🚧 Annunciato, non ancora disponibile
**Richiede:** Niente — gira su cloud Autodesk

### Cosa promette
- Toolset completo di modellazione via cloud
- Nessuna installazione locale necessaria
- Gira su qualsiasi server (incluso Proxmox)
- Stesse capacità del Fusion MCP locale ma sempre disponibile

**Questa sarà la soluzione 24/7.**

---

## Flusso Consigliato (Oggi)

```
Quando lavori ai modelli CAD:
  PC acceso + Fusion aperto
       ↓
  Connetti Hermes via MCP LAN
       ↓
  Revisione parametrica del design
  
Quando non lavori ai modelli:
  Analisi offline non disponibile
  → Aspetta Fusion Automation MCP cloud
```

## Related
- [[salvatore-robot-arm]] — Progetto su cui si applica
- SCHEMA.md — Wiki conventions
- Skill: `mechanical-engineer` — carica con `/skill mechanical-engineer` per attivare la persona da ingegnere meccanico
