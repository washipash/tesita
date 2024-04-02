import sqlite3
import datetime
import os


class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.database_file = os.path.basename(db_path)
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
            # Iniciar una transacción
            self.connection.execute('BEGIN TRANSACTION')

            # Actualizar el precio_bs en la base de datos para el producto con el ID dado
            self.cursor.execute("UPDATE productos SET precio_bs = ? WHERE ID_P = ?", (precio_bs, id_producto))
            self.connection.commit()  # Confirmar la transacción
            print("Precio en bolívares actualizado correctamente.")
        except sqlite3.Error as e:
            print("Error al actualizar precio en bolívares soberanos:", e)
            self.connection.rollback()  # Revertir la transacción en caso de error

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

    def restar_cantidad_producto(self, id_producto, cantidad_vendida):
        try:
            # Obtener la cantidad disponible del producto
            self.cursor.execute("SELECT cantidad FROM productos WHERE id = ?", (id_producto,))
            resultado = self.cursor.fetchone()
            if resultado is None:
                print(f"No se encontró ningún producto con el ID {id_producto}.")
                return
    
            cantidad_disponible = resultado[0]
    
            # Calcular la nueva cantidad después de la venta
            nueva_cantidad = cantidad_disponible - cantidad_vendida
    
            # Actualizar la cantidad en la tabla de productos
            self.cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, id_producto))
            self.connection.commit()
            print("Cantidad actualizada correctamente.")
        except sqlite3.Error as e:
            print("Error al restar cantidad de producto:", e)   

    def insertar_salida(self, id_producto, precio_venta, precio_bs, cantidad_vendida):
            try:
                # Obtener la fecha y hora actual
                fecha_actual = datetime.date.today()
                hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    
                # Ejecutar la consulta SQL para insertar los datos de la salida
                self.cursor.execute("INSERT INTO ventas (id_prod, fecha, hora, precio_vent, precio_bs) VALUES (?, ?, ?, ?, ?)",
                                    (id_producto, fecha_actual, hora_actual, precio_venta, precio_bs))
                self.connection.commit()  # Confirmar la transacción
                
                # Restar la cantidad vendida de la tabla de productos
                self.restar_cantidad_producto(id_producto, cantidad_vendida)
                
                print("Salida de productos registrada correctamente.")
            except sqlite3.Error as e:
                print("Error al insertar salida de productos:", e)
    
    def obtener_ultimo_id_venta(self):
        try:
            # Ejecutar una consulta SQL para obtener el último ID de venta
            self.cursor.execute("SELECT MAX(ID_V) FROM ventas_d")
            ultimo_id_venta = self.cursor.fetchone()[0]
            return ultimo_id_venta
        except sqlite3.Error as e:
            print("Error al obtener el último ID de venta:", e)
            return None     
        
    def actualizar_cantidad_producto(self, id_producto, nueva_cantidad):
        try:
        # Ejecutar la consulta SQL para actualizar la cantidad del producto
            self.cursor.execute("UPDATE productos SET cantidad = ? WHERE ID_P = ?", (nueva_cantidad, id_producto))
            self.connection.commit()  # Confirmar la transacción
            print("Cantidad del producto actualizada correctamente.")
        except sqlite3.Error as e:
            print("Error al actualizar la cantidad del producto:", e)    
            
    def insertar_usuario(self, nombre, contraseña):
        try:
            # Insertar los datos en la tabla 'user'
            self.cursor.execute("INSERT INTO user (nombre, contraseña) VALUES (?, ?)", (nombre, contraseña))
            # Confirmar la transacción
            self.connection.commit()
            print("Usuario registrado exitosamente.")
        except sqlite3.Error as e:
            print("Error al insertar usuario:", e)
# Uso:
# Crear una instancia del DatabaseManager
db_manager = DatabaseManager(r"recursos/bd/db.db")


     
            
  
            
       

