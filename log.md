# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete

## [2026-06-15] create | Wiki initialized
- Domain: DIY Robotic Arm (braccio robotico fai-da-te)
- Structure created with SCHEMA.md, index.md, log.md
- Categories: entities, concepts, components, comparisons, projects, queries
- Raw sources: articles, papers, transcripts, assets

## [2026-06-15] create | Progetto Salvatore, NEMA 17, Cycloidal Drive
- Created projects/salvatore-robot-arm.md — stato attuale, specifiche, roadmap
- Created entities/nema-17.md — specifiche motore, pro/contro
- Created concepts/cycloidal-drive.md — principio, variante a due dischi sfasati
- Updated index.md with 3 pages

## [2026-06-15] create | Confronto strutture leggere + update progetto
- Created comparisons/confronto-strutture-leggere.md — analisi THOR, Forte, CyBot, Skyentific
- Updated projects/salvatore-robot-arm.md — materiali (PLA/PETG/TPU) e specifiche dettagliate
- Updated index.md with 4 pages total

## [2026-06-15] create | Analisi CAD con Hermes
- Created concepts/analisi-cad-con-hermes.md — Fusion MCP vs trimesh, setup LAN, roadmap Automation MCP cloud
- Updated index.md with 5 pages total

## [2026-06-22] create | Analisi cuscinetto a sfere (bearing v10)
- Created concepts/cuscinetto-sfere-design-analysis.md — analisi dimensionale da Fusion 360: parametri, 3 corpi, sequenza costruttiva, problema d_ball 4.5mm vs sfere reali 4mm
- Updated index.md with 6 pages total

## [2026-06-28] obsidian | Convertito wiki in Obsidian vault
- Added `.obsidian/` config: app.json, appearance.json, core-plugins.json, graph.json, community-plugins.json, hotkeys.json, types.json
- Created `concepts/stepper-motor-control.md` — pagina mancante su controllo motori
- Added `aliases` in frontmatter di tutte le pagine per linking flessibile
- Rewritten `index.md` come home page vault con tabelle navigabili
- Updated SCHEMA.md: aggiunta convenzione aliases
- Updated .gitignore: esclusi workspace/cache di Obsidian
- **Vault pronto:** aprilo in Obsidian per vedere il grafo completo

## [2026-06-26] update | Rianalisi cuscinetto con sfere reali
- Aggiornata analisi: sfere ADCSHOP 4.5 mm confermate → `d_ball` CORRETTO
- Rimosso falso allarme 4 mm vs 4.5 mm
- Aggiunta sezione: la corona è una gabbia (retainer), non pista di rotolamento
- Aggiunto calcolo PCD reale per 26 sfere da 4.5 mm (~41 mm)
- Aggiunta nota qualità BB vs sfere cuscinetto
