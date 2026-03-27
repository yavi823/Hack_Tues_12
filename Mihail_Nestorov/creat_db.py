import sqlite3
import os

print("Papka:", os.getcwd())

conn = sqlite3.connect("smartpot.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS plants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT,
    date_planted TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plant_id INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    temperature REAL,
    humidity REAL,
    soil_moisture REAL,
    pressure REAL,
    FOREIGN KEY (plant_id) REFERENCES plants(id)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plant_id INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    event TEXT,
    FOREIGN KEY (plant_id) REFERENCES plants(id)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS ai_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plant_id INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT,
    FOREIGN KEY (plant_id) REFERENCES plants(id)
)
""")

conn.commit()
conn.close()

print("Bazata e suzdadena uspeshno")