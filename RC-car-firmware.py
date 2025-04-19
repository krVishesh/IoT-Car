import network
import espnow
from machine import Pin, PWM

# Initialize ESP-NOW
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
esp = espnow.ESPNow()
esp.active(True)

# Define motor pins for first DRV8833
drv1_in1 = PWM(Pin(10))
drv1_in2 = PWM(Pin(11))
drv1_in3 = PWM(Pin(12))
drv1_in4 = PWM(Pin(13))

# Define motor pins for second DRV8833
drv2_in1 = PWM(Pin(2))
drv2_in2 = PWM(Pin(3))
drv2_in3 = PWM(Pin(5))
drv2_in4 = PWM(Pin(6))

# Set PWM frequency
for motor in [drv1_in1, drv1_in2, drv1_in3, drv1_in4, drv2_in1, drv2_in2, drv2_in3, drv2_in4]:
    motor.freq(1000)

def motor_control(in1, in2, speed, reverse=False):
    """Control a motor direction and speed, with an option to reverse direction."""
    if reverse:
        speed = -speed
    if speed > 0:
        in1.duty_u16(speed)
        in2.duty_u16(0)
    elif speed < 0:
        in1.duty_u16(0)
        in2.duty_u16(abs(speed))
    else:
        in1.duty_u16(0)
        in2.duty_u16(0)

def receive_data():
    print("Waiting for data...")
    
    try:
        while True:
            # Non-blocking receive in a tight loop
            msg = esp.recv()
            if msg:
                peer_mac, data = msg
                if data:
                    try:
                        data_str = data.decode()
                        data = eval(data_str)  # Using eval for speed, but less safe than json.loads()

                        # Extract joystick values
                        joy1_y = data.get("Joystick1-Y", 1648)  # Forward/Reverse
                        joy2_x = data.get("Joystick2-X", 1649)  # Left/Right

                        # Normalize values (-30000 to +30000)
                        speed = int(((joy1_y - 1648) / (3264 - 1648)) * 40000)
                        turn = int(((joy2_x - 1649) / (3264 - 1649)) * 25000)

                        # Calculate motor speeds
                        left_speed = speed + turn
                        right_speed = speed - turn

                        # Ensure values are within PWM range
                        left_speed = max(min(left_speed, 30000), -30000)
                        right_speed = max(min(right_speed, 30000), -30000)

                        # Apply motor control with reversed logic for second motors
                        motor_control(drv1_in1, drv1_in2, right_speed)
                        motor_control(drv1_in3, drv1_in4, left_speed, reverse=True)  # Reverse
                        motor_control(drv2_in1, drv2_in2, right_speed)
                        motor_control(drv2_in3, drv2_in4, left_speed, reverse=True)  # Reverse

                        print(f"Speed: {speed}, Turn: {turn}, Left: {left_speed}, Right: {right_speed}")
                    except Exception as e:
                        print("Error decoding:", e)
    except KeyboardInterrupt:
        # Clean shutdown on keyboard interrupt
        for motor in [drv1_in1, drv1_in2, drv1_in3, drv1_in4, drv2_in1, drv2_in2, drv2_in3, drv2_in4]:
            motor.duty_u16(0)
        print("Program stopped")

# Run without asyncio
if __name__ == "__main__":
    receive_data()
