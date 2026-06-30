---
title: Cycloidal Drive — Progetto Spalla
aliases: [cycloidal-drive, riduttore cycloidal, cycloidal gearbox, riduttore epicicloidale, riduttore a disco, two-disk cycloidal]
created: 2026-06-15
updated: 2026-06-30
type: concept
tags: [cycloidal-drive, reducer, gearbox, 3d-printing, mechanics, torque, intermediate, shoulder-joint, 20-1]
confidence: high
---

# Cycloidal Drive — Riduttore per Giunto di Spalla

Riduttore cicloidale 20:1 progettato per il giunto **J2 (spalla)** del braccio robotico. Variante a due dischi eccentrici sfasati 180° per bilanciamento dinamico.

## Specifiche di Progetto

| Parametro | Valore | Note |
|-----------|--------|------|
| **Rapporto** | **20:1** | Z<sub>c</sub> = 20 lobi, Z<sub>r</sub> = 21 rulli |
| **Eccentricità (E)** | **1.0 mm** | Hole perni output = D<sub>pin</sub> + 2×E = 10 mm |
| **Pitch radius rulli (R)** | **32 mm** | Corona OD ≈ 76 mm |
| **Raggio rulli (Rr)** | **2 mm** | Rulli in acciaio Ø4×10 mm |
| **N. rulli corona** | **21** | In acciaio per cuscinetti (bearing steel, HRC 58-62) |
| **N. perni output** | **6** | Tubo alluminio Ø8×6 mm, M4 passante |
| **N. dischi** | **2** | Sfasati 180°, spessore 5 mm ciascuno |
| **Cuscinetti eccentrici** | **2× 6801-ZZ** | 12×21×5 mm |
| **Albero motore** | **Ø5 mm** | NEMA 17, cilindrico senza spianata |
| **Bloccaggio albero** | **Morsetto split** | 2× viti M3 |
| **Materiale dischi** | PETG | Stampato 3D |
| **Materiale corona** | PETG + inserti Al Ø8 | Oppure solo PETG (cupole stampate) |
| **Efficienza stimata** | ~70-75% | Con rulli acciaio rotanti |
| **Torque output** | ~7.5 Nm | Con NEMA 17 lungo (0.50 Nm × 20 × 0.75) |

## Parametri Cinematici

### Equazioni del profilo cicloide

```
Parametri:
  N = 21         (numero rulli corona)
  R = 32 mm      (pitch circle radius rulli)
  Rr = 2 mm      (raggio rullo = Ø4/2)
  E = 1.0 mm     (eccentricità)

ψ(t) = atan2(sin((1-N)·t), (R/(E·N)) - cos((1-N)·t))

X(t) = R·cos(t) - Rr·cos(t + ψ(t)) - E·cos(N·t)
Y(t) = -R·sin(t) + Rr·sin(t + ψ(t)) + E·sin(N·t)

t ∈ [0, 2π)
```

Verifica: R/(E·N) = 32/(1.0×21) = **1.52 > 1** ✅ profilo valido (nessun cuspide).

## Dimensioni del Riduttore

```
                  ┌──────────────────┐
     76 mm OD ←───┤  Corona esterna  │
                  │  (PETG stampato)  │
                  │   ┌─────────┐    │
                  │   │ Dischi  │    │  ← 26 mm spessore totale
                  │   │ 5+5 mm  │    │    (base 16 + dischi + piastra)
                  │   └─────────┘    │
                  │  6× perni Al Ø8  │
                  └──────────────────┘
                  NEMA 17 footprint 42×42 mm
```

## Componenti Acquistati / Reperiti

| Componente | Specifica | Fonte | Costo |
|---|---|---|---|
| Rulli acciaio | Bearing steel Ø4×10 mm, 100 pz | Amazon.it (sourcing map) | ~€14 |
| Cuscinetti eccentrici | 6801-ZZ (12×21×5) | Amazon.it | ~€5 cad. |
| Perni output alluminio | Tubo Ø8×6 mm, profilato Leroy Merlin | Già tagliati (6 pz) | €3 |
| Viti M4 passante | Per perni output e rulli corona | Già possedute | — |
| Viti M3 morsetto | Per bloccaggio albero motore | Da acquistare | ~€3 |
| Albero motore | NEMA 17 Ø5 cilindrico | In dotazione col motore | — |

## Relazione con Altri Giunti

| Giunto | Rapporto | Motore | Note |
|---|---|---|---|
| **J2 (spalla)** | **20:1** | NEMA 17 lungo | **Questo progetto** |
| J3 (gomito) | da definire | NEMA 17 lungo | Rapporto diverso (carico minore) |
| J1 (base) | da definire | NEMA 17 corto | Asse verticale |
| J4 (polso) | da definire | NEMA 17 corto | Carico minimo |

## Prossimi Passi

1. ⬜ Generare script parametrico Python per Fusion 360 via MCP
2. ⬜ Creare dischi cicloidali + corona in Fusion
3. ⬜ Verificare interferenze con simulazione
4. ⬜ Stampare prototipo e testare

## Related

- [[salvatore-robot-arm]] — Progetto braccio completo
- [[nema-17]] — Motori passo-passo
- [[mks-servo42d]] — Driver closed-loop
