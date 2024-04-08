import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication
from main import IngresoUsuario, Registro, VentanaPrincipal
from conection import DatabaseManager  # Importa la clase DatabaseManager desde tu archivo de conexión

if __name__ == "__main__":
    app = QApplication([])

    # Crear una instancia de DatabaseManager y conectar a la base de datos
    db_manager = DatabaseManager(r"recursos\bd\db.db")

    # Crear una instancia de la ventana de registro y la ventana de inicio de sesión
    ventana_registro = Registro(db_manager)
    ventana_ingreso = IngresoUsuario(db_manager)

    # Conectar la señal 'usuario_registrado' de la ventana de registro con el método 'abrir_ingreso' de la ventana de inicio de sesión
    ventana_registro.usuario_registrado.connect(ventana_ingreso.abrir_ingreso)
    
    # Mostrar la ventana de inicio de sesión
    ventana_ingreso.show()

    # Ejecutar la aplicación
    sys.exit(app.exec_())