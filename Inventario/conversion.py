from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi

class VentanaAñadirProducto(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("agregar_prod.ui", self)  # Cargar el archivo de interfaz de usuario
        self.done_btn.clicked.connect(self.agregar_producto)
        self.cancel_btn.clicked.connect(self.close)  # Conectar botón de cancelar para cerrar la ventana

        

    def agregar_producto(self):
        nombre = self.line_edit_nombre.text()
        descripcion = self.desc_edit.toPlainText()  # Utilizamos toPlainText() para obtener el texto de QTextEdit
        modelo = self.line_edit_modelo.text()
        marca = self.line_edit_marca.text()
        cantidad = self.spin_edit_cant.value()  # Usamos value() para obtener el valor del QSpinBox
        precio_unit = float(self.line_edit_precio.text())

        # Acceder al line edit de la tasa desde la página "page_ventas"
        tasa_edit = self.parent().page_ventas.tasa_edit
        tasa = float(tasa_edit.text())

        # Calcular precio en bolívares
        precio_bs = precio_unit * tasa

        # Calcular precio stock
        precio_stock = cantidad * precio_unit

        # Obtener ventana principal
        ventana_principal = self.parent()

        # Agregar datos a la tabla en la página de productos
        fila = ventana_principal.page_productos.table_widget_productos.rowCount()
        ventana_principal.page_productos.table_widget_productos.insertRow(fila)
        ventana_principal.page_productos.table_widget_productos.setItem(fila, 0, QtWidgets.QTableWidgetItem(nombre))
        ventana_principal.page_productos.table_widget_productos.setItem(fila, 1, QtWidgets.QTableWidgetItem(descripcion))
        ventana_principal.page_productos.table_widget_productos.setItem(fila, 2, QtWidgets.QTableWidgetItem(modelo))
        ventana_principal.page_productos.table_widget_productos.setItem(fila, 3, QtWidgets.QTableWidgetItem(marca))
        ventana_principal.page_productos.table_widget_productos.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(cantidad)))
        ventana_principal.page_productos.table_widget_productos.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(precio_unit)))
        ventana_principal.page_productos.table_widget_productos.setItem(fila, 6, QtWidgets.QTableWidgetItem(str(precio_bs)))
        ventana_principal.page_productos.table_widget_productos.setItem(fila, 7, QtWidgets.QTableWidgetItem(str(precio_stock)))
        ventana_principal.page_productos.table_widget_productos.setItem(fila, 8, QtWidgets.QTableWidgetItem(""))

        # Incrementar el contador de ID
        ventana_principal.id_counter += 1

        # Cerrar la ventana de agregar producto
        self.close()
