import sqlite3
import os

print("Papka:", os.getcwd())

conn = sqlite3.connect("smartpot.db")
c = conn.cursor()

print("Rasteniq:")
c.execute("SELECT * FROM plants")
print(c.fetchall())

print("Senzorni danni:")
c.execute("SELECT * FROM sensor_data")
print(c.fetchall())

print("Istoriq:")
c.execute("SELECT * FROM history")
print(c.fetchall())

print("AI status:")
c.execute("SELECT * FROM ai_status")
print(c.fetchall())

conn.close()

print("Gotovo")