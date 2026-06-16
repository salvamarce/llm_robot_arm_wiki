---
title: Cycloidal Drive
created: 2026-06-15
updated: 2026-06-15
type: concept
tags: [cycloidal-drive, reducer, gearbox, 3d-printing, mechanics, torque, intermediate]
confidence: high
---

# Cycloidal Drive

Riduttore epicicloidale a disco cycloidale. Usa un disco eccentricamente montato che rotola all'interno di una corona di perni, producendo un rapporto di riduzione alto con gioco ridotto e coppia elevata.

## Principio di Funzionamento

1. Un disco con profilo a cicloide è montato su un eccentrico sull'albero di ingresso
2. Il disco ruota all'interno di una corona fissa di rulli/perni
3. Il movimento cycloidale del disco viene convertito in rotazione dell'albero di uscita tramite perni di trasmissione
4. Rapporto di riduzione: tipicamente 10:1 a 100:1 per stadio

## Vantaggi per Robotica DIY

- **Rapporto alto in ingombro ridotto** — 30:1 in un disco spesso 10 mm
- **Gioco (backlash) minimo** — grazie al contatto multiplo dei rulli
- **Coppia elevata** — molti denti in presa contemporaneamente
- **Stampa 3D friendly** — geometria realizzabile in PLA/PETG/ABS
- **Assorbimento urti** — buona tolleranza a picchi di carico

## Variante a Due Dischi (Salvatore)

Progettazione con **due dischi centrici sfasati** per bilanciamento dinamico:

- Disco 1 e Disco 2 montati a 180° di fase
- Le masse eccentriche si compensano reciprocamente
- **Riduzione vibrazioni** rispetto al singolo disco
- Coppia trasmessa da entrambi i dischi — ridondanza e maggiore robustezza
- Assemblaggio più complesso ma risultato più silenzioso e fluido

## Design Parameters

| Parametro | Considerazione |
|-----------|---------------|
| Rapporto | Determina coppia in uscita e velocità massima |
| Eccentricità | Maggiore eccentricità = più coppia ma più vibrazioni |
| Diametro rulli | Influenza gioco e capacità di carico |
| Materiale | PLA/PETG per prototipi, ABS/Polycarbonate per uso continuativo |
| Tolleranze | Critiche — troppo gioco = backlash, troppo stretto = grippaggio |

## Progettazione e Stampa

- File STL/STEP da generare con strumenti parametrici (es. Cycloidal Gear Generator online, o script Python)
- Post-processing: fori calibrati, levigatura superfici di contatto
- Lubrificazione: grasso al litio o PTFE per ridurre attrito PLA-PLA

## Related
- [[nema-17]] — motori tipici abbinate a cycloidal drive
- [[salvatore-robot-arm]] — progetto che usa questa variante a due dischi
- Concept: rapporto di riduzione, coppia, backlash, eccentricità, bilanciamento dinamico
