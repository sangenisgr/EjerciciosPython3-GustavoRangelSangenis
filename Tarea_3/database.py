#La Tarea 3 consiste en emular el funcionamiento de una base de datos utilizando Pickle y Shelve cumpliendo con los siguientes puntos


#Crear 5 objetos estudiante (utilizando clase creada en el Ejercicio 3)
#Crear una función para guardar estudiantes.
#Crear una función para leer estudiantes.
#Crear una función para actualizar estudiantes.
#Crear un Modulo llamado StudentIO que contenga las funciones.
#Las funciones se deben crear tanto para Pickle como para Shelve.

import StudentIO
import pickle

class Estudiante():
    __nombre = ''
    __correo = ''
    __pwd = ''

    def __init__(self, n, m, p):
        self.__nombre = n
        self.__mail = m
        self.__pwd = p

estudiante_uno = Estudiante('Carlos', 'carlos@padts.com', 'carlos1')
estudiante_dos = Estudiante('Alex', 'alex@padts.com.mx', 'alex1')
estudiante_tres = Estudiante('Carla', 'carla@python.mx', '123cr')
estudiante_cuatro = Estudiante('Gustavo', 'sangenisgr@padts.com.mx', '123456789')
estudiante_cinco = Estudiante('Fabiola', 'fabiola@python.com.mx', 'fab1234')

db = {}
db['Estudiante_uno'] = estudiante_uno
db['Estudiante_dos'] = estudiante_dos
db['Estudiante_tres'] = estudiante_tres
db['Estudiante_cuatro'] = estudiante_cuatro
db['Estudiante_cinco'] = estudiante_cinco

db_estudiantes = open('ListaPickle', 'ab')

if __name__ == '__main__':

    StudentIO.guardarEstudiante()
    StudentIO.leerEstudiante()
    StudentIO.guardarEstudianteS()