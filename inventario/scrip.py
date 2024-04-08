import json

def cargar_datos_acceso(file_path):
    with open(file_path, 'r') as file:
        datos_acceso = json.load(file)
    return datos_acceso

# Suponiendo que el archivo JSON está en la misma carpeta que tu script y se llama "datos de acceso.json"
file_path = 'datos de acceso.json'
datos_acceso = cargar_datos_acceso(file_path)

# Autenticación del usuario
nombre_usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")

if nombre_usuario == datos_acceso['nombre'] and contraseña == datos_acceso['password']:
    print("Inicio de sesión exitoso.")
    # Aquí iría el código para iniciar sesión en la aplicación
else:
    print("Nombre de usuario o contraseña incorrectos.")