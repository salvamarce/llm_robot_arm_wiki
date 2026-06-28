---
title: NEMA 17
aliases: [nema-17, NEMA17, motore passo-passo, stepper motor, 17HS series, 42mm stepper]
created: 2026-06-15
updated: 2026-06-28
type: entity
tags: [stepper-motor, nema-17, mechanics, torque, beginner]
confidence: high
---

# NEMA 17

Motore passo-passo standard NEMA 17 (dimensione flangia 1.7" × 1.7" / 42mm × 42mm). Ampiamente usato nella robotica DIY, stampanti 3D, e CNC.

## Specifiche Tipiche

| Parametro | Valore |
|-----------|--------|
| Dimensione flangia | 42 × 42 mm (NEMA 17) |
| Lunghezza | Variabile (20–48 mm comuni) |
| Angolo passo | 1.8° (200 passi/giro) |
| Corrente | 0.5–2.0 A per fase (tipico) |
| Coppia | 0.2–0.6 Nm (dipende da lunghezza e corrente) |
| Tensione | 2.5–4.5 V (nom.), 12–24 V (driver) |

## Varianti Comuni

- **17HS3401** — 0.35 Nm, corto
- **17HS4401** — 0.4 Nm, medio
- **17HS8401** — 0.5 Nm, lungo

## Uso in Robotica DIY

- Ideali per bracci robotici leggeri e desk-top
- Richiedono riduttori ([[cycloidal-drive]]) per aumentare coppia utile
- Controllo con microstepping per ridurre vibrazioni e migliorare risoluzione
- Possono essere accoppiati a encoder per controllo in anello chiuso

## Pro: e Contro:

**Pro:**
- Economici e facilmente reperibili
- Ben supportati da driver e librerie
- Coppia elevata a basse velocità
- Nessuna spazzola, nessuna manutenzione

**Contro:**
- Rumorosi a media-alta velocità
- Risonanza a certe frequenze (microstepping aiuta)
- Consumo corrente anche a fermo
- Coppia cala rapidamente all'aumentare della velocità

## Related
- [[stepper-motor-control]]
- Moduli driver: TMC2209, TMC5160, A4988, DRV8825
- [[cycloidal-drive]]
