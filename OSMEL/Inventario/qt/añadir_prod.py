from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi

class VentanaAñadirProducto(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("agregar_prod.ui", self)  # Cargar el archivo de interfaz de usuario
        self.done_btn.clicked.connect(self.agregar_producto)
        
                # Acceder a la tabla de productos desde la página "page_productos"
        tabla_productos = self.parent().page_productos.table_widget_productos

        # Acceder al line edit de la tasa desde la página "page_ventas"
        tasa_edit = self.parent().page_ventas.tasa_edit

    def agregar_producto(self):
        nombre = self.line_edit_nombre.text()
        descripcion = self.desc_edit.toPlainText()  # Utilizamos toPlainText() para obtener el texto de QTextEdit
        modelo = self.line_edit_modelo.text()
        marca = self.line_edit_marca.text()
        cantidad = self.spin_edit_cant.value()  # Usamos value() para obtener el valor del QSpinBox
        precio_unit = float(self.line_edit_precio.text())
        tasa = float(self.page_ventas.tasa_edit.text())

        # Calcular precio en bolívares
        precio_bs = precio_unit * tasa

        # Calcular precio stock
        precio_stock = cantidad * precio_unit

        # Obtener ventana principal
        ventana_principal = self.parent()

        # Agregar datos a la tabla en la página de productos
        fila = ventana_principal.table_prod..rowCount()
        ventana_principal.table_prod.insertRow(fila)
        ventana_principal.table_prod.setItem(fila, 0, QTableWidgetItem(nombre))
        ventana_principal.table_prod.setItem(fila, 1, QTableWidgetItem(descripcion))
        ventana_principal.table_prod.setItem(fila, 2, QTableWidgetItem(modelo))
        ventana_principal.table_prod.setItem(fila, 3, QTableWidgetItem(marca))
        ventana_principal.table_prod.setItem(fila, 4, QTableWidgetItem(str(cantidad)))
        ventana_principal.table_prod.setItem(fila, 5, QTableWidgetItem(str(precio_unit)))
        ventana_principal.table_prod.setItem(fila, 6, QTableWidgetItem(str(precio_bs)))
        ventana_principal.table_prod.setItem(fila, 7, QTableWidgetItem(str(precio_stock)))
        ventana_principal.table_prod.setItem(fila, 8, QTableWidgetItem(""))

        # Incrementar el contador de ID
        ventana_principal.id_counter += 1

        # Cerrar la ventana de agregar producto
    def cerrar_ventana(self):
     self.close()