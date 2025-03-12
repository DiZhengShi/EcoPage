import sqlite3

# Conectar o crear la base de datos
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT NOT NULL
    )
""")

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos creada con éxito")
