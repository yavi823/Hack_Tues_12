import sqlite3

conn = sqlite3.connect("smartpot.db")
c = conn.cursor()

c.execute("INSERT INTO history (plant_id, event) VALUES (?, ?)", (1, "Поливане в 10:30"))

conn.commit()
conn.close()
print("Събитието е добавено!")