"""
SISTEMAS DISTRIBUIDOS.
Nombres y Apellidos: Winter Aníbal Meza Jiménez.
Curso: Octavo "A" 2023(1).
Práctica Guiada 1: Guias 1 y 2.
Fecha: Domingo, 4 de diciembre de 2022.
Docente: Ing. Willian Zamora Mero, PhD.

ACTIVIDAD:
Crear un pequeño programa (no es necesario crear interfaz gráfica por ahora) que permita
insertar datos a una colección denominada (clientes) cuyos campos son nombres, dirección,
email, saldo. Esta colección o tabla debe ser creada en la base de datos “dbprueba” y la
conexión del programa debe ser a través del usuario “facci”. Para realizar el programa usted
puede hacer uso del lenguaje de programación que usted considere. Sugerencia Python.
"""
# Importar las librerias que se van a utilizar.
import pymongo
from pymongo.errors import ConnectionFailure

# Establecer la conexión con MongoDB
cliente = pymongo.MongoClient("mongodb://facci:asd@192.168.1.21:27017/dbprueba")
# Seleccionar la base de datos
db = cliente["dbprueba"]

# Seleccionar la colección
coleccion = db["cliente"]

# Solicitar los datos al usuario
datoNombre = input("Ingrese el nombre del cliente: ")
datoDireccion = input("Ingrese la dirección del cliente: ")
datoEmail = input("Ingrese el email del cliente: ")
Datosaldo = float(input("Ingrese el saldo del cliente: "))

# Crear el documento a insertar
documento = {
    "nombre": datoNombre,
    "direccion": datoDireccion,
    "email": datoEmail,
    "saldo": Datosaldo
}

# Insertar el documento en la colección
coleccion.insert_one(documento)
print("Los datos del cliente se ha insertado correctamente.")




