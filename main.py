from paho.mqtt.client as mqtt
from gpiozero import Button
from signal import pause

from systemkey import client
# systemkey.py includes client setup, see "examplesystemkey.py"


button1 = Button(2)
button2 = Button(3)
button3 = Button(4)

broker_address = "homeassistant.local"
broker_port = 1883

def button1Func():
    client.connect(broker_address, broker_port)
    topic = "terminal.button1"
    client.publish(topic)
    client.disconnect()

def button2Func():
    client.connect(broker_address, broker_port)
    topic = "terminal.button2"
    client.publish(topic)
    client.disconnect()

def button3Func():
    client.connect(broker_address, broker_port)
    topic = "terminal.button3"
    client.publish(topic)
    client.disconnect()

button1.when_pressed = button1Func
button2.when_pressed = button2Func
button3.when_pressed = button3Func

pause()