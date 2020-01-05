import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish
import pigpio

pi = pigpio.pi()

pin_fog_pwr = 27
pin_fan_pwr = 17
pin_fan_pwm = 18

OFF_FAN = 1
OFF_FOG = 0

pi.write(pin_fog_pwr, OFF_FOG)
pi.write(pin_fan_pwr, OFF_FAN)

pi.hardware_PWM(pin_fan_pwm, 25000, 0)

publish.single("homeassistant/humidifier/poseidon/on/state", "OFF", hostname="192.168.0.10", retain=True)
publish.single("homeassistant/humidifier/poseidon/speed/state", "OFF", hostname="192.168.0.10", retain=True)

print("Humidifier shutdown")
