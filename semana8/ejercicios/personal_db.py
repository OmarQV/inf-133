# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("personal.db")

#-------------------------------------------------
# Crear tabla de SALARIOS 
print()
try:
   conn.execute(
      """
      CREATE TABLE SALARIOS
      (id INTEGER PRIMARY KEY,
      empleado_id INTEGER NOT NULL,
      salario INTEGER NOT NULL,
      fecha_inicio DATE NOT NULL,
      fecha_fin DATE NOT NULL,
      fecha_creacion TEXT NOT NULL,
      FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id));
      """
   )
except sqlite3.OperationalError:
   print("La tabla SALARIOS ya existe")
   
# Insertar datos de SALARIOS
conn.execute(
   """
   INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) 
   VALUES (1, 3000, '01-04-2024', '30-04-2025', '01-04-2024')
   """
)
conn.execute(
   """
   INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) 
   VALUES (2, 3500, '01-07-2023', '30-04-2024', '01-07-2023')
   """
)

# Consultar datos de SALARIOS
print("\nSALARIOS:")
cursor = conn.execute("SELECT * FROM SALARIOS")
for row in cursor:
   print(row)

# Actualiza 
conn.execute(
   """
   UPDATE SALARIOS
   SET salario = 3600
   WHERE id = 2
   """
)

# Consultar datos de SALARIOS
print("\nSALARIOS:")
cursor = conn.execute("SELECT * FROM SALARIOS")
for row in cursor:
   print(row)
#-------------------------------------------------
# Crear tabla de EMPLEADOS
try:
   conn.execute(
      """
      CREATE TABLE EMPLEADOS
      (id INTEGER PRIMARY KEY,
      nombres TEXT NOT NULL,
      apellido_paterno TEXT NOT NULL,
      apellido_materno TEXT NOT NULL,
      fecha_contratacion DATE NOT NULL,
      departamento_id INTEGER NOT NULL,
      cargo_id INTEGER NOT NULL,
      fecha_creacion DATE NOT NULL,
      FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
      FOREIGN KEY (cargo_id) REFERENCES CARGOS(id));
      """
   )
except sqlite3.OperationalError:
   print("La tabla EMPLEADOS ya existe")

# Insertar datos de EMPLEADOS
conn.execute(
   """
   INSERT INTO EMPLEADOS (nombres, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion) 
   VALUES ('Juan', 'González', 'Pérez', '15-05-2023', 1, 1, '15-05-2023')
   """
)
conn.execute(
   """
   INSERT INTO EMPLEADOS (nombres, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion) 
   VALUES ('Maria', 'Lopez', 'Martinez', '20-06-2023', 2, 2, '20-06-2023')
   """
)

# Consultar datos de EMPLEADOS
print("\nEMPLEADOS:")
cursor = conn.execute("SELECT * FROM EMPLEADOS")
for row in cursor:
   print(row)
   
# Actualiza 
conn.execute(
   """
   UPDATE EMPLEADOS
   SET cargo_id = 3
   WHERE id = 2
   """
)
# Consultar datos de EMPLEADOS
print("\nEMPLEADOS:")
cursor = conn.execute("SELECT * FROM EMPLEADOS")
for row in cursor:
   print(row)
#-------------------------------------------------
# Crear tabla de DEPARTAMENTOS
try:
   conn.execute(
      """
      CREATE TABLE DEPARTAMENTOS
      (id INTEGER PRIMARY KEY,
      nombre TEXT NOT NULL,
      fecha_creacion DATE NOT NULL);
      """
   )
except sqlite3.OperationalError:
   print("La tabla DEPARTAMENTOS ya existe")
    
# Insertar datos de DEPARTAMENTOS
conn.execute(
   """
   INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) 
   VALUES ('Ventas', '10-04-2020')
   """
)
conn.execute(
   """
   INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) 
   VALUES ('Marketing', '11-04-2020')
   """
)
# Consultar datos de DEPARTAMENTOS
print("\nDEPARTAMENTOS:")
cursor = conn.execute("SELECT * FROM DEPARTAMENTOS")
for row in cursor:
   print(row)
   
#-------------------------------------------------
# Crear tabla de CARGOS
try:
   conn.execute(
      """
      CREATE TABLE CARGOS
      (id INTEGER PRIMARY KEY,
      nombre TEXT NOT NULL,
      nivel TEXT NOT NULL,
      fecha_creacion DATE NOT NULL);
      """
   )
except sqlite3.OperationalError:
   print("La tabla CARGOS ya existe")

# Insertar datos de CARGOS
conn.execute(
   """
   INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
   VALUES ('Gerente de Ventas', 'Senior', '10-04-2020')
   """
)
conn.execute(
   """
   INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
   VALUES ('Analista de Marketing', 'Junior', '11-04-2020')
   """
)
conn.execute(
   """
   INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
   VALUES ('Representante de Ventas', 'Junior', '12-04-2020')
   """
)
# Consultar datos de CARGOS
print("\nCARGOS:")
cursor = conn.execute("SELECT * FROM CARGOS")
for row in cursor:
   print(row)




print()
# Guardar
conn.commit()
# Cerrar conexión
conn.close()