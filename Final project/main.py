from dotenv import load_dotenv
import os

import sqlite3
import subprocess
import base64
import requests

import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print("KEY:", api_key)

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

temp = bme280.temperature
humidity = bme280.humidity
pressure = bme280.pressure

print("Sensor:", temp, humidity, pressure)

subprocess.run(["rpicam-jpeg", "-o", "plant.jpg"], check=True)

with open("plant.jpg", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode("utf-8")

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "gpt-4.1-mini",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Kaji mi kratko sustoqnie na rastenieto"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}}
                ]
            }
        ],
        "max_tokens": 200
    },
    timeout=60
)

print("Status code:", response.status_code)
print("Raw response:", response.text)

data = response.json()

if "choices" not in data:
    print("Nqma choices")
    exit()

ai_text = data["choices"][0]["message"]["content"]
print("AI:", ai_text)

conn = sqlite3.connect("smartpot.db")
c = conn.cursor()

c.execute("""
INSERT INTO sensor_data (plant_id, temperature, humidity, soil_moisture, pressure)
VALUES (?, ?, ?, ?, ?)
""", (1, temp, humidity, 0, pressure))

c.execute("""
INSERT INTO ai_status (plant_id, status)
VALUES (?, ?)
""", (1, ai_text))

conn.commit()
conn.close()

print("Saved in DB")
