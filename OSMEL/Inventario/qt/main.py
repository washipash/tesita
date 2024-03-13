import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate , QBuffer, QByteArray , QTime
from PyQt5.QtGui import QImage,QPixmap 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QIODevice
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget ,QApplication ,QMainWindow,QStackedWidget,QGraphicsDropShadowEffect, QCalendarWidget , QBoxLayout
from PyQt5.QtWidgets import QMessageBox,QLabel,QTableWidgetItem
from PyQt5.QtWidgets import QDialog
import hashlib
import sqlite3
import os
import datetime
from bs4 import BeautifulSoup
import requests
from PyQt5.QtCore import Qt


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi("./qt/invUI.ui", self)
        self.Productos_btn.clicked.connect(self.cambiarPage)
        self.paginaInicia = True



    def cambiarPage(self):
        if self.paginaInicia:
            self.stackedWidget.setCurrentWidget(self.page_productos)
            self.paginaInicia = True
                

    def abrir_ventana_añadir_producto(self):
        ventana_añadir_producto = VentanaAñadirProducto(self)
        ventana_añadir_producto.exec_()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Clinica")  # Establecer el nombre de la aplicación
    
    inventario = VentanaPrincipal()

    widget = QStackedWidget()
    widget.addWidget(inventario)  # Agregar una instancia de VentanaPrincipal
    widget.show()
    sys.exit(app.exec_())
