---
title: MKS SERVO42D — Modulo stepper closed-loop CAN
created: 2026-06-16
updated: 2026-06-16
type: entity
tags: [stepper-driver, closed-loop, can-bus, mks-servo42d, hardware]
confidence: high
---

# MKS SERVO42D / SERVO57D

Modulo driver per motori passo-passo in **anello chiuso (closed-loop)** con controllo FOC e interfaccia CAN bus. Scelto da Salvatore per il [[salvatore-robot-arm]].

## Specifiche

| Parametro | Valore |
|-----------|--------|
| **Modelli** | SERVO42D (NEMA 17/23), SERVO57D (NEMA 23/24) |
| **Alimentazione** | 12-36V DC |
| **Corrente max** | 4A (SERVO42D), 8A (SERVO57D) con dissipatore |
| **Encoder** | 16384 cpr (14-bit magnetic) |
| **Interfaccia** | CAN bus (default 500 kbps) o Pulse/Step-Dir |
| **Microstepping** | Fino a 256 subdivision |
| **Coppia max** | Closed-loop FOC, coppia piena anche a fermo |
| **Display** | OLED 0.96" integrato |

## Vantaggi per il braccio robotico

- **Closed-loop**: encoder 16384 cpr, nessun passo perso — fondamentale con riduttori [[cycloidal-drive]] che hanno attrito interno
- **CAN bus**: 2 fili (CAN-H, CAN-L) per tutti i motori — wiring minimo nel braccio rotante
- **FOC**: funzionamento silenzioso e fluido, accelerazioni/decelerazioni configurabili
- **Sync hardware**: comandi broadcast/group per movimenti sincroni tra giunti
- **Homing integrato**: finecorsa e limit switch gestiti dal driver

## Libreria di Controllo

Repository: [salvamarce/MKS_SERVO42D](https://github.com/salvamarce/MKS_SERVO42D)

Libreria Arduino sviluppata da Salvatore:
- **100% C++**, piattaforma-indipendente, MIT license
- Copre l'intero set comandi del manuale V1.0.9
- CRC automatico 8bit
- Solo 4 byte per istanza motore
- API helper per lavorare in gradi (`degreesToEncoderCounts()`, `encoderCountsToDegrees()`)

### Modalità operative

| Modalità | Interfaccia | Uso consigliato |
|----------|------------|-----------------|
| SR_vFOC | CAN bus | **Primaria** — FOC su CAN |
| SR_CLOSE | CAN bus | Closed-loop su CAN (alternativa) |
| CR_vFOC | Pulse/Step-Dir | FOC con drive tradizionale |
| CR_CLOSE | Pulse/Step-Dir | Closed-loop con step/dir |

### Cablaggio base

```
Arduino → MCP2515 (CS=10, SPI)
               ├── CAN-H ──┐
               ├── CAN-L ──┤
                             ├── MKS SERVO42D #1 (CAN ID 0x01)
                             ├── MKS SERVO42D #2 (CAN ID 0x02)
                             └── MKS SERVO42D #3 (CAN ID 0x03)
             120Ω ──┘ └── 120Ω (terminazione ai capi)
```

## Installazione

### Arduino IDE
1. Scaricare ZIP da GitHub
2. Sketch → Include Library → Add .ZIP Library

### PlatformIO
```ini
lib_deps =
    MKS_SERVO42D
    autowp/arduino-mcp2515
```

## Quick Start

```cpp
#include <SPI.h>
#include <mcp2515.h>
#include "MKS_SERVO42D.h"

MCP2515 mcp2515(10);
MKS_SERVO42D motor(0x01);

void setup() {
    Serial.begin(115200);
    mcp2515.reset();
    mcp2515.setBitrate(CAN_500KBPS, MCP_8MHZ);
    mcp2515.setNormalMode();

    MKS_CANMessage msg;

    motor.setWorkMode(msg, MKS_MODE_SR_vFOC);
    sendMessage(msg);
    delay(500);

    motor.setMotorEnable(msg, true);
    sendMessage(msg);
    delay(500);

    // Rotazione relativa 180 gradi a 300 RPM
    motor.relativeMotionByDegrees(msg, 300, 10, 180.0);
    sendMessage(msg);
}

void loop() {}

void sendMessage(MKS_CANMessage& msg) {
    struct can_frame canMsg;
    canMsg.can_id = msg.canId;
    canMsg.can_dlc = msg.dlc;
    memcpy(canMsg.data, msg.data, msg.dlc);
    mcp2515.sendMessage(&canMsg);
}
```

## Related
- [[salvatore-robot-arm]] — Progetto che usa questi driver
- [[nema-17]] — Motori controllati
- [[cycloidal-drive]] — Riduttori abbinati
- [scheda prodotto MKS SERVO42D](https://www.makerbase.cn/products/mks-servo42d)
- [libreria su GitHub](https://github.com/salvamarce/MKS_SERVO42D)
