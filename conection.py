import sqlite3

class DatabaseManager:
    def __init__(self, database_file):
        self.database_file = database_file
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()
        
    def insertar_producto(self, nombre, marca, modelo, cantidad, precio_unitario):
        try:
            # Ejecutar la consulta SQL para insertar los datos del producto
            self.cursor.execute("INSERT INTO productos (nombre, marca, modelo, cantidad, precio_unitario) VALUES (?, ?, ?, ?, ?)",
                                (nombre, marca, modelo, cantidad, precio_unitario))
            self.connection.commit()  # Confirmar la transacción
            print("Producto insertado correctamente.")
        except sqlite3.Error as e:
            print("Error al insertar producto:", e)  

    def obtener_productos(self):
        # Ejecutar una consulta para obtener todos los datos de la tabla productos
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall()
        return productos

    def eliminar_producto(self, ID_P):
        try:
            # Ejecutar la consulta SQL para eliminar el producto con el ID dado
            self.cursor.execute("DELETE FROM productos WHERE ID_P = ?", (ID_P))
            self.connection.commit()  # Confirmar la transacción
            print("Producto eliminado correctamente.")
        except sqlite3.Error as e:
            print("Error al eliminar producto:", e)              

    def actualizar_precio_bs(self, id_producto, precio_bs):
        try:
            # Actualizar el precio_bs en la base de datos para el producto con el ID dado
            self.cursor.execute("UPDATE productos SET precio_bs = ? WHERE ID_P = ?", (precio_bs, id_producto))
            self.connection.commit()
            print("Precio en bolívares actualizado correctamente.")
        except sqlite3.Error as e:
            print("Error al actualizar precio en bolívares soberanos:", e)

    def obtener_productos(self):
        # Ejecutar una consulta para obtener todos los datos de la tabla productos
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall()
        return productos
    
    def obtener_producto_por_nombre(self, nombre):
        try:
            # Ejecutar una consulta para obtener los datos del producto por su nombre
            self.cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
            producto = self.cursor.fetchone()
            return producto
        except sqlite3.Error as e:
            print("Error al obtener producto por nombre:", e)
            return None


