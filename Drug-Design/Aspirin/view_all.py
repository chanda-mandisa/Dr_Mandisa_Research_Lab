import sqlite3

conn = sqlite3.connect("drug_simulation.db")
cursor = conn.cursor()

print("\n=== Drugs ===")
cursor.execute("SELECT * FROM drugs")
for row in cursor.fetchall():
    print(row)

print("\n=== Targets ===")
cursor.execute("SELECT * FROM targets")
for row in cursor.fetchall():
    print(row)

print("\n=== Binding Sites ===")
cursor.execute("SELECT * FROM binding_sites")
for row in cursor.fetchall():
    print(row)

print("\n=== Pharmacokinetics ===")
cursor.execute("SELECT * FROM pharmacokinetics")
for row in cursor.fetchall():
    print(row)

print("\n=== Pharmacodynamics ===")
cursor.execute("SELECT * FROM pharmacodynamics")
for row in cursor.fetchall():
    print(row)

conn.close()

