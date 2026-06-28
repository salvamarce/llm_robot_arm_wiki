---
title: Robot Arm Wiki — Home
aliases: [index, home, robot arm wiki, braccio robotico wiki, vault home]
created: 2026-06-15
updated: 2026-06-28
type: project
tags: [meta, index, home, navigation]
confidence: high
---

# Braccio Robotico DIY di Salvatore — Vault

> **Progetto:** Braccio robotico 4-DOF con NEMA 17, riduttori cycloidal 25:1, driver [[mks-servo42d]] su CAN bus, target 500g a 450 mm.
> Apri il **Grafo** (Graph View) in Obsidian per vedere tutte le connessioni tra le note.

---

## 🎯 Progetto Principale

| Pagina | Descrizione |
|--------|-------------|
| [[salvatore-robot-arm]] | Specifiche, stato avanzamento, roadmap, assegnazione motori |

## 🔧 Entità (Componenti Hardware)

| Pagina | Descrizione |
|--------|-------------|
| [[nema-17]] | Motori passo-passo NEMA 17 — specifiche, varianti, pro/contro |
| [[mks-servo42d]] | Driver closed-loop FOC con CAN bus — specifiche, cablaggio, libreria Arduino |

## 📐 Concetti (Design e Teoria)

| Pagina | Descrizione |
|--------|-------------|
| [[cycloidal-drive]] | Riduttore epicicloidale a disco — variante a due dischi sfasati |
| [[stepper-motor-control]] | Controllo motori passo-passo — microstepping, FOC closed-loop, profili accelerazione |
| [[analisi-cad-con-hermes]] | Analisi CAD via Fusion 360 MCP — setup LAN, roadmap cloud |
| [[cuscinetto-sfere-design-analysis]] | Analisi dimensionale cuscinetto a sfere (bearing v10) — geometria, PCD, qualità sfere |

## ⚖️ Confronti

| Pagina | Descrizione |
|--------|-------------|
| [[confronto-strutture-leggere]] | THOR, Forte, CyBot, Skyentific — raccomandazioni per struttura leggera |

---

## 📊 Statistiche Vault

- **Pagine totali:** 8 (escluse SCHEMA e log)
- **Wikilink:** Ogni pagina ha minimo 2 collegamenti entranti/uscenti
- **Graph view:** Colori per tipo — 🔶 Entity, 🟣 Concept, 🔵 Project, 🟢 Comparison
- **Ultimo aggiornamento:** 2026-06-28

---

## 🔗 Collegamenti Esterni

- [Repository GitHub MKS_SERVO42D Library](https://github.com/salvamarce/MKS_SERVO42D)
- [Repository GitHub Wiki](https://github.com/salvamarce/llm_robot_arm_wiki)
- [THOR Robot Arm](https://github.com/AngelLM/Thor)
- [Forte Arm Paper](https://arxiv.org/abs/2507.15693)
- [Makerbase SERVO42D](https://www.makerbase.cn/products/mks-servo42d)

---

*Per convenzioni wiki vedi [[SCHEMA]]. Per cronologia modifiche vedi [[log]].*
