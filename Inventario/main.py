import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate , QBuffer, QByteArray , QTime
from PyQt5.QtGui import QImage,QPixmap 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QIODevice, QDateTime, Qt
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget ,QApplication ,QMainWindow,QStackedWidget,QGraphicsDropShadowEffect, QCalendarWidget , QBoxLayout
from PyQt5.QtWidgets import QMessageBox,QLabel,QTableWidgetItem
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QTimer  
from PyQt5.QtGui import QMovie
import hashlib
import sqlite3
import os
import datetime
from añadir_prod import VentanaAnadirProducto
from database_manager import DatabaseManager # Importa la clase DatabaseManager desde el archivo database_manager.py



from PyQt5.QtCore import Qt

class DatabaseManager:
    def __init__(self, database_file):
        self.database_file = database_file
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def obtener_productos(self):
        # Ejecutar una consulta para obtener todos los datos de la tabla productos
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall()
        return productos
    
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
        self.edit_btn.clicked.connect(self.abrir_editar_producto)
        self.paginaInicia = True
        self.mostrar_datos_productos()
        self.cierre_btn.clicked.connect(self.abrir_ventas_diarias)
                # Insertar GIF en el QLabel
        self.insertar_gif_en_label()
     # Actualizar la hora y el día cada segundo
        self.actualizar_hora_fecha()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_hora_fecha)
        self.timer.start(1000)

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

    def mostrarPaginaProductos(self):
        # Llamar a la función para mostrar los datos de los productos
        self.mostrar_datos_productos()
        self.stackedWidget.setCurrentWidget(self.page_productos)

    def mostrarPaginaVentas(self):
        self.stackedWidget.setCurrentWidget(self.page_ventas)

    def mostrarPaginaReparaciones(self):
        self.stackedWidget.setCurrentWidget(self.page_reparaciones)

    def mostrarPaginaayuda(self):
        self.stackedWidget.setCurrentWidget(self.page_ayuda)

    # Método para abrir la ventana de añadir producto
    def abrir_ventana_anadir_producto(self):
        ventana_anadir_producto = VentanaAnadirProducto(self.db_manager, self.actualizar_tabla)
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

    def actualizar_tabla(self):
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("inventario")
    # Crear una instancia de DatabaseManager y conectar a la base de datos
    db_manager = DatabaseManager(r"recursos\bd\db.db")
    # Pasar la instancia de DatabaseManager a la ventana principal
    ventana_principal = VentanaPrincipal(db_manager)
    ventana_principal.show()
    ventana_principal.showMaximized()  # Mostrar la ventana en pantalla completa
    sys.exit(app.exec_())