# IoT RC Car with ESP-NOW

![RC Car](https://img.shields.io/badge/Project-RC%20Car-blue)
![MicroPython](https://img.shields.io/badge/MicroPython-FFD43B?style=flat&logo=python&logoColor=blue)
![ESP-NOW](https://img.shields.io/badge/ESP--NOW-FF0000?style=flat&logo=espressif&logoColor=white)

A high-performance IoT RC Car controlled via ESP-NOW protocol, featuring 720 coreless motors for smooth and responsive movement.

## 🚀 Features

- **ESP-NOW Communication**: Fast and reliable wireless control using ESP-NOW protocol
- **Dual DRV8833 Motor Drivers**: Precise control over four 720 coreless motors
- **Custom Controller**: Compatible with Custom ESP-Now-RC controller
- **MicroPython Firmware**: Easy to modify and update
- **PWM Control**: Smooth speed and direction control
- **Real-time Response**: Low latency control system

## 🛠️ Hardware Requirements

- ESP32/ESP8266 Microcontroller
- 2x DRV8833 Motor Drivers
- 4x 720 Coreless Motors
- Custom ESP-Now-RC Controller
- Power Supply (Micro-Lipo Batteries atleast 2A discharge)
- Breadboard/PCB

## 📋 Pin Configuration

### Motor Driver 1 (DRV8833)
- IN1: GPIO 10
- IN2: GPIO 11
- IN3: GPIO 12
- IN4: GPIO 13

### Motor Driver 2 (DRV8833)
- IN1: GPIO 2
- IN2: GPIO 3
- IN3: GPIO 5
- IN4: GPIO 6

## 🔧 Installation

1. Flash MicroPython firmware to your ESP32/ESP8266
2. Upload the `RC-car-firmware.py` to your device
3. Connect the motor drivers and motors according to the pin configuration
4. Power up the system
5. Pair with your Custom ESP-Now-RC controller

## 🎮 Control System

The car uses a dual-joystick control system:
- **Left Joystick (Y-axis)**: Controls forward/backward movement
- **Right Joystick (X-axis)**: Controls left/right turning

## 📊 Technical Specifications

- **PWM Frequency**: 1000Hz
- **Speed Range**: -30000 to +30000
- **Communication Protocol**: ESP-NOW
- **Motor Type**: 720 Coreless Motors
- **Control Resolution**: 16-bit PWM

## ⚠️ Safety Notes

- Always ensure proper power supply voltage
- Check motor temperature during extended use
- Keep firmware updated for optimal performance
- Ensure proper wiring to prevent short circuits

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- MicroPython community
- ESP-NOW protocol developers
- Custom ESP-Now-RC controller team

---

Made with ❤️ for RC enthusiasts