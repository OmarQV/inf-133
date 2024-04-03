# Conexion a la base de datos
import sqlite3

# Crear la cadena de conexion
conn = sqlite3.connect("instituto.db")

conn.execute(
   """
   INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento)
   VALUES ('Carlos','Gomez','2001-02-10')
   """
)

conn.execute(
   """
   INSERT INTO CARRERAS (nombre, duracion)
   VALUES ('Licenciatura en Contabolidad','')
   """
)

# ------- JOIN -----------
print("\n--------- JOIN ----------")
cursor = conn.execute(
   """
   SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULACION.fecha
   FROM MATRICULAS
   JOIN ESTUDIANTES ON MATRICULAS.estudiante_id = ESTUDIANTES.id
   JOIN CARRERAS ON MATRICULAS.carreras_id = CARRERAS.id
   """
)
for row in cursor:
   print(row)