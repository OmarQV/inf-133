# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")

# ------------- PLATOS --------------
# Crear tabla de platos
try:
   conn.execute(
      """
      CREATE TABLE PLATOS
      (id INTEGER PRIMARY KEY,
      nombre TEXT NOT NULL,
      precio REAL NOT NULL,
      categoria TEXT NOT NULL);
      """
   )
except sqlite3.OperationalError:
   print("La tabla PLATOS ya existe")


# Insertar datos de platos
# Plato 1
conn.execute(
   """
   INSERT INTO PLATOS (nombre, precio, categoria)
   VALUES ('Pizza', 10.99,'italiana')
   """
)
# Plato 2
conn.execute(
   """
   INSERT INTO PLATOS (nombre, precio, categoria)
   VALUES ('Hamburguesa', 8.99,'Americana')
   """
)
# Plato 3
conn.execute(
   """
   INSERT INTO PLATOS (nombre, precio, categoria)
   VALUES ('Sushi', 12.99,'Japonesa')
   """
)
# Plato 4
conn.execute(
   """
   INSERT INTO PLATOS (nombre, precio, categoria)
   VALUES ('Ensalada', 6.99,'Vegetariana')
   """
)

# SALIDA
# 'Hamburguesa', 8.99,'Americana'
# -> 'Hamburguesa', 9.99,'Americana'

# Listar datos de platos
print("\nPLATOS:")
cursor = conn.execute(
   "SELECT * FROM PLATOS"
)
for row in cursor:
   print(row)
   
# ------------- MESAS --------------
# Crear tabla de mesas
try:
   conn.execute(
      """
      CREATE TABLE MESAS
      (id INTEGER PRIMARY KEY,
      numero INTEGER NOT NULL);
      """
   )
except sqlite3.OperationalError:
   print("La tabla MESAS ya existe")


# Insertar datos de platos
# Mesa 1
conn.execute(
   """
   INSERT INTO MESAS (numero)
   VALUES (1)
   """
)
# Mesa 2
conn.execute(
   """
   INSERT INTO MESAS (numero)
   VALUES (2)
   """
)
# Mesa 3
conn.execute(
   """
   INSERT INTO MESAS (numero)
   VALUES (3)
   """
)
# Mesa 4
conn.execute(
   """
   INSERT INTO MESAS (numero)
   VALUES (4)
   """
)
# Listar datos de platos
print("\nMESAS:")
cursor = conn.execute(
   "SELECT * FROM MESAS"
)
for row in cursor:
   print(row)

# ------------- PEDIDOS --------------
# Crear tabla de pedidos
try:
   conn.execute(
      """
      CREATE TABLE PEDIDOS
      (id INTEGER PRIMARY KEY,
      plato_id INTEGER NOT NULL,
      mesa_id INTEGER NOT NULL,
      cantidad INTEGER NOT NULL,
      fecha DATE NOT NULL,
      FOREIGN KEY (plato_id) REFERENCES PLATOS(id),
      FOREIGN KEY (mesa_id) REFERENCES MESAS(id));
      """
   )
except sqlite3.OperationalError:
   print("La tabla PEDIDOS ya existe")


# Pedido 1
conn.execute(
   """
   INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
   VALUES (1, 2, 2, '2024-04-01')
   """
)
# Pedido 2
conn.execute(
   """
   INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
   VALUES (2, 3, 1, '2024-04-01')
   """
)
# Pedido 3
conn.execute(
   """
   INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
   VALUES (3, 1, 3, '2024-04-02')
   """
)
# Pedido 4
conn.execute(
   """
   INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
   VALUES (4, 4, 1, '2024-04-02')
   """
)
# Listar datos de platos
print("\nPEDIDOS:")
cursor = conn.execute(
   "SELECT * FROM PEDIDOS"
)
for row in cursor:
   print(row)

print("\n*"*50)
# Actualiza el precio del plato con id 2 (Hamburguesa) a 9.99
conn.execute(
   """
   UPDATE PLATOS
   SET precio = 9.99
   WHERE id = 2
   """
)
# Listar datos de platos
print("\nPLATOS: Actualiza el precio:")
cursor = conn.execute(
   "SELECT * FROM PLATOS"
)
for row in cursor:
   print(row)
# Cambia la categoría del plato con id 3 (Sushi) a "Fusión"
conn.execute(
   """
   UPDATE PLATOS
   SET categoria = "Fusión"
   WHERE id = 3
   """
)
# Listar datos de platos
print("\nPLATOS: Cambia la categoría")
cursor = conn.execute(
   "SELECT * FROM PLATOS"
)
for row in cursor:
   print(row)
# Elimina el plato con id 4 (Ensalada) de la tabla de platos
conn.execute(
   """
   DELETE FROM PLATOS
   WHERE id = 4
   """
)
print("\nPLATOS: Elimina el plato con id 4")
cursor = conn.execute(
   "SELECT * FROM PLATOS"
)
for row in cursor:
   print(row)
# Elimina el pedido con id 3
conn.execute(
   """
   DELETE FROM PEDIDOS
   WHERE id = 3
   """
)
print("\nPEDIDOS: Elimina el pedido con id 3")
cursor = conn.execute(
   "SELECT * FROM PEDIDOS"
)
for row in cursor:
   print(row)
# ----------------------------

print()
# Guardar datos
conn.commit()
# Cerrar conexión
conn.close()
