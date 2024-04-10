# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("tu_base_de_datos.db")

# Crear tabla de SALARIOS 
try:
   conn.execute(
      """
      CREATE TABLE SALARIOS
      (id INTEGER PRIMARY KEY,
      empleado_id INTEGER NOT NULL,
      salario REAL NOT NULL,
      fecha_inicio DATE NOT NULL,
      fecha_fin DATE NOT NULL,
      fecha_creacion TEXT NOT NULL,
      FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id));
      """
   )
except sqlite3.OperationalError:
   print("La tabla SALARIOS ya existe")

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
      fecha_creacion TEXT NOT NULL,
      FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
      FOREIGN KEY (cargo_id) REFERENCES CARGOS(id));
      """
   )
except sqlite3.OperationalError:
   print("La tabla EMPLEADOS ya existe")
  
## Crear tabla de DEPARTAMENTOS
try:
   conn.execute(
      """
      CREATE TABLE DEPARTAMENTOS
      (id INTEGER PRIMARY KEY,
      nombre TEXT NOT NULL,
      fecha_creacion TEXT NOT NULL);
      """
   )
except sqlite3.OperationalError:
   print("La tabla DEPARTAMENTOS ya existe")
    


# Crear tabla de CARGOS
try:
   conn.execute(
      """
      CREATE TABLE CARGOS
      (id INTEGER PRIMARY KEY,
      nombre TEXT NOT NULL,
      nivel TEXT NOT NULL,
      fecha_creacion TEXT NOT NULL);
      """
   )
except sqlite3.OperationalError:
   print("La tabla CARGOS ya existe")



# Insertar datos de carreras
conn.execute(
   """
   INSERT INTO DEPARTAMANETOS (nombre, fecha_creacion) 
   VALUES ('Contabilidad', )
   """
)


print()
# Guardar
conn.commit()
# Cerrar conexión
conn.close()