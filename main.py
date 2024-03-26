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
from PyQt5.QtCore import QTimer  
from PyQt5.QtGui import QMovie
import hashlib
import sqlite3
from bs4 import BeautifulSoup
import os
import datetime
from añadir_prod import VentanaAnadirProducto
from conection import DatabaseManager # Importa la clase DatabaseManager desde el archivo database_manager.py
from PyQt5.QtCore import Qt

    
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

class editarproducto(QtWidgets.QDialog):
    def __init__(self):
        super(editarproducto, self).__init__()
        loadUi(r"qt\actualizar_prod.ui", self)                   

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, db_manager):
        super(VentanaPrincipal, self).__init__()
        loadUi(r"qt\invUI.ui", self)
        self.db_manager = db_manager  # Guarda una referencia al objeto db_manager
        self.mostrarPaginaProductos()  # Corregir aquí
        self.total_v_line.setReadOnly(True)  # Hacer que el QLineEdit sea de solo lectura
        self.total_bs_line.setReadOnly(True)  # Hacer que el QLineEdit sea de solo lectura
        self.paginaInicia = True
        self.mostrar_datos_productos()
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
        self.save_v_btn.clicked.connect(self.guardar_venta) # Conectar el botón save_v_btn a la función guardar_venta
        self.frame_controls.setVisible(True)  # Inicialmente, el frame está oculto       
        self.btn_menu.clicked.connect(self.toggle_frame_controls)
        self.prod_name_edit.editingFinished.connect(self.actualizar_nombre) # Conectar señales y ranuras para manejar la entrada de texto en los line edits
        self.id_prod_edit.editingFinished.connect(self.actualizar_id)   
        self.add_v_btn.clicked.connect(self.salida_producto)  # Conectar el botón "Agregar"
        self.table_prod_comprados = self.findChild(QtWidgets.QTableWidget, "table_prod_comprados")# Después de cargar la interfaz de usuario en el constructor
        self.tasa_edit.textChanged.connect(self.actualizar_precios_bs)
        self.insertar_gif_en_label() # Insertar GIF en el QLabel     
        self.actualizar_hora_fecha() # Actualizar la hora y el día cada segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_hora_fecha)
        self.timer.start(1000)
        
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
        # Generar un ID único de tres dígitos
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
        pixmap = QtGui.QPixmap(r"recursos\img\icons\smart.png")  # Cambia la ruta por la de tu imagen
        # Cambia el tamaño de la imagen
        scaled_pixmap = pixmap.scaled(200, 200)  # Cambia 200, 200 por el tamaño deseado
        self.img_label.setPixmap(pixmap)

        # Configura la imagen en el QLabel
        pixmap = QtGui.QPixmap(r"recursos\img\icons\manual.png")  # Cambia la ruta por la de tu imagen
        # Cambia el tamaño de la imagen
        scaled_pixmap = pixmap.scaled(200, 200)  # Cambia 200, 200 por el tamaño deseado
        self.manual_label.setPixmap(pixmap)

    def insertar_gif_en_label(self):
        # Crear un objeto QMovie para el GIF
        movie = QtGui.QMovie(r"recursos\img\icons\maxwell.gif")

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

    def abrir_editar_producto(self):
        editar_producto = editarproducto()
        editar_producto.exec_()

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
     
    def guardar_venta(self):
        try:
            # Generar un nuevo ID único para la venta (suponiendo que ID_V es autoincremental)
            nuevo_id_venta = self.db_manager.obtener_ultimo_id_venta() + 1
    
            # Obtener el total de la venta y la hora actual
            total_venta = self.total_v_line.text()
            total_bs = self.total_bs_line.text()
            hora_actual = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
    
            # Insertar los datos de la venta en la tabla ventas_v
            self.db_manager.insertar_venta(nuevo_id_venta, hora_actual, total_venta, total_bs)
    
            # Limpiar la tabla de productos comprados y los campos de total
            self.table_prod_comprados.clearContents()
            self.table_prod_comprados.setRowCount(0)
            self.total_v_line.clear()
            self.total_bs_line.clear()
    
            print("Venta guardada correctamente.")
        except Exception as e:
            print("Error al insertar venta:", e)
     
     
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("inventario")
    # Crear una instancia de DatabaseManager y conectar a la base de datos
    db_manager = DatabaseManager(r"recursos\bd\db.db")
    # Pasar la instancia de DatabaseManager a la ventana principal
    ventana_principal = VentanaPrincipal(db_manager)
    ventana_principal.show()
    ventana_principal.showMaximized()  # Mostrar la ventana en pantalla completa
    icon = QIcon("")
    sys.exit(app.exec_())