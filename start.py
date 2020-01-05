import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish
import pigpio

pi = pigpio.pi()

pin_fog_pwr = 27
pin_fan_pwr = 17
pin_fan_pwm = 18

ON_FAN = 0
OFF_FAN = 1

ON_FOG = 1
OFF_FOG = 0

speed_dict = {
    "low": 250000,
    "medium": 750000,
    "high": 1000000,
}

current_speed = speed_dict["high"]

pi.set_mode(pin_fog_pwr, pigpio.OUTPUT)
pi.set_mode(pin_fan_pwr, pigpio.OUTPUT)

# ENABLE = 0, DISABLE = 1

def turn_on():
    pi.write(pin_fog_pwr, ON_FOG)
    pi.write(pin_fan_pwr, ON_FAN)

def turn_off():
    pi.write(pin_fog_pwr, OFF_FOG)
    pi.write(pin_fan_pwr, OFF_FAN)

def on_command(client, userdata, message):
    payload = message.payload.decode("utf-8") 

    if payload == "ON":
        turn_on()
    elif payload == "OFF":
        turn_off()

    publish.single("homeassistant/humidifier/poseidon/on/state", payload, hostname="192.168.0.10")

def set_speed(new_speed):
    global current_speed
    current_speed = speed_dict[new_speed] if new_speed in speed_dict else current_speed
    pi.hardware_PWM(pin_fan_pwm, 25000, current_speed)
    publish.single("homeassistant/humidifier/poseidon/speed/state", current_speed, hostname="192.168.0.10", r$

def on_speed(client, userdata, message):
    payload = message.payload.decode("utf-8") 
    set_speed(payload)

def on_message(client, userdata, message):
    if message.topic == "homeassistant/humidifier/poseidon/on/set":
        on_command(client, userdata, message)
    elif message.topic == "homeassistant/humidifier/poseidon/speed/set":
        on_speed(client, userdata, message)
    else:
        pass 

set_speed("high")
turn_off()

print("Humidifier setup completed")

subscribe.callback(on_message, "homeassistant/humidifier/poseidon/#", hostname="192.168.0.10")
