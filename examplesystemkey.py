from paho.mqtt.client as mqtt

client = mqtt.Client()
client.username_pw_set(username="", password="")
# just insert the username and password