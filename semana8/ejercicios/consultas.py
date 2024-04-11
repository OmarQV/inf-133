# Conexion a la base de datos
import sqlite3

# Crear la cadena de conexion
conn = sqlite3.connect("personal.db")

# ------- JOIN -----------
print("\n--------- 1 ----------")
cursor = conn.execute(
   """
   SELECT EMPLEADOS.nombres, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, SALARIOS.salario
   FROM EMPLEADOS
   JOIN SALARIOS ON EMPLEADOS.id = SALARIOS.empleado_id
   """
)
for row in cursor:
   print(row)
   
print("\n--------- 2 ----------")
cursor = conn.execute(
   """
   SELECT e.nombres, e.apellido_paterno, e.apellido_materno, d.nombre 
   AS departamento, c.nombre 
   AS cargo
   FROM EMPLEADOS e
   JOIN DEPARTAMENTOS d 
   ON e.departamento_id = d.id
   JOIN CARGOS c 
   ON e.cargo_id = c.id;
   """
)
for row in cursor:
   print(row)

print("\n--------- 3 ----------")
cursor = conn.execute(
   """
   SELECT EMPLEADOS.nombres, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, DEPARTAMENTOS.nombre 
   AS departamento, CARGOS.nombre 
   AS cargo, SALARIOS.salario
   FROM EMPLEADOS
   JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id = DEPARTAMENTOS.id
   JOIN CARGOS ON EMPLEADOS.cargo_id = CARGOS.id
   JOIN SALARIOS ON EMPLEADOS.id = SALARIOS.empleado_id;
   """
)
for row in cursor:
   print(row)

print("\n--------- ACTUALIZA 1 ----------")
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
   
print("\n--------- ACTUALIZA 2 ----------")
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


print("\n--------- DELETE ----------")
conn.execute(
   """
   DELETE FROM SALARIOS 
   WHERE empleado_id = (SELECT id 
   FROM EMPLEADOS WHERE nombres = 'Maria' 
   AND apellido_paterno = 'Lopez' 
   AND apellido_materno = 'Martinez')
   """
)
conn.execute(
   """
   DELETE FROM EMPLEADOS 
   WHERE nombres = 'Maria' 
   AND apellido_paterno = 'Lopez' 
   AND apellido_materno = 'Martinez'
   """
)
# Consultar datos de EMPLEADOS
print("\nEMPLEADOS:")
cursor = conn.execute("SELECT * FROM EMPLEADOS")
for row in cursor:
   print(row)
print()

print("\n--------- 5 ----------")
cursor = conn.execute(
   """
   SELECT e.nombres, e.apellido_paterno, e.apellido_materno, d.nombre 
   AS departamento, c.nombre 
   AS cargo, s.salario
   FROM EMPLEADOS e
   JOIN DEPARTAMENTOS d ON e.departamento_id = d.id
   JOIN CARGOS c ON e.cargo_id = c.id
   JOIN SALARIOS s ON e.id = s.empleado_id;
   """
)
for row in cursor:
   print(row)

conn.commit()