---
title: Braccio Robotico DIY di Salvatore
created: 2026-06-15
updated: 2026-06-16
type: project
tags: [in-progress, arduino, stepper-motor, nema-17, cycloidal-drive, 3d-printing, 4-dof, closed-loop, can-bus]
confidence: high
---

# Braccio Robotico DIY di Salvatore

Progetto personale di braccio robotico fai-da-te con stampa 3D e motori passo-passo NEMA 17 in anello chiuso su CAN bus.

## Stato Attuale

- **Fase:** Assemblaggio riduttore cycloidal
- **Motori:** 4× NEMA 17 (2 lunghi, 2 corti)
- **Riduttori:** Cycloidal drive 25:1, due dischi centrici sfasati (design originale)
- **Controllo:** MKS SERVO42D closed-loop FOC su CAN bus — libreria Arduino sviluppata
- **DOF:** 4

## Specifiche di Progetto

| Parametro | Valore |
|---|---|
| **Payload target** | 500 g |
| **Sbraccio target** | 400–450 mm |
| **DOF** | 4 (base + spalla + gomito + polso) |
| **Riduttore** | Cycloidal 25:1, 2 dischi sfasati, stampato in PETG/PLA+ |
| **Efficienza riduttore** | ~75% (stima, con grasso al litio) |
| **Motori** | NEMA 17 (2× lunghi ~0.50 Nm, 2× corti ~0.35 Nm) |
| **Driver** | [[mks-servo42d]] — FOC closed-loop, 4A max, encoder 16384 cpr |
| **Bus** | CAN 500 kbps, 2 fili per tutti i motori |
| **Struttura** | Segmenti a U in PETG, stampa 3D |
| **Hardware** | Viti M3/M4, dadi, inserti filettati, cuscinetti 608ZZ |

## Assegnazione Motori e Coppie (25:1, 75% efficienza)

| Giunto | Motore | Coppia nominale | Coppia uscita giunto | Carico statico a 450mm |
|---|---|---|---|---|
| **J1 (base)** | NEMA 17 *corto* | 0.35 Nm | **6.6 Nm** | ~1–2 Nm dinamico (asse verticale) |
| **J2 (spalla)** | NEMA 17 *lungo* | 0.50 Nm | **9.4 Nm** | ~5.5 Nm |
| **J3 (gomito)** | NEMA 17 *lungo* | 0.50 Nm | **9.4 Nm** | ~3.0 Nm |
| **J4 (polso)** | NEMA 17 *corto* | 0.35 Nm | **6.6 Nm** | ~1.2 Nm |

- **J1 ha il carico più basso** perché ruota su asse verticale (parallelo a gravità) — solo inerzia rotazionale, nessun sollevamento.
- J2 e J3 combattono la gravità su tutto il braccio → motori lunghi.
- J4 margine enorme, motore corto più che sufficiente.
- **Margine minimo sulla spalla** (J2): +70% a 450mm con 500g. A 500mm si sale al 73% — strutturalmente sconsigliato in PETG.

## Velocità Stimate (25:1)

| RPM motore | RPM giunto | Velocità in punta a 400mm |
|---|---|---|
| 150 | 6 (36°/s) | ~250 mm/s |
| 300 | 12 (72°/s) | ~500 mm/s — target operativo |
| 600 | 24 (144°/s) | ~1 m/s |

Risoluzione: 200 step × 25 = 5000 passi/giro output; con microstepping 1/16 → 80000 passi/giro ≈ 0.0045°/passo.

## Materiali

| Componente | Materiale | Motivazione |
|---|---|---|
| Struttura portante (braccio) | PETG | Più rigido del PLA, resistente al creep |
| Riduttore cycloidal | PETG o PLA+ | Tolleranze critiche — materiale stabile |
| Giunti e mozzi | PETG | Resistenza meccanica |
| Piedini e guarnizioni | TPU | Antivibranti, ammortizzazione |
| Prototipi/Test | PLA+ | Economico e facile da stampare |

## Roadmap

1. ✅ Progettazione e stampa riduttore cycloidal (2 dischi, 25:1)
2. 🔄 Assemblaggio e rifinitura riduttore
3. ⬜ Progettazione struttura braccio (4 DOF, ~400-450mm)
4. ⬜ Stampa e assemblaggio struttura
5. ⬜ Cablaggio CAN bus e alimentazione 24V
6. ⬜ Firmware e cinematica (libreria MKS_SERVO42D pronta)
7. ⬜ Calibrazione e test
8. ⬜ Validazione payload 500g

## Componenti

- [[nema-17]] — Motori passo-passo: 2 lunghi (J2, J3) + 2 corti (J1, J4)
- [[cycloidal-drive]] — Riduttori 25:1 a due dischi sfasati
- [[mks-servo42d]] — Driver closed-loop FOC CAN bus + libreria Arduino

## Related
- [[stepper-motor-control]]
- [MKS_SERVO42D library (GitHub)](https://github.com/salvamarce/MKS_SERVO42D)
