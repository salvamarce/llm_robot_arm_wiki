---
title: Braccio Robotico DIY di Salvatore
aliases: [salvatore-robot-arm, robot arm, braccio robotico, Salvatore Robot Arm, braccio DIY, 4-DOF arm]
created: 2026-06-15
updated: 2026-06-30
type: project
tags: [in-progress, arduino, stepper-motor, nema-17, cycloidal-drive, 3d-printing, 4-dof, closed-loop, can-bus, shoulder-joint]
confidence: high
---

# Braccio Robotico DIY di Salvatore

Progetto personale di braccio robotico fai-da-te con stampa 3D e motori passo-passo NEMA 17 in anello chiuso su CAN bus.

## Stato Attuale

- **Fase:** Progettazione riduttore cycloidal J2 (spalla) — 20:1
- **Motori:** 4× NEMA 17 (2 lunghi, 2 corti)
- **Riduttori:** Cycloidal drive **20:1**, due dischi eccentrici sfasati 180° (design originale)
- **Controllo:** MKS SERVO42D closed-loop FOC su CAN bus — libreria Arduino sviluppata
- **DOF:** 4

## Specifiche di Progetto

| Parametro | Valore |
|---|---|
| **Payload target** | 500 g |
| **Sbraccio target** | 400–450 mm |
| **DOF** | 4 (base + spalla + gomito + polso) |
| **Riduttore J2 (spalla)** | Cycloidal **20:1**, 2 dischi sfasati, PETG |
| **Rulli corona** | 21× bearing steel Ø4×10 mm, HRC 58-62 |
| **Eccentricità** | **1.0 mm** |
| **Pitch radius rulli** | **32 mm** |
| **Perni output** | 6× tubo alluminio Ø8×6 mm, M4 passante |
| **Cuscinetti eccentrici** | 2× 6801-ZZ (12×21×5) |
| **Efficienza riduttore** | ~70-75% (con rulli acciaio rotanti) |
| **Torque output spalla** | **~7.5 Nm** (0.50 Nm × 20 × 0.75) |
| **Motori** | NEMA 17 (2× lunghi ~0.50 Nm, 2× corti ~0.35 Nm) |
| **Driver** | [[mks-servo42d]] — FOC closed-loop, 4A max, encoder 16384 cpr |
| **Bus** | CAN 500 kbps, 2 fili per tutti i motori |
| **Struttura** | Segmenti a U in PETG, stampa 3D |
| **Hardware** | Viti M3/M4, dadi, inserti filettati, cuscinetti 6801-ZZ |

## Assegnazione Motori e Coppie (20:1, 75% efficienza)

| Giunto | Motore | Rapporto | Coppia uscita | Carico statico | Safety factor |
|---|---|---|---|---|---|
| **J1 (base)** | NEMA 17 *corto* | da definire | — | ~1–2 Nm | — |
| **J2 (spalla)** | NEMA 17 *lungo* | **20:1** | **~7.5 Nm** | ~3.4 Nm | **2.2×** ✅ |
| **J3 (gomito)** | NEMA 17 *lungo* | da definire | — | ~3.0 Nm | — |
| **J4 (polso)** | NEMA 17 *corto* | da definire | — | ~1.2 Nm | — |

## Velocità Stimate (20:1)

| RPM motore | RPM giunto | Velocità angolare | Velocità in punta a 450mm |
|---|---|---|---|
| 120 | 6 | 36°/s | ~280 mm/s |
| **200** | **10** | **60°/s** | **~470 mm/s** — target operativo |
| 400 | 20 | 120°/s | ~940 mm/s |

Risoluzione: 200 step × 20 = 4000 passi/giro output; con microstepping 1/16 → 64000 passi/giro ≈ 0.0056°/passo.

## Materiali

| Componente | Materiale | Motivazione |
|---|---|---|
| Struttura portante (braccio) | PETG | Più rigido del PLA, resistente al creep |
| Dischi cicloidali | PETG | Tolleranze critiche — materiale stabile |
| Corona esterna | PETG + inserti Al (o solo PETG) | Da decidere |
| Giunti e mozzi | PETG | Resistenza meccanica |
| Piedini e guarnizioni | TPU | Antivibranti, ammortizzazione |
| Prototipi/Test | PLA+ | Economico e facile da stampare |

## Roadmap

1. ✅ Progettazione riduttore cycloidal J2 (20:1)
2. ✅ Parametri definiti: R=32, E=1.0, 21 rulli Ø4×10 bearing steel
3. ✅ Componenti acquistati: rulli acciaio (sourcing map), cuscinetti 6801-ZZ
4. ⬜ Generazione CAD in Fusion 360 via script MCP
5. ⬜ Stampa e assemblaggio riduttore J2
6. ⬜ Progettazione riduttori J1, J3, J4
7. ⬜ Progettazione struttura braccio (4 DOF, ~400-450mm)
8. ⬜ Stampa e assemblaggio struttura
9. ⬜ Cablaggio CAN bus e alimentazione 24V
10. ⬜ Firmware e cinematica (libreria MKS_SERVO42D pronta)
11. ⬜ Calibrazione e test
12. ⬜ Validazione payload 500g

## Componenti

- [[nema-17]] — Motori passo-passo: 2 lunghi (J2, J3) + 2 corti (J1, J4)
- [[cycloidal-drive]] — Riduttori cicloidali, specifica J2: 20:1, R=32, E=1.0, 2 dischi
- [[mks-servo42d]] — Driver closed-loop FOC CAN bus + libreria Arduino

## Related
- [[stepper-motor-control]]
- [MKS_SERVO42D library (GitHub)](https://github.com/salvamarce/MKS_SERVO42D)
