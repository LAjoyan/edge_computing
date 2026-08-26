# Edge Computing with Raspberry Pi Pico WH

Hands-on laboratory exercises and foundational edge computing workflows using the **Raspberry Pi Pico WH** running **MicroPython**.

---

## 🛠️ Hardware Specifications

| Component | Specification |
| :--- | :--- |
| **Model** | Raspberry Pi Pico WH (with pre-soldered pin headers) |
| **Silicon / MCU** | Raspberry Pi **RP2040** (Dual-core ARM Cortex-M0+ @ 133 MHz) |
| **Memory** | 264 KB on-chip SRAM, 2 MB external onboard QSPI Flash |
| **Wireless Module** | Infineon **CYW43439** (2.4 GHz 802.11n Wi-Fi & Bluetooth 5.2) |
| **I/O & Development** | 26 multi-function GPIO pins, 3-pin SWD debug port, micro-USB |

---

## 📂 Repository Structure

```
edge_computing/
├── .vscode/
├── 00_setup_internal_led/
│   └── main.py
├── 01_led/
│   └── main.py
│   └── traffic_light.jpg
├── 03_hardware_fundamentals/
│   └── main.py
│   └── nokia.py
│   └── pedestrian_light.jpg
├── 04_analog_digital_signals/
│   └── main.py
│   └── wokwi_pwm_simulation
├── .gitignore
└── README.md
```
---

## 🧪 Labs & Progress

### `00_setup_internal_led` Onboard LED Verification

Verifies the MicroPython runtime environment and board-level communication by driving the onboard status LED.

**Key Concepts:**

- Pin Mapping: On the standard Pico, the onboard LED is hardwired to GPIO 25, but on the Pico W / WH it is wired through the Infineon CYW43439 wireless IC. MicroPython automatically abstracts this via `Pin("LED", Pin.OUT)`

- State Inversion: Uses `.toggle()`to invert the LED state without tracking high (1) and low (0) values manually.

### `01_led` External Multi-LED Traffic Light Cycle

Interfaces external components via a breadboard, driving multiple color-coded LEDs sequentially through dedicated GPIO pins.

**Wiring & Wokwi Simulation:**

> 💡 **New to Wokwi?** [Wokwi](https://wokwi.com/) is a free online electronics simulator. It allows you to build, wire, and test code for microcontrollers (like the Raspberry Pi Pico) directly in your web browser without needing to buy any physical hardware!

![Wokwi Circuit Simulation](./01_led/traffic_light.jpg)

> **Note:** The Wokwi simulation image above shows all three LEDs illuminated at once to demonstrate a fully working circuit. It is crucial to ensure all jumper wires and resistors are plugged into the exact right places for the circuit to succeed. In reality, the provided `main.py` script cycles through the lights one at a time (like a traffic light). However, once you have everything wired correctly, you can modify the code and let your imagination decide how to light them up!

**Hardware Pin Mapping**
- Red LED: GPIO 15 (Pin 20) $\rightarrow$ Current-limiting resistor $\rightarrow$ Ground
- Yellow LED: GPIO 13 (Pin 17) $\rightarrow$ Current-limiting resistor $\rightarrow$ Ground
- Green LED: GPIO 10 (Pin 14) $\rightarrow$ Current-limiting resistor $\rightarrow$ Ground

**Implementation Details**

- Organizes hardware pin objects inside a Python dictionary for structured access.
- Uses list comprehension to isolate and shut off non-active LEDs during each phase of the cycle.


###  03_hardware_fundamentals

This project is a hardware simulation of a pedestrian crossing light built in MicroPython. It features a cross-request button, standard Red/Green walk lights, and an audible buzzer signal to assist visually impaired pedestrians.

**📸 Simulation Preview**

![Wokwi breadboard simulation showing a Raspberry Pi Pico W connected to LEDs, a button, and a buzzer. The green LED is illuminated and a music note indicates the buzzer is active.](./03_hardware_fundamentals/pedestrian_light.jpg)
*The pedestrian crossing system in the active "Walk" phase. The green LED is illuminated and the buzzer is emitting the audible crossing signal.*

## 🛠️ Hardware Setup (Pin Mapping)

| Component        | GPIO Pin | Role                          | Configuration                                 |
| ---------------- | -------- | ----------------------------- | --------------------------------------------- |
| **Red LED**      | 15       | "Do Not Walk" Signal          | Output (wired with current-limiting resistor) |
| **Green LED**    | 14       | "Walk" Signal                 | Output (wired with current-limiting resistor) |
| **Push Button**  | 13       | Pedestrian Cross Request      | Input (Internal `PULL_UP`)                    |
| **Buzzer**       | 11       | Audible Crossing Signal       | Output                                        |

## ✨ System Features
* **Hardware Interrupts:** Uses `Pin.irq` for immediate cross-request registration without blocking the main traffic loop.
* **Debouncing Logic:** Software debounce implemented using `time.ticks_ms()` to prevent rapid, ghost button presses.
* **Audible Accessibility:** Integrated buzzer sequence mimics real-world accessibility features for pedestrian crossings.
* **Clearance Warning:** Flashing green sequence indicates the crossing phase is about to terminate.


### 04_analog_digital_signals and Duty Cycle Fading

This project demonstrates the fundamental differences between a standard digital signal and an analog-like Pulse Width Modulation (PWM) signal. It visually compares a constant reference LED against a PWM-driven LED that progressively halves its brightness.


**📸 Simulation Preview**

![wokwi_pwm_simulation](./04_analog_digital_signals/wokwi_pwm_simulation.jpg)

*Wokwi simulation displaying the console output a**s the PWM duty cycle is progressively halved, resulting in a dimming effect on the left LED.*

**🛠️ Hardware Setup (Pin Mapping)**

| Component | GPIO Pin | Role | Configuration |
| :--- | :--- | :--- | :--- |
| **Fading LED** | 15 | PWM Output (Variable brightness) | `PWM()` operating at `1000 Hz` |
| **Reference LED**| 14 | Digital Output (Constant brightness) | `Pin.OUT` driven `HIGH (1)` |

**✨ Key Concepts & Implementation**

- **16-Bit Resolution:** MicroPython handles PWM duty cycles using 16-bit integers (`2**16`), meaning the power level is represented by a value between `0` (off) and `65535` (fully on).
- **Pulse Width Modulation (PWM):** Instead of a true analog voltage, the microcontroller rapidly pulses the digital pin on and off 1,000 times per second (`freq(1000)`) to create the illusion of dimming.
- **Algorithmic Fading:** The main loop utilizes a multiplier to perfectly cut the duty cycle in half on each step, dropping the visual brightness in a precise sequence: 50% ➔ 25% ➔ 12.5% ➔ 6.25% ➔ 3.125% before resetting.


## 🚀 Environment & Setup
1. Firmware: Flash the latest MicroPython for Raspberry Pi Pico W `.uf2` binary onto the board using `BOOTSEL` mode.

2. VS Code Setup: Use the MicroPico extension to manage the serial connection, upload files, and interact via REPL.

3. Execution: Save standalone scripts as main.py directly to the device root to trigger execution on boot.