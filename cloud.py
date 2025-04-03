### IoT Cloud Operations Repository

# This script simulates an IoT device publishing data to AWS IoT Core.
import paho.mqtt.client as mqtt
import json
import time

# MQTT Configuration
BROKER = "test.mosquitto.org"  # Replace with your MQTT broker (e.g., ThingsBoard, AWS IoT)
PORT = 1883
TOPIC = "iot/sensor/data"

# Callback for connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}")

# Initialize MQTT Client
client = mqtt.Client()
client.on_connect = on_connect
client.connect(BROKER, PORT, 60)
client.loop_start()

# Simulating sensor data
try:
    while True:
        sensor_data = {
            "temperature": round(25 + (5 * (time.time() % 10) / 10), 2),
            "humidity": round(50 + (10 * (time.time() % 10) / 10), 2)
        }
        payload = json.dumps(sensor_data)
        client.publish(TOPIC, payload)
        print(f"Published: {payload} to {TOPIC}")
        time.sleep(5)  # Send data every 5 seconds
except KeyboardInterrupt:
    print("Stopping script...")
    client.loop_stop()
    client.disconnect()
