---
title: Analisi Design Cuscinetto a Sfere (Fusion 360)
created: 2026-06-22
updated: 2026-06-22
type: concept
tags: [bearings, cad, fusion-360, design-analysis, bearing-v10, ball-bearing]
confidence: high
---

# Analisi Design Cuscinetto a Sfere (Fusion 360)

Analisi dimensionale e geometrica del file **bearing v10** su Fusion 360, una corona/retainer per cuscinetto a sfere progettata per sfere metalliche da **4 mm**.

## Parametri attuali (Fusion 360)

| Parametro | Valore |
|---|---|
| `d_ball` | **4.5 mm** |
| `d_ball_toll` (gioco) | 0.1 mm |
| Pattern circolare | **26 tasche** su 360° |
| Nome file | bearing v10 |

## I 3 corpi identificati

### Corpo2 — Anello principale (la corona)
- **OD:** 9.2 mm (R=4.6 mm)
- **ID:** 8.0 mm (R=4.0 mm)
- **Spessore:** 2.0 mm (da z=-1 a z=+1)
- Centro all'origine

### Corpo3 — Tasche per le sfere (186 facce)
- 26 facce sferiche, 52 toroidali, 28 cilindriche, 53 coniche, 27 piane
- Si estende in z da 0.149 a 0.760 mm
- Raggio superfici sferiche residue nel pocket: **0.2375 mm** (micro-dettaglio del taglio, non raggio tasca principale)
- Bordo circolare principale: **R 3.95 mm**

### Corpo1 — Rondella/feature secondaria
- Dimensione: 7.9 × 1.0 mm, z=0..1

## Sequenza costruttiva (timeline Fusion 360)

1. **Rivoluzione1** → profilo base
2. **Rivoluzione2** → anello principale (Corpo2)
3. **PrimitivaSfera1** → crea una sfera
4. **Allinea1** → posiziona la sfera
5. **Combina1 (taglio)** → sottrae la sfera dall'anello → crea la prima tasca
6. **Rivoluzione3** → dettaglio
7. **Serie C1 (26 copie, 360°)** → replica le tasche
8. **Specchio3** → specchia
9. **Rivoluzione4,5** → dettagli finali

## ⚠️ Problema principale: diametro sfera

L'utente ha confermato **sfere da 4 mm**, ma il parametro nel design è **`d_ball = 4.5 mm`**.

| Cosa | Sta | Dovrebbe (per 4 mm) |
|---|---|---|
| `d_ball` | **4.5 mm** | 4.0 mm |
| `d_ball_toll` | 0.1 mm | 0.1-0.15 mm (ok) |
| OD corona | 9.2 mm | Da verificare con contesto |
| Numero sfere | 26 | Dipende dal diametro primitivo |

**Impatto:**
- Con 4.5 mm: gioco = 0.1 mm (corretto)
- Con 4 mm dentro tasche da 4.5 mm: gioco = **0.6 mm** — le sfere ballano

### Altre considerazioni geometriche

L'anello è **molto piccolo** per sfere da 4 o 4.5 mm:
- **OD = 9.2 mm**, **ID = 8.0 mm** → parete radiale di soli **0.6 mm**
- Una sfera da 4.5 mm ha raggio 2.25 mm — la parete è 4× più sottile del raggio della sfera
- Se la tasca è centrata a R≈4.2 mm, la sfera sporge **oltre il diametro esterno** (R4.2 + 2.25 = R6.45, ma l'OD è R4.6)

### Possibili interpretazioni

1. **Corpo2 non è l'anello completo** — è solo la **gabbia (retainer)** e gli anelli interno/esterno sono file separati o non ancora modellati
2. **Le dimensioni sono fuori scala** — per sfere da 4 mm ci si aspetterebbe un OD di almeno 16-22 mm
3. **È un cuscinetto in miniatura** — esistono cuscinetti con sfere da 4 mm e OD~12-16 mm, ma 9.2 mm è comunque molto stretto

## Note per revisione

- Correggere `d_ball` da 4.5 mm → **4.0 mm** per matchare le sfere reali
- Dopo la correzione, verificare che `d_ball_toll` sia ancora adeguato (0.1-0.15 mm)
- Valutare se la corona completa include anche anelli interno/esterno separati

## Related
- [[analisi-cad-con-hermes]] — Workflow di analisi CAD via Fusion MCP
- [[cycloidal-drive]] — Riduttore cycloidal che potrebbe usare cuscinetti simili
- [[salvatore-robot-arm]] — Progetto braccio robotico
