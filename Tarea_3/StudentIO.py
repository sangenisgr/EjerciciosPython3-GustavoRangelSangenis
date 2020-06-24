import pickle
import shelve

import database

#FUNCIONES PARA PICKLE
def guardarEstudiante():

    pickle.dump(database.db, database.db_estudiantes)
    database.db_estudiantes.close()


def leerEstudiante():

    db_estudiantes = open('ListaPickle', 'rb')
    unpickler = pickle.Unpickler(db_estudiantes)
    leerEstudiante = unpickler.load()
    db_estudiantes.close()

    print(leerEstudiante)

#FUNCIONES PARA SHELVE


def guardarEstudianteS():
    db_estudiantes = shelve.open('ListaShelve.db')
    db_estudiantes = db_estudiantes()
    database.db_estudiantes['key'] = db_estudiantes

