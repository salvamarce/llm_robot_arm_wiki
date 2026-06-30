"""
Cycloidal Drive — Generazione Parametrica per Fusion 360
========================================================
Esegui via fusion_mcp_execute con featureType: "script"

Parametri:
  R  = 32 mm   (pitch circle radius rulli corona)
  Rr =  2 mm   (raggio rulli = Ø4/2)
  E  =  1.0 mm (eccentricità)
  N  = 21      (numero rulli corona)
  Zc = 20      (lobi disco = N - 1 = riduzione 20:1)

NOTA: Fusion usa cm internamente. Tutti i valori qui sono in cm.
Adattare secondo le unità del documento attivo.
"""

import math
import adsk.core, adsk.fusion, adsk.cam, traceback

# ── Parametri (in cm per Fusion) ──────────────────────────────────
R  = 3.2      # 32 mm
Rr = 0.2      # 2 mm (raggio rullo)
E  = 0.1      # 1.0 mm eccentricità
N  = 21       # numero rulli corona
Zc = 20       # lobi disco
NUM_POINTS = 500  # punti per generare il profilo
DISK_THICKNESS = 0.5    # 5 mm spessore disco
CLEARANCE = 0.01        # 0.1 mm clearance
BOLT_R = 0.15           # raggio perno output 1.5 mm (Ø3 per M3)
PIN_RADIUS = 0.4        # raggio perno output 4 mm (Ø8)
PIN_HOLE_R = 0.5        # foro output 5 mm raggio = 10 mm diametro (Ø8 + 2*E)

# PCD perni output (da ottimizzare)
PIN_PCD = 2.4  # 24 mm 
NUM_PINS = 6

# Cuscinetto centrale
BEARING_OD = 1.05  # raggio 10.5 mm (OD 21mm 6801-ZZ / 2)
SHAFT_HD_R = 0.65  # raggio 6.5 mm (foro passaggio albero)

# Corona
CORONA_OD = R + Rr + 0.3  # raggio esterno corona
ROLLER_DIA = 0.2           # raggio foro rullo
RING_THICKNESS = 0.6       # spessore corona 6 mm
RING_GAP = 0.015           # gioco 0.15 mm


def cycloidal_point(t):
    """Calcola un punto (x, y) del profilo cicloide al parametro t."""
    s = math.sin((1 - N) * t)
    c = math.cos((1 - N) * t)
    denom = (R / (E * N)) - c
    psi = math.atan2(s, denom)
    
    x = R * math.cos(t) - Rr * math.cos(t + psi) - E * math.cos(N * t)
    y = -R * math.sin(t) + Rr * math.sin(t + psi) + E * math.sin(N * t)
    return x, y


def generate_profile_points():
    """Genera N punti del profilo cicloide per t in [0, 2pi)."""
    pts = []
    for i in range(NUM_POINTS):
        t = (2 * math.pi * i) / NUM_POINTS
        x, y = cycloidal_point(t)
        pts.append((x, y))
    return pts


def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        if not design:
            ui.messageBox("Nessun design attivo. Creane uno prima.")
            return
        
        # Usa unità del documento
        units = design.fusionUnitsManager
        default_unit = units.defaultLengthUnits
        
        root = design.rootComponent
        
        # ── 1. DISCO CICLOIDALE ──
        ui.messageBox("Genero il profilo cicloide...")
        
        # Crea sketch sul piano XY
        sketches = root.sketches
        xy_plane = root.xYConstructionPlane
        sketch = sketches.add(xy_plane)
        
        # Genera punti del profilo
        pts = generate_profile_points()
        
        # Crea punti nello sketch
        sketch_points = []
        for x, y in pts:
            pt = adsk.core.Point3D.create(x, y, 0)
            sketch_point = sketch.sketchPoints.add(pt)
            sketch_points.append(sketch_point)
        
        # Crea spline attraverso i punti
        # Nota: Fusion potrebbe avere limiti sul numero di punti
        # In tal caso, riduci NUM_POINTS a ~200
        spline = sketch.sketchCurves.sketchFittedSplines.add(sketch_points)
        
        # ── 2. EXTRUSIONE DISCO ──
        ui.messageBox("Estrudo il disco...")
        prof = sketch.profiles.item(0)
        extrudes = root.features.extrudeFeatures
        ext_input = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        ext_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(DISK_THICKNESS))
        ext = extrudes.add(ext_input)
        body = ext.bodies.item(0)
        body.name = "Disco Cicloidale"
        
        # ── 3. FORO CUSCINETTO CENTRALE ──
        ui.messageBox("Aggiungo foro centrale per cuscinetto...")
        
        # Sketch per fori sul piano superiore del disco
        top_face = None
        for face in body.faces:
            # Trova la faccia più alta (Z positiva)
            bbox = face.boundingBox
            if bbox.maxPoint.z > 0.24 and bbox.minPoint.z > 0.24:
                top_face = face
                break
        
        if top_face:
            hole_sketch = sketches.add(top_face)
            
            # Foro cuscinetto centrale
            center = adsk.core.Point3D.create(0, 0, 0)
            center_pt = hole_sketch.sketchPoints.add(center)
            circle = hole_sketch.sketchCurves.sketchCircles.addByCenterRadius(center_pt, BEARING_OD)
            
            # Extraid come taglio
            hole_prof = hole_sketch.profiles.item(0)
            hole_extrudes = root.features.extrudeFeatures
            hole_input = hole_extrudes.createInput(hole_prof, adsk.fusion.FeatureOperations.CutFeatureOperation)
            hole_input.setAllExtent(True)
            hole_extrudes.add(hole_input)
        
        # ── 4. FORI PER PERNI OUTPUT ──
        ui.messageBox("Aggiungo fori per perni output...")
        
        pin_sketch = sketches.add(xy_plane)
        for i in range(NUM_PINS):
            angle = (2 * math.pi * i) / NUM_PINS
            px = PIN_PCD * math.cos(angle)
            py = PIN_PCD * math.sin(angle)
            pt = pin_sketch.sketchPoints.add(adsk.core.Point3D.create(px, py, 0))
            circle = pin_sketch.sketchCurves.sketchCircles.addByCenterRadius(pt, PIN_HOLE_R)
        
        # Extraid fori perni
        for profile in pin_sketch.profiles:
            if profile:
                hole_input = hole_extrudes.createInput(profile, adsk.fusion.FeatureOperations.CutFeatureOperation)
                hole_input.setAllExtent(True)
                hole_extrudes.add(hole_input)
        
        # ── 5. CORONA CON RULLI ──
        ui.messageBox("Genero la corona esterna con sedi rulli...")
        
        corona_sketch = sketches.add(xy_plane)
        
        # Cerchio esterno corona
        center_origin = adsk.core.Point3D.create(0, 0, 0)
        center_pt = corona_sketch.sketchPoints.add(center_origin)
        outer_circle = corona_sketch.sketchCurves.sketchCircles.addByCenterRadius(center_pt, CORONA_OD)
        
        # Cerchio interno corona (dove alloggia il disco)
        inner_circle = corona_sketch.sketchCurves.sketchCircles.addByCenterRadius(center_pt, R + Rr + RING_GAP)
        
        # 21 fori per rulli in acciaio
        for i in range(N):
            angle = (2 * math.pi * i) / N
            rx = R * math.cos(angle)
            ry = R * math.sin(angle)
            r_pt = corona_sketch.sketchPoints.add(adsk.core.Point3D.create(rx, ry, 0))
            r_circle = corona_sketch.sketchCurves.sketchCircles.addByCenterRadius(r_pt, ROLLER_DIA)
        
        # Extraid corona
        corona_prof = corona_sketch.profiles.item(0)
        if corona_prof:
            corona_input = extrudes.createInput(corona_prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            corona_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(RING_THICKNESS))
            corona = extrudes.add(corona_input)
            corona.bodies.item(0).name = "Corona"
        
        # ── 6. FORI M3 PER RULLI (sulla corona) ──
        # (facoltativo, fori passanti M3 attraverso la corona)
        ui.messageBox("Aggiungo fori passanti M3 per rulli...")
        
        screw_sketch = sketches.add(xy_plane)
        for i in range(N):
            angle = (2 * math.pi * i) / N
            sx = R * math.cos(angle)
            sy = R * math.sin(angle)
            s_pt = screw_sketch.sketchPoints.add(adsk.core.Point3D.create(sx, sy, 0))
            s_circle = screw_sketch.sketchCurves.sketchCircles.addByCenterRadius(s_pt, 0.15)  # Ø3 M3
        
        for profile in screw_sketch.profiles:
            if profile:
                screw_input = hole_extrudes.createInput(profile, adsk.fusion.FeatureOperations.CutFeatureOperation)
                screw_input.setAllExtent(True)
                hole_extrudes.add(screw_input)
        
        # ── 7. FORI DI MONTAGGIO BASE (NEMA 17) ──
        ui.messageBox("Aggiungo fori mounting NEMA 17...")
        
        mount_sketch = sketches.add(xy_plane)
        mount_r = 1.55  # 31 mm bolt circle / 2 = 15.5 mm
        for i in range(4):
            angle = (2 * math.pi * i) / 4 + math.pi / 4  # 45° offset
            mx = mount_r * math.cos(angle)
            my = mount_r * math.sin(angle)
            m_pt = mount_sketch.sketchPoints.add(adsk.core.Point3D.create(mx, my, 0))
            m_circle = mount_sketch.sketchCurves.sketchCircles.addByCenterRadius(m_pt, 0.15)  # Ø3 M3
        
        for profile in mount_sketch.profiles:
            if profile:
                mount_input = hole_extrudes.createInput(profile, adsk.fusion.FeatureOperations.CutFeatureOperation)
                mount_input.setAllExtent(True)
                hole_extrudes.add(mount_input)
        
        ui.messageBox(
            "✅ Riduttore cicloidale generato!\n\n"
            f"Componenti:\n"
            f"- Disco cicloide (spess. {DISK_THICKNESS*10:.0f} mm)\n"
            f"- Corona con {N} sedi rulli\n"
            f"- 6 fori perni output (ø{PIN_HOLE_R*20:.0f} mm)\n"
            f"- Foro cuscinetto centrale (ø{BEARING_OD*20:.0f} mm)\n"
            f"- 4 fori mounting NEMA 17\n\n"
            f"Rapporto: {Zc}:1  |  E = {E*10:.1f} mm  |  R = {R*10:.0f} mm"
        )
        
    except Exception as e:
        if ui:
            ui.messageBox(f"❌ Errore: {traceback.format_exc()}")
        raise

