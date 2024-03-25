import sys
import requests
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
        self.add_btn.clicked.connect(self.abrir_ventana_anadir_producto)      
        self.inicio_btn.clicked.connect(self.mostrarPaginaInicio)
        self.Productos_btn.clicked.connect(self.mostrarPaginaProductos)
        self.ventas_btn.clicked.connect(self.mostrarPaginaVentas)
        self.reparacion_btn.clicked.connect(self.mostrarPaginaReparaciones)
        self.ayuda_btn.clicked.connect(self.mostrarPaginaayuda)
        self.buscar_venta_btn.clicked.connect(self.abrir_buscar_ventas)
        self.delete_btn.clicked.connect(self.abrir_eliminar_venta)
        self.paginaInicia = True
        self.mostrar_datos_productos()
        self.cierre_btn.clicked.connect(self.abrir_ventas_diarias)
        self.clear_btn.clicked.connect(self.eliminar_fila)
        self.frame_controls.setVisible(True)  # Inicialmente, el frame está oculto       
        self.btn_menu.clicked.connect(self.toggle_frame_controls)
        # Conectar señales y ranuras para manejar la entrada de texto en los line edits
        self.prod_name_edit.editingFinished.connect(self.actualizar_nombre)
        self.id_prod_edit.editingFinished.connect(self.actualizar_id)
        # Conectar el botón "Agregar"
        self.add_v_btn.clicked.connect(self.agregar_producto)
        # Después de cargar la interfaz de usuario en el constructor
        self.table_prod_comprados = self.findChild(QtWidgets.QTableWidget, "table_prod_comprados")
        
                # Insertar GIF en el QLabel
        self.insertar_gif_en_label()
     # Actualizar la hora y el día cada segundo
        self.actualizar_hora_fecha()
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
                 id_producto = self.table_prod.item(row, 0).text()
                 self.id_prod_edit.setText(id_producto)
                 break

    def actualizar_nombre(self):
        # Método para actualizar el nombre del producto según el ID ingresado
        id_producto = self.id_prod_edit.text()
        if id_producto:
            # Buscar el nombre del producto en la tabla de productos
            for row in range(self.table_prod.rowCount()):
                if self.table_prod.item(row, 0).text() == id_producto:
                    nombre_producto = self.table_prod.item(row, 1).text()
                    self.prod_name_edit.setText(nombre_producto)
                    break
    
    def agregar_producto(self):
        # Método para agregar el producto a la tabla de productos comprados
        id_producto = self.id_prod_edit.text()    
        nombre = self.prod_name_edit.text()
        cantidad = self.cant_prod.text()
    
        if not nombre and not id_producto:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Ingrese el nombre o el ID del producto.")
            return
    
        if not cantidad:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Ingrese la cantidad del producto.")
            return
    
           # Obtener los datos del producto desde la base de datos
        producto = self.db_manager.obtener_producto_por_nombre(nombre)

        if producto is not None:  # Verificar si se encontró el producto
            # Validar que la cantidad no sea mayor que la cantidad disponible
            cantidad_disponible = producto[4]  # Obtener la cantidad disponible del producto
            if int(cantidad) > cantidad_disponible:
                QtWidgets.QMessageBox.warning(self, "Advertencia", "La cantidad ingresada es mayor que la cantidad disponible.")
                return
    
            # Obtener los datos adicionales del producto
        marca = producto[2]  # Marca del producto
        modelo = producto[3]  # Modelo del producto
        precio_unitario = producto[5]  # Precio unitario del producto

        # Calcular el precio de venta
        precio_venta = float(precio_unitario) * int(cantidad)

        # Obtener la tasa del tasa_edit
        tasa_text = self.tasa_edit.text()
        try:
            tasa = float(tasa_text)
        except ValueError:
            # Manejar el caso en que el valor de la tasa no sea un número válido
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Ingrese una tasa válida.")
            return

        # Calcular el precio en bolívares soberanos (bs)
            precio_bs = precio_venta * tasa

            # Agregar el producto a la tabla de productos comprados
            self.table_prod_comprados.insertRow(0)
            fila = 0
            self.table_prod_comprados.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(producto[0])))  # ID del producto
            self.table_prod_comprados.setItem(fila, 1, QtWidgets.QTableWidgetItem(nombre))  # Nombre del producto
            self.table_prod_comprados.setItem(fila, 2, QtWidgets.QTableWidgetItem(marca))  # Marca del producto
            self.table_prod_comprados.setItem(fila, 3, QtWidgets.QTableWidgetItem(modelo))  # Modelo del producto
            self.table_prod_comprados.setItem(fila, 4, QtWidgets.QTableWidgetItem(cantidad))  # Cantidad del producto
            self.table_prod_comprados.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(precio_unitario)))  # Precio unitario del producto
            self.table_prod_comprados.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(precio_venta)))  # Precio de venta del producto
            self.table_prod_comprados.setItem(fila, 7, QtWidgets.QTableWidgetItem(str(precio_bs)))  # Precio en bs del producto

            # Limpiar el line edit de nombre y la cantidad
            self.prod_name_edit.clear()
            self.id_prod_edit.clear()
            self.cant_prod.clear()
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Producto no encontrado.")
        
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

            # Calcular el precio en bolívares soberanos (bs) multiplicando por la tasa
            precio_bs = precio * tasa

            # Mostrar el precio_bs en la columna correspondiente de la tabla de productos
            item_bs = QtWidgets.QTableWidgetItem(str(precio_bs))
            self.table_prod.setItem(row, 6, item_bs)  # Suponiendo que la columna del precio_bs es la número 5

            # Actualizar la base de datos con el nuevo precio en bs
            id_producto = int(self.table_prod.item(row, 1).text())  # Suponiendo que el ID del producto está en la columna número 0
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