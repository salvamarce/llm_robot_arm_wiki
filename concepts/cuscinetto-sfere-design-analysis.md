---
title: Analisi Design Cuscinetto a Sfere (Fusion 360)
created: 2026-06-22
updated: 2026-06-26
type: concept
tags: [bearings, cad, fusion-360, design-analysis, bearing-v10, ball-bearing]
confidence: high
---

# Analisi Design Cuscinetto a Sfere (Fusion 360)

Analisi dimensionale e geometrica del file **bearing v10** su Fusion 360, una gabbia/retainer per cuscinetto a sfere.

## Sfere reali acquistate (2026-06-26)

| Specifica | Valore |
|---|---|
| Prodotto | ADCSHOP 1500 Steel Balls Gauge 4.5 mm |
| Diametro | **4.5 mm** (nominale) |
| Materiale | Alloy steel |
| Tolleranza | ±0.05-0.1 mm (pallini soft air, NON qualità cuscinetto) |
| Peso | ~0.25 g cad. |

**NOTA:** Queste sono pallini per aria compressa, non sfere per cuscinetti di precisione G25/G200. La tolleranza dimensionale è molto più larga e la rotondità non è specificata.

## Aggiornamento analisi (2026-06-26) — Sfere 4.5 mm

Le sfere acquistate sono **4.5 mm** → il parametro `d_ball = 4.5 mm` nel design è **corretto**. Il falso allarme dell'analisi precedente (che ipotizzava 4 mm) era dovuto a info incomplete.

### ⚠️ Problemi reali che emergono coi dati corretti

#### 1. La corona NON è un cuscinetto completo — è una gabbia (retainer)

| Parametro | Valore | Problema |
|---|---|---|
| OD corona | 9.2 mm | R = 4.6 mm |
| ID corona | 8.0 mm | R = 4.0 mm |
| Parete radiale | **0.6 mm** | Più sottile del raggio sfera (2.25 mm) |
| Centro tasca ~R 4.2 | | Sfera sporge **oltre OD** (R 6.45 vs R 4.6) e **oltre ID** (R 1.95 vs R 4.0) |

Conclusione: **i due anelli di rotolamento (piste interna/esterna) non sono modellati in questo file.** La corona in Fusion 360 è solo il retainer/gabbia che mantiene le sfere spaziate. Le piste sono verosimilmente ricavate nei bracci del robot o in altri componenti separati.

#### 2. 26 tasche con sfere da 4.5 mm

- PCD gabbia = ~8.6 mm (tra ID 8.0 e OD 9.2)
- Circonferenza gabbia = π × 8.6 = **27.0 mm**
- 26 × 4.5 mm = **117 mm** di spazio lineare richiesto
- Rapporto: **4.3× la circonferenza disponibile**

26 sfere da 4.5 mm NON possono stare su una gabbia di 9.2 mm OD. Il PCD reale delle sfere nel cuscinetto assemblato deve essere **almeno 40 mm** (Dp = 26 × 4.5 / π + spaziatura). La gabbia in Fusion è probabilmente solo un inserto centrale di un retainer molto più grande.

#### 3. Qualità delle sfere

Le ADCSHOP 4.5 mm sono **pallini per soft air**, NON sfere per cuscinetti:

| Proprietà | BB soft air | Cuscinetto G25/G200 |
|---|---|---|
| Tolleranza diametro | ±0.05-0.1 mm | ±0.0025 mm (G25) |
| Rotondità | Non specificata | 0.00025 mm (G25) |
| Durezza | Acciaio dolce | HRC 60-66 (100Cr6) |
| Materiale | Alloy steel (generico) | Acciaio al cromo |

Con `d_ball_toll = 0.1 mm` e sfere con ±0.1 mm di variazione, **alcune tasche saranno a zero gioco e altre avranno gioco eccessivo**. Per un braccio robotico lento (<30 RPM) probabilmente funziona comunque, ma non aspettarti rotazione fluida.

### Calcolo PCD reale per 26 sfere da 4.5 mm

Ipotesi: spaziatura tra sfere ≈ 10% del diametro (tipico per gabbie stampate 3D)

- Spazio per sfera + spaziatura = 4.5 × 1.1 = **4.95 mm**
- Circonferenza primitiva = 26 × 4.95 = **128.7 mm**
- **PCD = 128.7 / π ≈ 41.0 mm**
- Raggio primitivo ≈ **20.5 mm**

Le piste del cuscinetto (anelli esterno/interno) devono avere diametri approssimativi:
- **Anello esterno ID ≈ PCD + d_ball = 41 + 4.5 = 45.5 mm**
- **Anello interno OD ≈ PCD - d_ball = 41 - 4.5 = 36.5 mm**

Questi sono i veri diametri del cuscinetto assemblato, molto più grandi della gabbia di 9.2 mm vista in Fusion.

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

## Altre considerazioni geometriche (valide per 4.5 mm)

La gabbia (Corpo2) è **molto più piccola delle dimensioni del cuscinetto completo**:
- **OD gabbia = 9.2 mm**, **ID gabbia = 8.0 mm** → parete radiale di soli **0.6 mm**
- Una sfera da 4.5 mm ha raggio 2.25 mm — la parete è 4× più sottile del raggio della sfera
- Se la tasca è centrata a R≈4.2 mm, la sfera sporge **oltre il diametro esterno** (R4.2 + 2.25 = R6.45, ma l'OD è R4.6) e oltre il diametro interno (R1.95 vs R4.0)
- **Confermato: è una gabbia, non una pista**

## Note per revisione

- `d_ball = 4.5 mm` è **corretto** — nessuna modifica necessaria
- `d_ball_toll = 0.1 mm` è adeguato per gabbia stampata 3D, ma le BB in acciaio dolce potrebbero avere variazione dimensionale comparabile — monitorare usura
- Verificare che il PCD reale del cuscinetto assemblato sia ≥ 40 mm per 26 sfere da 4.5 mm
- Considerare sfere per cuscinetti vere (G25-G200) per applicazioni che richiedono rotazione fluida o carichi assiali significativi

## Related
- [[analisi-cad-con-hermes]] — Workflow di analisi CAD via Fusion MCP
- [[cycloidal-drive]] — Riduttore cycloidal che potrebbe usare cuscinetti simili
- [[salvatore-robot-arm]] — Progetto braccio robotico
