import sqlite3
import datetime
import os


class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.database_file = os.path.basename(db_path)
    
        
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
            try:
                # Ejecutar una consulta para obtener todos los datos de la tabla productos
                self.cursor.execute("SELECT * FROM productos")
                productos = self.cursor.fetchall()
                return productos
            except sqlite3.Error as e:
                print("Error al obtener productos:", e)
                return None

    def eliminar_producto(self, ID_P):
        try:
            # Ejecutar la consulta SQL para eliminar el producto con el ID dado
            self.cursor.execute("DELETE FROM productos WHERE ID_P = ?", (ID_P,))
            self.connection.commit()  # Confirmar la transacción
            print("Producto eliminado correctamente.")
        except sqlite3.Error as e:
            print("Error al eliminar producto:", e)              

    def actualizar_precio_bs(self, ID_P, precio_bs):
        try:
            # Iniciar una transacción
            self.connection.execute('BEGIN TRANSACTION')

            # Actualizar el precio_bs en la base de datos para el producto con el ID dado
            self.cursor.execute("UPDATE productos SET precio_bs = ? WHERE ID_P = ?", (precio_bs, ID_P))
            self.connection.commit()  # Confirmar la transacción
            print("Precio en bolívares actualizado correctamente.")
        except sqlite3.Error as e:
            print("Error al actualizar precio en bolívares soberanos:", e)
            self.connection.rollback()  # Revertir la transacción en caso de error

    def obtener_producto_por_nombre(self, nombre, marca, modelo):
       try:
           # Ejecutar una consulta para obtener los datos del producto por su nombre
           self.cursor.execute("SELECT * FROM productos WHERE nombre = ? AND marca = ? AND modelo = ?", (nombre, marca, modelo))
           producto = self.cursor.fetchone()
           print("Producto encontrado:", producto)
           return producto
       except sqlite3.Error as e:
           print("Error al obtener producto por nombre:", e)
           return None
        
    def obtener_producto_por_id(self, ID_P):
        try:
            # Ejecutar una consulta para obtener los datos del producto por su ID
            self.cursor.execute("SELECT * FROM productos WHERE ID_P = ?", (ID_P,))
            producto = self.cursor.fetchone()
            return producto
        except sqlite3.Error as e:
            print("Error al obtener producto por ID:", e)
            return None    

    def restar_cantidad_producto(self, ID_P, cantidad_vendida):
        try:
            # Obtener la cantidad disponible del producto
            self.cursor.execute("SELECT cantidad FROM productos WHERE ID_P = ?", (ID_P,))
            resultado = self.cursor.fetchone()
            if resultado is None:
                print(f"No se encontró ningún producto con el ID {ID_P}.")
                return
    
            cantidad_disponible = resultado[0]
    
            # Calcular la nueva cantidad después de la venta
            nueva_cantidad = cantidad_disponible - cantidad_vendida
    
            # Actualizar la cantidad en la tabla de productos
            self.cursor.execute("UPDATE productos SET cantidad = ? WHERE ID_P = ?", (nueva_cantidad, ID_P))
            self.connection.commit()
            print("Cantidad actualizada correctamente.")
        except sqlite3.Error as e:
            print("Error al restar cantidad de producto:", e)   

    def insertar_salida(self, ID_P, precio_venta, precio_bs, cantidad_vendida, CEDULA):
            try:
                # Obtener la fecha y hora actual
                fecha_actual = datetime.date.today()
                hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    
                # Ejecutar la consulta SQL para insertar los datos de la salida
                self.cursor.execute("INSERT INTO ventas (ID_P, fecha, hora, precio_vent, precio_bs, CEDULA) VALUES (?, ?, ?, ?, ?, ?)",
                                    (ID_P, fecha_actual, hora_actual, precio_venta, precio_bs, CEDULA))
                self.connection.commit()  # Confirmar la transacción
                
                # Restar la cantidad vendida de la tabla de productos
                self.restar_cantidad_producto(ID_P, cantidad_vendida)
                
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
        
    def actualizar_cantidad_producto(self, ID_P, nueva_cantidad):
        try:
            # Ejecutar la consulta SQL para actualizar la cantidad del producto
            self.cursor.execute("UPDATE productos SET cantidad = ? WHERE ID_P = ?", (nueva_cantidad, ID_P))
            self.connection.commit()  # Confirmar la transacción
            print("Cantidad del producto actualizada correctamente.")
        except sqlite3.Error as e:
            print("Error al actualizar la cantidad del producto:", e)    
    
    def existe_producto(self, nombre, marca, modelo):
        try:
            # Convertir los parámetros a minúsculas para normalizar
            nombre = nombre.lower()
            marca = marca.lower()
            modelo = modelo.lower()

            # Ejecutar una consulta para verificar si el producto existe en la base de datos
            self.cursor.execute("SELECT COUNT(*) FROM productos WHERE LOWER(nombre) = ? AND LOWER(marca) = ? AND LOWER(modelo) = ?", (nombre, marca, modelo))
            count = self.cursor.fetchone()[0]
            return count > 0  # Devuelve True si el producto existe, False si no
        except sqlite3.Error as e:
            print("Error al verificar si el producto existe:", e)
            return False        
            
    def insertar_usuario(self, username, nombre, password, repetir_contraseña, tipo=None):
        try:
            # Verificar si las contraseñas coinciden
            if password != repetir_contraseña:
                print("Las contraseñas no coinciden.")
                return False

            # Verificar el tipo seleccionado y asignar el valor correspondiente
            tipo = "administrador" if tipo == "administrador" else "normal"
            # Insertar los datos en la tabla 'user'
            self.cursor.execute("INSERT INTO user (username, nombre, password, tipo) VALUES (?, ?, ?, ?)", (username, nombre, password, tipo))
            # Confirmar la transacción
            self.connection.commit()
            print("Usuario registrado exitosamente.")
            return True
        except sqlite3.Error as e:
            print("Error al insertar usuario:", e)
            return False
    
    def cargar_datos(self, username, password):
        try:
            # Ejecutar una consulta para verificar las credenciales del usuario
            self.cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?", (username, password))
            usuario = self.cursor.fetchone()
    
            if usuario:
                # Si se encuentra un usuario con las credenciales proporcionadas, retornar los datos del usuario
                return usuario
            else:
                # Si no se encuentra ningún usuario con las credenciales proporcionadas, retornar None
                return None
        except sqlite3.Error as e:
            # Manejar cualquier error de la base de datos
            print("Error al autenticar usuario:", e)
            return None
    
    def obtener_usuarios(self):
        try:
            self.cursor.execute("SELECT * FROM user")
            usuarios = self.cursor.fetchall()
            return usuarios
        except sqlite3.Error as e:
            print("Error al obtener los usuarios:", e)
            return None

    def eliminar_usuario(self, ID_U):
        try:
            self.cursor.execute("DELETE FROM user WHERE ID_U = ?", (ID_U,))
            self.connection.commit()  # Confirmar la transacción
            print("Usuario eliminado correctamente.")
        except sqlite3.Error as e:
            print("Error al eliminar usuario:", e)    

    def obtener_ventas_d(self):
        try:
            self.cursor.execute("SELECT ID_V, fecha, hora, precio_vent, precio_bs FROM ventas_d")
            ventas_d = self.cursor.fetchall()
            return ventas_d
        except sqlite3.Error as e:
            print("Error al obtener las ventas diarias:", e)
            return None
        
    def usuario_existe(self, username):
        try:
            # Realizar la consulta para verificar si el usuario existe
            # Suponiendo que tu tabla de usuarios se llama 'user' y el campo de nombre de usuario 'username'
            query = "SELECT COUNT(*) FROM user WHERE username = ?"
            self.cursor.execute(query, (username,))
            resultado = self.cursor.fetchone()[0]

            # Si resultado es mayor que 0, significa que el usuario ya existe
            return resultado > 0
        except sqlite3.Error as e:
            print("Error al verificar si el usuario existe:", e)
            return False    
        
    def actualizar_producto(self, nombre_antiguo, nuevo_nombre, nuevo_modelo, nueva_marca, nueva_cantidad, nuevo_precio):
        try:
            # Realizar la actualización en la base de datos
            self.cursor.execute("UPDATE productos SET nombre = ?, modelo = ?, marca = ?, cantidad = ?, precio_unitario = ? WHERE nombre = ?", 
                                (nuevo_nombre, nuevo_modelo, nueva_marca, nueva_cantidad, nuevo_precio, nombre_antiguo))
            # Confirmar la transacción
            self.connection.commit()
            print("Producto actualizado correctamente.")
        except sqlite3.Error as e:
            print("Error al actualizar producto:", e)
                        