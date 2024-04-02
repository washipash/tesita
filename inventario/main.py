import sys
import requests
import pandas as pd
from openpyxl import Workbook
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate , QBuffer, QByteArray , QTime
from PyQt5.QtGui import QImage,QPixmap 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QIODevice, QDateTime, Qt
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget ,QApplication ,QMainWindow,QStackedWidget,QGraphicsDropShadowEffect, QCalendarWidget , QBoxLayout
from PyQt5.QtWidgets import QMessageBox,QLabel,QTableWidgetItem, QLineEdit
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QTimer  
from PyQt5.QtGui import QMovie
import hashlib
import sqlite3
from bs4 import BeautifulSoup
import os
import json
import re
import openpyxl
import datetime
from datetime import datetime
from añadir_prod import VentanaAnadirProducto
from conection import DatabaseManager 
from PyQt5.QtCore import Qt
 
class IngresoUsuario(QDialog):
    def __init__(self, ventana_registro):
        super(IngresoUsuario, self).__init__()
        self.ventana_registro = ventana_registro
        loadUi(r"qt\login.ui", self)
        self.setWindowTitle("Login")
        self.user_btn.clicked.connect(self.ingreso)
        self.close_btn.clicked.connect(self.salida)
        self.register_btn.clicked.connect(self.abrir_registro)
        self.pass_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ventana_registro.usuario_registrado.connect(self.abrir_ingreso)
        self.ingresoAnterior()
        
    def abrir_ingreso(self):
        # Crear una nueva instancia de la ventana de inicio de sesión
        self.ventana_ingreso = IngresoUsuario()
        # Mostrar la ventana de inicio de sesión
        self.ventana_ingreso.show()    
        
    def ingresoAnterior(self):
        usuario, _ = self.cargar_datos_acceso()
        if usuario:
            self.txt_username.setText(usuario)
            self.txt_password.setFocus()
        else:
            print("No se encontraron datos de acceso almacenados.")

    def salida(self):
        reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Desea Salir?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.Yes:
            QApplication.quit()

    def authenticate_user(self, username, password):
        # Implementa la autenticación del usuario
        conexion = sqlite3.connect(r"recursos\bd\db.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM User WHERE nombre = ? AND contraseña = ?", (username, password))
        usuario = cursor.fetchone()
        conexion.close()

        if usuario:
            # Usuario autenticado
            # Aquí puedes abrir la ventana principal
            ventana_principal = VentanaPrincipal()
            ventana_principal.show()
            self.close()  # Cierra la ventana de inicio de sesión
        else:
            QMessageBox.warning(self, "Error", "Nombre de usuario o contraseña incorrectos.")

    def ingreso(self):
       nombre = self.name_edit.text()
       password = self.pass_edit.text()
       self.authenticate_user(nombre, password)
       self.guardar_datos_acceso(nombre, password)
       print("Datos de acceso guardados exitosamente.")

    def guardar_datos_acceso(self, usuario):
        with open("datos_acceso.json", "w") as archivo:
            json.dump({"usuario": usuario}, archivo)

    def cargar_datos_acceso(self):
        try:
            with open("datos_acceso.json", "r") as archivo:
                datos_acceso = json.load(archivo)
                return datos_acceso["usuario"], None
        except FileNotFoundError:
            return None, None
        
    def abrir_registro(self):
        # Cerrar la ventana actual de inicio de sesión
        self.close()
        
        # Abrir la ventana de registro
        self.ventana_registro.exec_()
    
    def abrir_principal(self):
        # Crear una instancia de VentanaPrincipal con el objeto db_manager como argumento
        ventana_principal = VentanaPrincipal(self.db_manager)
        ventana_principal.show()
        # Volver a abrir la ventana principal
        self.show()

class Registro(QDialog):
    usuario_registrado = pyqtSignal()
    def __init__(self):
        super(Registro, self).__init__()
        loadUi(r"qt\register.ui", self)
        self.done_r_btn.clicked.connect(self.registrarUsuario)
        self.close_r_btn.clicked.connect(self.close)

    def registrarUsuario(self):
        nombre = self.name_user_line.text()
        contraseña = self.pass_user_line.text()
        nueva_contraseña = self.new_pass_user_line.text()

        if not nombre or not contraseña or not nueva_contraseña:
            QMessageBox.critical(self, "Error", "Por favor, complete todos los campos.")
            return

        if contraseña != nueva_contraseña:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden.")
            return

        if self.usuario_existe(nombre):
            QMessageBox.warning(self, "Error", "El nombre de usuario ya existe.")
            return

        # Conectar a la base de datos
        conexion = sqlite3.connect(r"recursos\bd\db.db")
        cursor = conexion.cursor()

        # Insertar los datos en la tabla 'user'
        cursor.execute("INSERT INTO user (nombre, contraseña) VALUES (?, ?)", (nombre, contraseña))

        # Confirmar la transacción
        conexion.commit()

        # Cerrar la conexión con la base de datos
        conexion.close()

        QMessageBox.information(self, "Éxito", "Usuario registrado exitosamente.")
         # Emitir la señal de usuario registrado cuando se complete el registro
        self.usuario_registrado.emit()

        # Cerrar la ventana de registro
        self.close()

    def usuario_existe(self, username):
        # Implementa la lógica para verificar si el usuario ya existe en la base de datos
        return False  # Cambia esto con la lógica real de tu aplicación 
      
class VentanaVentasDiarias(QtWidgets.QDialog):
    def __init__(self):
        super(VentanaVentasDiarias, self).__init__()
        loadUi(r"qt\ventas_diarias.ui", self) 

class Ventanabuscarventa(QtWidgets.QDialog):
    def __init__(self):
        super(Ventanabuscarventa, self).__init__()
        loadUi(r"qt\buscar_venta.ui", self)
 
class eliminarventa(QtWidgets.QDialog):
    def __init__(self):
        super(eliminarventa, self).__init__()
        loadUi(r"qt\eliminar_venta.ui", self)  

class ventanaeditarproducto(QtWidgets.QDialog):
    def __init__(self):
        super(ventanaeditarproducto, self).__init__()
        loadUi(r"qt\actualizar_prod.ui", self)                   

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, db_manager):
        super(VentanaPrincipal, self).__init__()
        loadUi(r"qt\invUI.ui", self)
        self.setWindowTitle('Inventario SmartTech Store')  
        self.paginaInicia = True
        self.db_manager = db_manager  # Guarda una referencia al objeto db_manager
        self.mostrarPaginaProductos()  # Corregir aquí
        self.mostrar_datos_productos()
        self.total_v_line.setReadOnly(True)  # Hacer que el QLineEdit sea de solo lectura
        self.total_bs_line.setReadOnly(True)  # Hacer que el QLineEdit sea de solo lectura
        self.table_prod_comprados = self.findChild(QtWidgets.QTableWidget, "table_prod_comprados")# Después de cargar la interfaz de usuario en el constructor
        self.tasa_edit.textChanged.connect(self.actualizar_precios_bs)     
        self.prod_name_edit.editingFinished.connect(self.actualizar_nombre) # Conectar señales y ranuras para manejar la entrada de texto en los line edits
        self.id_prod_edit.editingFinished.connect(self.actualizar_id)   
        self.insertar_gif_en_label() # Insertar GIF en el QLabel     
        self.actualizar_hora_fecha() # Actualizar la hora y el día cada segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_hora_fecha)
        self.timer.start(1000)
        self.add_btn.clicked.connect(self.abrir_ventana_anadir_producto)      
        self.inicio_btn.clicked.connect(self.mostrarPaginaInicio)
        self.Productos_btn.clicked.connect(self.mostrarPaginaProductos)
        self.ventas_btn.clicked.connect(self.mostrarPaginaVentas)
        self.reparacion_btn.clicked.connect(self.mostrarPaginaReparaciones)
        self.ayuda_btn.clicked.connect(self.mostrarPaginaayuda)
        self.buscar_venta_btn.clicked.connect(self.abrir_buscar_ventas)
        self.delete_btn.clicked.connect(self.abrir_eliminar_venta)
        self.cierre_btn.clicked.connect(self.abrir_ventas_diarias)
        self.clear_btn.clicked.connect(self.eliminar_fila)
        self.clear_f_btn.clicked.connect(self.eliminar_fila_v)
        self.clear_venta_btn.clicked.connect(self.eliminar_todas_las_filas)       
        self.frame_controls.setVisible(True)  # Inicialmente, el frame está oculto       
        self.btn_menu.clicked.connect(self.toggle_frame_controls)
        self.add_v_btn.clicked.connect(self.salida_producto)  # Conectar el botón "Agregar"
        self.save_v_btn.clicked.connect(self.guardar_salida)# Conexión del botón al método para guardar la salida desde el QTableWidget
        self.act_name_btn.clicked.connect(self.ordenar_por_nombre)      
        self.act_marca_btn.clicked.connect(self.ordenar_por_marca)        
        self.act_modelo_btn.clicked.connect(self.ordenar_por_modelo)
        self.edit_p_btn.clicked.connect(self.abrir_ventana_editar_producto)

    def ordenar_por_nombre(self):
        self.ordenar_tabla(1)

    def ordenar_por_marca(self):
        self.ordenar_tabla(3)

    def ordenar_por_modelo(self):
        self.ordenar_tabla(2)

    def ordenar_tabla(self, columna):
        self.table_prod.sortItems(columna, QtCore.Qt.AscendingOrder)
        
    def actualizar_id(self):
    # Método para actualizar el ID del producto según el nombre ingresado
     nombre = self.prod_name_edit.text()
     if nombre:
        # Buscar el ID del producto en la tabla de productos
        for row in range(self.table_prod.rowCount()):
            if self.table_prod.item(row, 1).text() == nombre:
                ID_P = self.table_prod.item(row, 0).text()
                self.id_prod_edit.setText(ID_P)
                break

    def actualizar_nombre(self):
    # Método para actualizar el nombre del producto según el ID ingresado
     ID_P = self.id_prod_edit.text()
     if ID_P:
        # Buscar el nombre del producto en la tabla de productos
        for row in range(self.table_prod.rowCount()):
            if self.table_prod.item(row, 0).text() == ID_P:
                nombre_producto = self.table_prod.item(row, 1).text()
                self.prod_name_edit.setText(nombre_producto)
                break

    def salida_producto(self):
        id_producto = self.id_prod_edit.text()
        nombre = self.prod_name_edit.text()
        cantidad = self.cant_prod.text()
    
        if not nombre:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Ingrese el nombre del producto.")
            return
    
        if not cantidad:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Ingrese la cantidad del producto.")
            return
    
        producto = self.db_manager.obtener_producto_por_nombre(nombre)
    
        if producto is not None:
            cantidad_disponible = producto[4]
    
            if int(cantidad) > cantidad_disponible:
                QtWidgets.QMessageBox.warning(self, "Advertencia", "La cantidad ingresada es mayor que la cantidad disponible.")
                return
        
            
        
            marca = producto[2]
            modelo = producto[3]
            precio_unitario = producto[5]
    
            precio_venta = float(precio_unitario) * int(cantidad)
            tasa_text = self.tasa_edit.text()
    
            try:
                tasa = float(tasa_text)
            except ValueError:
                QtWidgets.QMessageBox.warning(self, "Advertencia", "Ingrese una tasa válida.")
                return
    
            precio_bs = precio_venta * tasa
    
            # Insertar fila en la tabla de productos comprados
            row_position = 0  # Insertar en la primera posición
            self.table_prod_comprados.insertRow(row_position)
            self.table_prod_comprados.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(producto[0])))
            self.table_prod_comprados.setItem(row_position, 1, QtWidgets.QTableWidgetItem(nombre))
            self.table_prod_comprados.setItem(row_position, 2, QtWidgets.QTableWidgetItem(marca))
            self.table_prod_comprados.setItem(row_position, 3, QtWidgets.QTableWidgetItem(modelo))
            self.table_prod_comprados.setItem(row_position, 4, QtWidgets.QTableWidgetItem(cantidad))
            self.table_prod_comprados.setItem(row_position, 5, QtWidgets.QTableWidgetItem(str(precio_unitario)))
            self.table_prod_comprados.setItem(row_position, 6, QtWidgets.QTableWidgetItem(str(precio_venta)))
            self.table_prod_comprados.setItem(row_position, 7, QtWidgets.QTableWidgetItem(str(precio_bs)))
    
            # Calcular la suma de los valores en la columna 6 (precio de venta)
            total_venta = 0.0
            for row in range(self.table_prod_comprados.rowCount()):
                precio_venta_text = self.table_prod_comprados.item(row, 6).text()
                if precio_venta_text:
                    try:
                        precio_venta = float(precio_venta_text)
                        total_venta += precio_venta
                    except ValueError:
                        QtWidgets.QMessageBox.warning(self, "Advertencia", "Error al convertir el precio de venta a número flotante.")
                        return
                    
            # Calcular la suma de los valores en la columna 7 (precio bs)
            total_bs_venta = 0.0
            for row in range(self.table_prod_comprados.rowCount()):
                precio_venta_bs_text = self.table_prod_comprados.item(row, 7).text()
                if precio_venta_bs_text:
                    try:
                        precio_bs = float(precio_venta_bs_text)
                        total_bs_venta += precio_bs
                    except ValueError:
                        QtWidgets.QMessageBox.warning(self, "Advertencia", "Error al convertir el precio de venta a número flotante.")
                        return        
    
            # Actualizar el QLineEdit con el total de la venta
            self.total_v_line.setText(str(total_venta))
            self.total_bs_line.setText(str(total_bs_venta))
    
            # Limpiar los campos de entrada
            self.prod_name_edit.clear()
            self.cant_prod.clear()
    
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Producto no encontrado.")
    
        try:
            # Actualizar la cantidad del producto en la base de datos
                nueva_cantidad = cantidad_disponible - int(cantidad)
                self.db_manager.actualizar_cantidad_producto(nombre, nueva_cantidad)
                print("Cantidad del producto actualizada correctamente en la base de datos.")
        except Exception as e:
                print("Error al actualizar la cantidad del producto:", e)
    
    def guardar_salida(self):
        num_filas = self.table_prod_comprados.rowCount()
    
        # Verificar si hay datos en el QTableWidget
        if num_filas == 0:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No hay productos en la lista para guardar la salida.")
            return
        
        # Obtener los precios de venta y bs de los QLineEdits
        precio_venta = float(self.total_v_line.text())
        precio_bs = float(self.total_bs_line.text())
    
        # Recorrer las filas del QTableWidget y obtener los datos
        for columna in range(num_filas):
            id_producto_item = self.table_prod_comprados.item(columna, 1)
            
            # Verificar si alguno de los ítems es None
            if id_producto_item is None:
                QtWidgets.QMessageBox.warning(self, "Advertencia", f"Faltan datos en la fila {columna+1}.")
                return
    
            id_producto = id_producto_item.text()
            
            # Obtener la cantidad vendida desde la columna 5 (Cantidad) de la tabla
            cantidad_vendida_item = self.table_prod_comprados.item(columna, 4)
            if cantidad_vendida_item is None:
                QtWidgets.QMessageBox.warning(self, "Advertencia", f"Falta la cantidad vendida en la columna {columna+1}.")
                return
            cantidad_vendida = int(cantidad_vendida_item.text())
    
            # Llamada al método insertar_salida con los argumentos necesarios, incluida cantidad_vendida
            self.db_manager.insertar_salida(id_producto, precio_venta, precio_bs, cantidad_vendida)
    
        # Limpiar el QTableWidget después de guardar la salida
        self.table_prod_comprados.setRowCount(0)
    
        # Limpiar los campos de total_v_line y total_bs_line
        self.total_v_line.clear()
        self.total_bs_line.clear()
        
    def setup_ui(self):
        
        # Supongamos que self.table_prod_comprados es tu tabla donde deseas eliminar filas
        self.table_prod_comprados = QtWidgets.QTableWidget(self)
        
        # Supongamos que self.eliminar_btn es tu botón para eliminar filas
        self.clear_f_btn = QtWidgets.QPushButton("Eliminar fila", self)
        
    def eliminar_fila_v(self):
        # Obtener la fila seleccionada
        selected_row = self.table_prod_comprados.currentRow()
        
        # Verificar si se ha seleccionado una fila
        if selected_row >= 0:
            # Obtener el ID de la fila seleccionada (asumiendo que el ID está en la primera columna)
            id_fila = self.table_prod_comprados.item(selected_row, 0).text()  # Suponiendo que el ID es de tipo texto
            
            # Eliminar la fila de la tabla
            self.table_prod_comprados.removeRow(selected_row)
        else:
            # Si no se seleccionó ninguna fila, mostrar un mensaje de advertencia
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Por favor, seleccione una fila para eliminar.")    
        
    # Definir la función eliminar_todas_las_filas para limpiar todas las filas de la tabla table_prod_comprados
    def eliminar_todas_las_filas(self):
        # Obtener el número total de filas en la tabla
        total_filas = self.table_prod_comprados.rowCount()
    
        # Eliminar todas las filas de la tabla
        for row in range(total_filas):
            self.table_prod_comprados.removeRow(0)  # Siempre eliminamos la primera fila (índice 0) porque después de eliminar una fila, las filas restantes se desplazan hacia arriba    
        
            # Limpiar los QLineEdit total_v y total_bs
            self.total_v_line.clear()
            self.total_bs_line.clear()
          
    def toggle_frame_controls(self):
        if self.frame_controls.isVisible():
            # Si el frame está visible, lo ocultamos hacia la izquierda
            self.frame_controls.setVisible(False)
            self.frame_controls.setGeometry(-self.frame_controls.width(), 0, self.frame_controls.width(), self.frame_controls.height())
        else:
            # Si el frame está oculto, lo mostramos deslizándolo desde la izquierda
            self.frame_controls.setGeometry(0, 0, self.frame_controls.width(), self.frame_controls.height())
            self.frame_controls.setVisible(True)    
        
            
        # Conectar el evento de cambio de valor del tasa_edit a la función actualizar_precios_bs
        self.tasa_edit.textChanged.connect(self.actualizar_precios_bs)
# Método para actualizar los precios en bolívares soberanos (bs) en la tabla de productos
    def actualizar_precios_bs(self):
        # Obtener el valor de la tasa del tasa_edit
        tasa_text = self.tasa_edit.text()
        try:
            tasa = float(tasa_text)
        except ValueError:
            # Manejar el caso en que el valor de la tasa no sea un número válido
            return

        # Iterar sobre todas las filas de la tabla de productos
        for row in range(self.table_prod.rowCount()):
            # Obtener el precio en la columna correspondiente
            precio_str = self.table_prod.item(row, 5).text()  # Suponiendo que la columna del precio es la número 4
            try:
                precio = float(precio_str)
            except ValueError:
                # Manejar el caso en que el precio no sea un número válido
                continue

            # Calcular el precio_bs para el producto actual
            precio_bs = precio * tasa

            # Mostrar el precio_bs en la columna correspondiente de la tabla de productos
            item_bs = QtWidgets.QTableWidgetItem(str(precio_bs))
            self.table_prod.setItem(row, 6, item_bs)  # Suponiendo que la columna del precio_bs es la número 5

            # Actualizar la base de datos con el nuevo precio_bs
            id_producto = int(self.table_prod.item(row, 0).text())  # Suponiendo que el ID del producto está en la columna número 0
            self.db_manager.actualizar_precio_bs(id_producto, precio_bs)

 # Configura la imagen en el QLabel
        pixmap = QtGui.QPixmap(r"recursos\img\smart.png")  # Cambia la ruta por la de tu imagen
        # Cambia el tamaño de la imagen
        scaled_pixmap = pixmap.scaled(200, 200)  # Cambia 200, 200 por el tamaño deseado
        self.img_label.setPixmap(pixmap)

        # Configura la imagen en el QLabel
        pixmap = QtGui.QPixmap(r"recursos\img\manual.png")  # Cambia la ruta por la de tu imagen
        # Cambia el tamaño de la imagen
        scaled_pixmap = pixmap.scaled(200, 200)  # Cambia 200, 200 por el tamaño deseado
        self.manual_label.setPixmap(pixmap)

    def insertar_gif_en_label(self):
        # Crear un objeto QMovie para el GIF
        movie = QtGui.QMovie(r"recursos\img\maxwell.gif")

        # Establecer el objeto QMovie en el QLabel
        self.gif_label.setMovie(movie)

        # Iniciar la reproducción del GIF
        movie.start()

    def actualizar_hora_fecha(self):
        # Obtener la fecha y hora actual
        ahora = QDateTime.currentDateTime()

        # Formatear la hora actual como "HH:mm:ss"
        hora_texto = ahora.toString("HH:mm:ss")

        # Formatear el día de la semana y la fecha como "Día, DD de Mes de Año"
        fecha_texto = ahora.toString("dddd, d 'de' MMMM 'de' yyyy")

        # Mostrar la hora y la fecha en los QLabel correspondientes
        self.hora_label.setText("Hora actual: " + hora_texto)
        self.dia_label.setText("Fecha actual: " + fecha_texto)

    # Métodos para cambiar de página
    def mostrarPaginaInicio(self):
        self.stackedWidget.setCurrentWidget(self.page_inicio)



    def mostrarPaginaVentas(self):
        self.stackedWidget.setCurrentWidget(self.page_ventas)

    def mostrarPaginaReparaciones(self):
        self.stackedWidget.setCurrentWidget(self.page_reparaciones)

    def mostrarPaginaayuda(self):
        self.stackedWidget.setCurrentWidget(self.page_ayuda)

    # Método para abrir la ventana de añadir producto
    def abrir_ventana_anadir_producto(self):
     ventana_anadir_producto = VentanaAnadirProducto(self.db_manager, self.actualizar_datos_tabla)
     ventana_anadir_producto.exec_()
     
    def abrir_ventana_editar_producto(self):
     ventana_editar_producto = ventanaeditarproducto()
     ventana_editar_producto.exec_() 

    # Método para abrir la ventana de ventas diarias
    def abrir_ventas_diarias(self):
        ventana_ventas_diarias = VentanaVentasDiarias()
        ventana_ventas_diarias.exec_()

    def abrir_buscar_ventas(self):
        ventana_buscar_ventas = Ventanabuscarventa()
        ventana_buscar_ventas.exec_()

    def abrir_eliminar_venta(self):
        eliminar_venta = eliminarventa()
        eliminar_venta.exec_()

    def abrir_eliminar_venta(self):
        eliminar_venta = eliminarventa()
        eliminar_venta.exec_()

    def mostrarPaginaProductos(self):
        # Llamar a la función para mostrar los datos de los productos
        self.mostrar_datos_productos()
        self.stackedWidget.setCurrentWidget(self.page_productos)

    def actualizar_datos_tabla(self):
        self.mostrar_datos_productos()
     

    def mostrar_datos_productos(self):  # Define el método dentro de la clase
        try:
            # Obtener los datos de la tabla productos de la base de datos
            productos = self.db_manager.obtener_productos()

            # Limpiar la tabla antes de insertar nuevos datos
            self.table_prod.setRowCount(0)

            # Insertar los datos en la tabla table_prod
            for row_number, row_data in enumerate(productos):
                self.table_prod.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.table_prod.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        except Exception as e:
            print("Error al obtener productos:", e)
            
    def setup_ui(self):
        # Supongamos que self.table_prod es tu tabla donde deseas eliminar filas
        self.table_prod = QtWidgets.QTableWidget(self)
        
        # Supongamos que self.eliminar_btn es tu botón para eliminar filas
        self.eliminar_btn = QtWidgets.QPushButton("Eliminar fila", self)
        
    def eliminar_fila(self):
        # Obtener la fila seleccionada
        selected_row = self.table_prod.currentRow()
        
        # Verificar si se ha seleccionado una fila
        if selected_row >= 0:
            # Obtener el ID de la fila seleccionada (asumiendo que el ID está en la primera columna)
            id_fila = self.table_prod.item(selected_row, 0).text()  # Suponiendo que el ID es de tipo texto
            
            # Eliminar la fila de la base de datos utilizando el ID obtenido
            self.eliminar_fila_base_datos(id_fila)
            
            # Eliminar la fila de la tabla
            self.table_prod.removeRow(selected_row)
        else:
            # Si no se seleccionó ninguna fila, mostrar un mensaje de advertencia
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Por favor, seleccione una fila para eliminar.")
    
    def eliminar_fila_base_datos(self, id_fila):
    # Eliminar la fila de la base de datos utilizando el método eliminar_producto
     self.db_manager.eliminar_producto(id_fila)  # Utilizando el ID recibido
          
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("inventario")
    # Crear una instancia de DatabaseManager y conectar a la base de datos
    db_manager = DatabaseManager(r"recursos\bd\db.db")
    ventana_registro = Registro()
    ventana_ingreso = IngresoUsuario(ventana_registro)
    ventana_ingreso.show()
    ventana_registro.usuario_registrado.connect(ventana_ingreso.abrir_ingreso)
    # Pasar la instancia de DatabaseManager a la ventana principal
    ventana_principal = VentanaPrincipal(db_manager)
    ventana_principal.show()
    ventana_principal.showMaximized()  # Mostrar la ventana en pantalla completa
    icon = QIcon(r"recursos\img\smart.png")
    sys.exit(app.exec_())