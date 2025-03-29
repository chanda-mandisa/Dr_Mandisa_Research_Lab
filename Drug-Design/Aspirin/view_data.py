import sqlite3

conn = sqlite3.connect("drug_simulation.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM drugs")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

