import sqlite3

conn = sqlite3.connect("smartpot.db")
c = conn.cursor()

c.execute("""
INSERT INTO sensor_data (plant_id, temperature, humidity, soil_moisture, pressure)
VALUES (?, ?, ?, ?, ?)
""", (1, 25, 55, 40, 1012))

conn.commit()
conn.close()
print("Данните от сензорите са добавени!")