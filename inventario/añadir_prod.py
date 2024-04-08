from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from conection import DatabaseManager

class VentanaAnadirProducto(QtWidgets.QDialog):
    def __init__(self, db_manager, actualizar_func):
        super(VentanaAnadirProducto, self).__init__()
        loadUi(r"qt\agregar_prod.ui", self)
        self.db_manager = db_manager
        self.actualizar_func = actualizar_func
        self.done_btn.clicked.connect(self.agregar_producto)
        self.cancel_btn.clicked.connect(self.close)

    def agregar_producto(self):
        # Obtener los datos ingresados por el usuario desde los widgets
        nombre = self.nombre_line.text()
        modelo = self.modelo_line.text()
        marca = self.marca_line.text()
        cantidad = self.cant_spin.value()
        
        # Obtener el texto del campo de precio
        precio_texto = self.precio_line.text()
        
        # Verificar si el campo de precio está vacío
        if not precio_texto:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Ingrese un precio válido.")
            return
        
        # Intentar convertir el texto del precio a un número flotante
        try:
            precio_unitario = float(precio_texto)
        except ValueError:
            # Mostrar un mensaje de advertencia si el texto no es un número válido
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Ingrese un número válido en el campo de precio.")
            return
        
        # Verificar si los campos obligatorios están vacíos
        if not nombre or not marca or not modelo:
            QtWidgets.QMessageBox.critical(self, "Error", "Los campos Nombre, Marca y Modelo son obligatorios.")
            return
        
        # Verificar si el precio unitario es mayor que cero
        if precio_unitario <= 0:
            QtWidgets.QMessageBox.critical(self, "Error", "El precio unitario debe ser mayor que cero.")
            return
        
        # Verificar si el producto ya existe en la base de datos
        if self.db_manager.existe_producto(nombre, marca, modelo):
            QtWidgets.QMessageBox.warning(self, "Advertencia", "El producto ya existe en la base de datos. Por favor, modifique el producto existente o agregue otro.")
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