import sqlite3

connection = sqlite3.connect("telemetry.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM telemetry")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()