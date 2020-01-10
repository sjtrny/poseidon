# poseidon

Poseidon is a custom built humidifier. This repository contains:
- parts list
- wiring diagram
- required software and setup instructions

## Overview

Poseidon uses two relays to control power to:
- a fan
- a fogger (ultrasonic mist maker)

There is optional PWM control of the fan speed if using a 4-wire PWM fan.

Poseidon runs on [ESPHome](https://esphome.io). See `poseidon.yml`  for the configuration of the device.

## Parts List

The parts list can be found in the `parts.xlsx` file.

## Hardware and Wiring

<img src="https://github.com/sjtrny/poseidon/raw/master/wiring.png" width="800px"/>

## Instructions

1. Create virtual environment and install dependencies

```
./setup.sh
```

2. Activate virtual environment

```
source venv/bin/activate
```

3. Add wifi details to  `gaia.yml`

4. Plug in ESP32 via USB

5. Compile and upload to ESP32

```
esphome poseidon.yml run
```

