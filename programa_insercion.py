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
from pymongo import MongoClient

# Configurar la conexión a MongoDB
client = MongoClient('mongodb://facci:asd@192.168.1.21:27017/dbprueba')
db = client['dbprueba']
collection = db['cliente']

# Obtener los datos del cliente
datoNombre = input("Ingrese el nombre del cliente: ")
datoDireccion = input("Ingrese la dirección del cliente: ")
datoEmail = input("Ingrese el email del cliente: ")
datoSaldo = float(input("Ingrese el saldo del cliente: "))


# Crear el documento del cliente
cliente = {
    "nombre": datoNombre,
    "direccion": datoDireccion,
    "email": datoEmail,
    "saldo": datoSaldo
}

# Insertar el documento en la colección "clientes"
result = collection.insert_one(cliente)
print("Documento insertado con el ID:", result.inserted_id)


# Codigo que proporciona el profesor en la guía 3.
import pymongo
from pymongo.errors import ConnectionFailure

try:

    cliente="mongodb://facci:asd@192.168.1.21:27017/dbprueba"
    connection = pymongo.MongoClient(cliente)
    mydb = connection["dbprueba"]
    mycol = mydb["cliente"]
    mydict = { "nombre": "WINTERMEZA", "direccion": "Manta Barrio la Florita", "email":"wmeza@gmail.com", "saldo":"10" }
    dataInserted = mycol.insert_one(mydict)
    print("ID:"+str(dataInserted.inserted_id))
    print ("Registro insertado")
    connection.close_cursor
    connection.close
except ConnectionFailure:
    print("Server no se encuentra disponible. Intente más tarde")



