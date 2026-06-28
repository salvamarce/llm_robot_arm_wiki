# Wiki Schema

## Domain
DIY Robotic Arm — costruzione, progettazione e programmazione di bracci robotici fai-da-te. Include componenti meccanici, elettronici, firmware, software di controllo, cinematica, e progetti completi.

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `stepper-motor-control.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- Add `aliases: [nome-alias1, nome-alias2]` in frontmatter per nomi alternativi (plurale, inglese/italiano, abbreviazioni)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- Language: prefer italiano per i contenuti, ma mantieni termini tecnici in inglese quando sono standard (es. "forward kinematics", "PID controller", "end-effector")
- **Provenance markers:** On pages that synthesize 3+ sources, append `^[raw/articles/source-file.md]` markers at paragraphs whose claims trace to a specific source

## Frontmatter
  ```yaml
  ---
  title: Page Title
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  type: entity | concept | comparison | query | summary | component | project
  tags: [from taxonomy below]
  sources: [raw/articles/source-name.md]
  confidence: high | medium | low
  contested: true
  ---
  ```

### raw/ Frontmatter
```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: <hex digest of raw content below frontmatter>
---
```

## Tag Taxonomy

Add new tags here BEFORE using them.

### By Category
- **Mechanics:** 3d-printing, filament, abs, pla, petg, aluminum, acrylic, bearings, joints, linkage, timing-belt, leadscrew, pulley, gearbox, frame, base, mounting
- **Motors:** stepper-motor, servo-motor, blcd-motor, dynamixel, continuous-rotation, encoder, gear-ratio, torque, rpm, stall-torque
- **Electronics:** microcontroller, arduino, esp32, raspberry-pi, stm32, teensy, motor-driver, a4988, drv8825, tmc2209, l298n, pca9685, pwm, h-bridge, pcb, breadboard, wiring, power-supply, voltage-regulator, step-down, buck-converter
- **Sensors:** encoder, potentiometer, hall-effect, imu, accelerometer, gyroscope, force-sensor, load-cell, limit-switch, endstop, current-sensor
- **Software:** firmware, arduino-ide, platformio, ros, ros2, moveit, python, cpp, control-software, kinematics-library, inverse-kinematics, forward-kinematics, dh-parameters, trajectory-planning, motion-control, pid, feedforward, calibration, serial-communication, i2c, can-bus, usb
- **Design:** cad, onshape, fusion360, freecad, solidworks, stl, step, openscad, simulation, stress-analysis, finite-element, workspace, reach, payload, precision, repeatability, accuracy, backlash
- **Control:** joint-space, task-space, cartesian-control, velocity-control, torque-control, position-control, impedance-control, admittance-control, gravity-compensation, pick-and-place, path-planning, collision-detection
- **Projects:** arduino-robot-arm, mearm, uarm, open-source-arm, robotis-open-manipulator, braccio-tinkerkit, phantomx, lynxmotion, arm-link, desktop-robot-arm
- **Meta:** tutorial, review, comparison, guide, benchmark, troubleshooting, safety

### By Difficulty
- beginner
- intermediate
- advanced

### By Status
- in-progress
- tested
- experimental
- planned

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** when fully superseded — move to `_archive/`, remove from index

## Entity Pages
One page per notable entity. Include:
- Overview / what it is
- Key specifications and facts
- Relationships to other entities ([[wikilinks]])
- Source references
- For commercial products: price, availability, community support

## Concept Pages
One page per concept or topic. Include:
- Definition / explanation
- Practical relevance for DIY robotic arms
- Current state of knowledge
- Open questions or debates
- Related concepts ([[wikilinks]])

## Comparison Pages
Side-by-side analyses. Include:
- What is being compared and why
- Dimensions of comparison (table format in markdown)
- Verdict or synthesis for DIY use
- Sources

## Project Pages
One page per specific robot arm build / project. Include:
- Goal and target specifications (DOF, reach, payload, precision)
- Bill of materials with costs
- Build log / instructions
- Software stack
- Results and lessons learned
- Links to entity/concept pages for components used

## Update Policy
When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report
