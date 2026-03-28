import sqlite3

conn = sqlite3.connect("smartpot.db")
c = conn.cursor()

c.execute("INSERT INTO ai_status (plant_id, status) VALUES (?, ?)", (1, "Добро състояние"))

conn.commit()
conn.close()
print("AI статусът е добавен!")