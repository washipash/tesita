from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from database_manager import DatabaseManager

class VentanaAnadirProducto(QtWidgets.QDialog):
    def __init__(self, db_manager, actualizar_func):
        super(VentanaAnadirProducto, self).__init__()
        loadUi(r"qt\agregar_prod.ui", self)
        self.db_manager = db_manager
        self.actualizar_func = actualizar_func
        self.done_btn.clicked.connect(self.agregar_producto)
        self.cancel_btn.clicked.connect(self.close)

class VentanaAnadirProducto(QtWidgets.QDialog):
    def __init__(self, db_manager, actualizar_func):
        super(VentanaAnadirProducto, self).__init__()
        loadUi(r"qt\agregar_prod.ui", self)
        self.db_manager = db_manager
        self.actualizar_func = actualizar_func
        self.done_btn.clicked.connect(self.agregar_producto)  # Conectar botón Done
        self.cancel_btn.clicked.connect(self.close)  # Conectar botón Cancel

    def agregar_producto(self):
        # Obtener los datos ingresados por el usuario desde los widgets
        nombre = self.nombre_line.text()
        modelo = self.modelo_line.text()
        marca = self.marca_line.text()
        cantidad = self.cant_spin.value()
        precio_unitario = float(self.precio_line.text())  # Convertir el texto a float
        
        # Verificar si los campos obligatorios están vacíos
        if not nombre or not marca or not modelo:
            QtWidgets.QMessageBox.critical(self, "Error", "Los campos Nombre, Marca y Modelo son obligatorios.")
            return
        
        # Verificar si el precio unitario es mayor que cero
        if precio_unitario <= 0:
            QtWidgets.QMessageBox.critical(self, "Error", "El precio unitario debe ser mayor que cero.")
            return
        
        # Insertar el nuevo producto en la base de datos
        try:
            self.db_manager.insertar_producto(nombre, marca, modelo, cantidad, precio_unitario)
            QtWidgets.QMessageBox.information(self, "Éxito", "Producto agregado correctamente.")
            
            # Llamar a la función para actualizar la tabla en la ventana principal
            if self.actualizar_func:
                self.actualizar_func()
            
            # Cerrar la ventana de agregar producto
            self.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo agregar el producto: {str(e)}")