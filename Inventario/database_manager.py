import sqlite3


class DatabaseManager:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        # Crear la tabla clientes
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                                cedula TEXT PRIMARY KEY,
                                nombre TEXT,
                                telefono TEXT)''')

        # Crear la tabla productos
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                                ID_P INTEGER PRIMARY KEY,
                                nombre TEXT,
                                marca TEXT,
                                modelo TEXT,
                                cantidad INTEGER,
                                precio_unitario REAL)''')

        # Crear la tabla reparacion
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS reparacion (
                                ID_R INTEGER PRIMARY KEY,
                                descripcion TEXT,
                                fecha TEXT,
                                pago REAL,
                                CI_C TEXT,
                                FOREIGN KEY (CI_C) REFERENCES clientes (cedula))''')

        # Crear la tabla venta
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS venta (
                                ID_V INTEGER PRIMARY KEY,
                                id_prod INTEGER,
                                precio REAL,
                                precio_vent REAL,
                                precio_bs REAL,
                                FOREIGN KEY (id_prod) REFERENCES productos (ID_P))''')
        
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

    def insertar_producto(self, nombre, marca, modelo, cantidad, precio_unitario):
        try:
            # Insertar los datos del producto en la tabla productos
            self.cursor.execute("INSERT INTO productos (nombre, marca, modelo, cantidad, precio_unitario) VALUES (?, ?, ?, ?, ?)", (nombre, marca, modelo, cantidad, precio_unitario))
            self.connection.commit()
            print("Producto insertado correctamente.")
        except sqlite3.Error as e:
            print("Error al insertar producto:", e)
        
        
if __name__ == "__main__":
# Crear una instancia de DatabaseManager y conectar a la base de datos
     db_manager = DatabaseManager(r"Recursos\bd\db.db")

# Crear las tablas si no existen db_manager.create_tables()

# Ejemplo de inserción de datos de un nuevo producto
     nombre = "Producto 1"
     marca = "Marca 1"
     modelo = "Modelo 1"
     cantidad = 10
     precio_unitario = 50.0

# Llamar al método insertar_producto para agregar el nuevo producto a la base de datos
     db_manager.insertar_producto(nombre, marca, modelo, cantidad, precio_unitario)

# Cerrar la conexión después de realizar las operaciones necesarias
     db_manager.close_connection()