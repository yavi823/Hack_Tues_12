import sqlite3

conn = sqlite3.connect("smartpot.db")
c = conn.cursor()

c.execute("INSERT INTO plants (name, type, date_planted) VALUES (?, ?, ?)",
          ("Моят Босилек", "Босилек", "2026-03-27"))

conn.commit()
conn.close()
print("Растението е добавено!")