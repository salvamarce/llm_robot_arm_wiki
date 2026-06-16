---
title: Confronto Bracci Robotici 3D Stampati — Strutture Leggere
created: 2026-06-15
updated: 2026-06-15
type: comparison
tags: [comparison, 3d-printing, structure, lightweight, beginner, intermediate]
confidence: high
sources: [github.com/AngelLM/Thor, arxiv.org/abs/2507.15693, kingroon.com/blogs/top-3d-printed-robot-arm-projects, circuitdigest.com/top-10-opensource-robotic-arms]
---

# Confronto Bracci Robotici 3D Stampati — Strutture Leggere

Analisi dei progetti open-source di bracci robotici stampati in 3D, con focus su strutture leggere, minimali e robuste. Esclude i progetti super-grossi (es. "Giant Robot Arm" con motori ingombranti).

> **Obiettivo di Salvatore:** Braccio con NEMA 17, riduttori cycloidal stampati, materiali misti PLA/PETG/TPU, leggero e minimal ma robusto.

---

## Progetti Analizzati

### 1. THOR — AngelLM
| Specifica | Valore |
|-----------|--------|
| **DOF** | 6 (Yaw-Roll-Roll-Yaw-Roll-Yaw) |
| **Altezza** | 625 mm |
| **Payload** | 750 g |
| **Motori** | Stepper (NEMA 17 simili) |
| **Trasmissione** | Ingranaggi stampati + pulegge GT2 + cinghie |
| **Materiale** | PLA/PETG |
| **Costo BOM** | ~350€ |
| **Peso totale** | ~2.5 kg |
| **Struttura** | Braccio tubolare segmentato, giunti compatti |
| **Pro:** | Design maturo, ampia community, documentazione eccellente, ROS2 pronto |
| **Contro:** | Rumoroso (ingranaggi stampati), struttura tradizionale non ottimizzata per peso minimo |
| **Rilevanza:** | 🟡 Riferimento ma struttura più massiccia del necessario |

### 2. Forte — UMass Amherst
| Specifica | Valore |
|-----------|--------|
| **DOF** | 6 (RRPRRR) |
| **Raggiungimento** | 467 mm |
| **Payload** | 630 g |
| **Motori** | NEMA 17 + NEMA 23 |
| **Trasmissione** | Capstan (cavo d'acciaio) + cinghie + ingranaggi elicoidali |
| **Materiale** | PLA (30% infill) |
| **Costo BOM** | ~$212 |
| **Peso totale** | 3.5 kg |
| **Ripetibilità** | 0.467 mm |
| **Struttura** | Ottimizzazione topologica FEM, braccio cavo, motori alla base |
| **Pro:** | Struttura ottimizzata per peso minimo con FEA, rapporto payload/peso eccellente, precisione sub-mm, bassissimo costo |
| **Contro:** | Usa anche NEMA 23 (più grossi), trasmissione a cavo complessa, richiede stampa accurata |
| **Rilevanza:** | 🟢 Ottimo riferimento per filosofia di design leggero |

### 3. CyBot — quartit (In Progress)
| Specifica | Valore |
|-----------|--------|
| **DOF** | 6 |
| **Raggiungimento** | 400-500 mm |
| **Payload** | 500 g - 1 kg |
| **Motori** | 6× NEMA 17 |
| **Trasmissione** | **Cycloidal gearbox stampato 3D** (20:1 max, quasi zero backlash) |
| **Materiale** | PLA/PETG |
| **Costo** | ~200-300€ stimato |
| **Struttura** | Attuatori compatti con cycloidal integrati |
| **Pro:** | **Stessa filosofia progettuale di Salvatore** — NEMA 17 + cycloidal, componenti minimi, design compatto |
| **Contro:** | Progetto ancora in sviluppo (no firmware completo), tolleranze critiche per cycloidal |
| **Rilevanza:** | 🟢 **ALTISSIMA** — Progetto gemello per filosofia |

### 4. Skyentific 6DoF
| Specifica | Valore |
|-----------|--------|
| **DOF** | 6 |
| **Precisione** | 0.2 mm |
| **Payload** | 150 g |
| **Motori** | Stepper |
| **Trasmissione** | Diretta + cinghie |
| **Materiale** | PETG (0.15 mm, 50% infill) |
| **Struttura** | Design segmentato modulare |
| **Pro:** | Precisione eccellente, codice Arduino su GitHub |
| **Contro:** | Payload basso, struttura meno robusta |
| **Rilevanza:** | 🟡 Riferimento per precisione |

### 5. EEZYbotARM MK2 — DaGHIZmo
| Specifica | Valore |
|-----------|--------|
| **DOF** | 4 |
| **Raggiungimento** | ~250 mm |
| **Payload** | ~100 g |
| **Motori** | MG90S servos |
| **Trasmissione** | Collegamento diretto |
| **Materiale** | PLA |
| **Costo** | ~50€ |
| **Struttura** | Braccio piatto segmentato |
| **Pro:** | Economico, facile, entry-level |
| **Contro:** | Struttura poco rigida, payload molto limitato |
| **Rilevanza:** | 🔴 Non adatto a NEMA 17 o cycloidal |

---

## Raccomandazioni per il Progetto di Salvatore

### Approccio Strutturale Consigliato

Basandoti su NEMA 17 + riduttori cycloidal stampati, la struttura ideale combina elementi da più progetti:

**Geometria del braccio:**
- **Braccio aperto/tubolare** tipo Forte — struttura ottimizzata (cavo, con nervature), non massiccio
- **Segmenti a C o a U** per risparmiare peso mantenendo rigidezza torsionale
- Giunti compatti con **cycloidal integrato nel mozzo** (stile CyBot)

**Materiali:**
- **PETG per la struttura portante** — più rigido del PLA, migliore resistenza a calore e creep
- **PLA+ per prototipi e parti non strutturali**
- **TPU per piedini antivibranti, cuscinetti soft, guarnizioni** tra giunti
- **Inserti filettati in ottone** nei punti di assemblaggio (M3/M4)

**Configurazione DOF (3 → 4):**
1. **J1 — Base (Yaw):** Rotazione orizzontale. Cycloidal + cuscinetto reggispinta
2. **J2 — Spalla (Pitch):** Movimento verticale. Cycloidal + coppia di cuscinetti. **Giunto più sollecitato**
3. **J3 — Gomito (Pitch):** Secondo segmento. Cycloidal più piccolo
4. **J4 — Polso (Roll o Pitch):** Da aggiungere dopo, opzionale

**Alternative alla struttura tradizionale:**
- **Link in alluminio sagomato + attacchi stampati** — più rigido ma meno "tutto stampato"
- **Braccio con struttura a traliccio aperto** — massimo risparmio peso, stile esoscheletro
- **Tubi in carbonio o alluminio con giunti stampati** — compromesso eccellente tra peso e rigidezza (usato da molti progetti professionali)

### Tabella Riepilogativa

| Approccio | Peso | Rigidezza | Stampa 3D | Complessità |
|-----------|------|-----------|-----------|-------------|
| Tutto PLA massiccio | Alto | Media | Facile | Bassa |
| Struttura ottimizzata FEA (tipo Forte) | Basso | Alta | Media | Alta |
| Petalo/traliccio aperto | Basso | Bassa | Facile | Media |
| Tubi + giunti stampati | Molto basso | Molto alta | Solo giunti | Media |
| **Consigliato: segmenti a U rinforzati** | **Medio-basso** | **Alta** | **Media** | **Medio-bassa** |

### Source da Ingestire
- https://github.com/AngelLM/Thor — struttura di riferimento
- https://arxiv.org/abs/2507.15693 — paper Forte (design ottimizzato)
- Progetto CyBot — reference per cycloidal + NEMA 17
- Tutorial: "Design of 3D Printed Robot Arm Structures" su YouTube

## Related
- [[cycloidal-drive]] — Riduttore in uso
- [[nema-17]] — Motori
- [[salvatore-robot-arm]] — Pagina progetto
