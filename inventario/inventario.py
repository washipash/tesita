import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication
from main import  VentanaPrincipal, IngresoUsuario, Registro  # Reemplaza 'your_module' con el nombre real de tu módulo

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Crear una instancia de la ventana de registro
    ventana_registro = Registro()
    
    # Crear una instancia de la ventana de inicio de sesión, pasando la ventana de registro como argumento
    ventana_ingreso = IngresoUsuario(ventana_registro)
    
    # Conectar la señal 'usuario_registrado' de la ventana de registro con el método 'abrir_ingreso' de la ventana de inicio de sesión
    ventana_registro.usuario_registrado.connect(ventana_ingreso.abrir_ingreso)
    
    # Mostrar la ventana de inicio de sesión
    ventana_ingreso.show()

    # Ejecutar la aplicación
    sys.exit(app.exec_())