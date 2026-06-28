---
title: Controllo Motori Passo-Passo
created: 2026-06-28
updated: 2026-06-28
type: concept
tags: [stepper-motor, control, firmware, motion-control, pid, acceleration, microstepping]
confidence: high
aliases: [stepper-motor-control, Stepper Motor Control, controllo stepper, motion control]
---

# Controllo Motori Passo-Passo

Strategie e tecniche per il controllo di motori passo-passo in applicazioni robotiche, con focus sul [[salvatore-robot-arm]].

## Microstepping

Tecnica che suddivide ogni passo completo in sotto-passi più piccoli:

| Divisione | Passi/giro (1.8°) | Angolo/passo |
|-----------|-------------------|--------------|
| Full step | 200 | 1.8° |
| 1/2 | 400 | 0.9° |
| 1/4 | 800 | 0.45° |
| 1/8 | 1600 | 0.225° |
| 1/16 | 3200 | 0.1125° |
| 1/32 | 6400 | 0.05625° |

Con [[cycloidal-drive]] 25:1 e microstepping 1/16: **80.000 passi/giro in uscita ≈ 0.0045°/passo**.

## Closed-Loop Control

I driver [[mks-servo42d]] implementano **closed-loop FOC**:

- **Encoder 16384 cpr** → rileva ogni deviazione dalla posizione comandata
- **Correzione in tempo reale** → nessun passo perso, anche sotto carico
- **Stall detection** → segnalazione se il carico supera la coppia massima
- **FOC (Field Oriented Control)** → coppia ottimale a tutte le velocità

### Loop di controllo interno

```
Posizione target → PID Position → PID Velocity → FOC Current → Motore
                                        ↑                        |
                                        └── Encoder 16384 cpr ←──┘
```

## Acceleration Profiling

Per bracci robotici, l'accelerazione graduale è fondamentale:

- **Accelerazione trapezoidale** — standard, facile da implementare
- **Accelerazione S-curve** — più fluida, riduce vibrazioni meccaniche
- **Accelerazione variabile per giunto** — profili diversi per base, spalla, polso

## CAN Bus Control

Tutti i giunti comunicano su un [[mks-servo42d|bus CAN singolo 500 kbps]]:

- **Comandi broadcast** — tutti i motori simultaneamente
- **Comandi individuali** — per giunto specifico (0x01-0x04)
- **Sincronizzazione** — movimento coordinato tra giunti

## Gestione della Coppia

Coppia nominale dei motori [[nema-17]] con riduttori [[cycloidal-drive]]:

| Giunto | Motore | Coppia alla mass | Note |
|--------|--------|-----------------|------|
| J1 (base) | NEMA 17 corto | 6.6 Nm | Rotazione verticale, carico minimo |
| J2 (spalla) | NEMA 17 lungo | 9.4 Nm | **Maggiore carico gravitazionale** |
| J3 (gomito) | NEMA 17 lungo | 9.4 Nm | Carico medio |
| J4 (polso) | NEMA 17 corto | 6.6 Nm | Carico minimo |

## Considerazioni per Stampa 3D

- **PID anti-backlash** — compensa gioco meccanico dei riduttori stampati
- **Feed-forward** — anticipa coppia richiesta per gravità (gravity compensation)
- **TORQUE_MODE** — utile per rilevare collisioni o carichi eccessivi

## Related

- [[nema-17]] — Motori utilizzati
- [[mks-servo42d]] — Driver closed-loop FOC CAN bus
- [[cycloidal-drive]] — Riduttori
- [[salvatore-robot-arm]] — Progetto braccio robotico
