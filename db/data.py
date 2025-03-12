import sqlite3

conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM usuarios")
datos = cursor.fetchall()
conn.close()

print("Datos en la base de datos:", datos)
