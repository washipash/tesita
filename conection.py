import sqlite3
import random

class DatabaseManager:
    def __init__(self, database_file):
        self.database_file = database_file
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()
    
    def generar_id_unico(self):
        # Generar un ID aleatorio de tres dígitos
        while True:
            id_aleatorio = random.randint(100, 999)
            # Verificar si el ID ya existe en la base de datos
            self.cursor.execute("SELECT COUNT(*) FROM productos WHERE ID_P = ?", (id_aleatorio,))
            if self.cursor.fetchone()[0] == 0:
                return id_aleatorio  # Devolver el ID aleatorio único
        
    def insertar_producto(self, nombre, marca, modelo, cantidad, precio_unitario):
        try:
            # Generar un ID aleatorio único para el nuevo producto
            id_aleatorio = self.generar_id_unico()
            # Ejecutar la consulta SQL para insertar los datos del producto
            self.cursor.execute("INSERT INTO productos (ID_P, nombre, marca, modelo, cantidad, precio_unitario) VALUES (?, ?, ?, ?, ?, ?)",
                                (id_aleatorio, nombre, marca, modelo, cantidad, precio_unitario))
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
        
    def obtener_producto_por_id(self, ID_P):
        try:
            # Ejecutar una consulta para obtener los datos del producto por su nombre
            self.cursor.execute("SELECT * FROM productos WHERE ID_P = ?", (ID_P,))
            producto = self.cursor.fetchone()
            return producto
        except sqlite3.Error as e:
            print("Error al obtener producto por id:", e)
            return None    

    def insertar_venta(self, id_producto, cantidad, precio_venta, precio_bs, hora_venta):
        try:
            # Ejecutar la consulta SQL para insertar los datos de la venta
            self.cursor.execute("INSERT INTO ventas_d (id_producto, cantidad, precio_venta, precio_bs, hora_venta) VALUES (?, ?, ?, ?, ?)",
                                (id_producto, cantidad, precio_venta, precio_bs, hora_venta))
            self.connection.commit()  # Confirmar la transacción
            print("Venta registrada correctamente.")
        except sqlite3.Error as e:
            print("Error al insertar venta:", e)
    
    def obtener_ultimo_id_venta(self):
        try:
            # Ejecutar una consulta SQL para obtener el último ID de venta
            self.cursor.execute("SELECT MAX(ID_V) FROM ventas_d")
            ultimo_id_venta = self.cursor.fetchone()[0]
            return ultimo_id_venta
        except sqlite3.Error as e:
            print("Error al obtener el último ID de venta:", e)
            return None        

