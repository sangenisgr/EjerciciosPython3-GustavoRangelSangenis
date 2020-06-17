#Creamos una clase estudiante, le agregamos los atributos: nombre, correo electronico y contraseña

class Estudiante:
    __nombre = None
    __correo = None
    __contrasenia = None

    def __init__(self,nombre,correo,contrasenia):
        self.__nombre = nombre
        self.__correo = correo
        self.__contrasenia = contrasenia



    def ingresarNombre(self,nombre):
        nombre = (input("Ingresa tu nombre: "))
        print(nombre)

    def ingrearCorreo(self,correo):
            correo = (input("Ingresa tu correo"))
            print(correo)

    def ingresarContraseña(self,contrasenia):
            contrasenia = (input("Ingresa tu contrasenia"))
            print(contrasenia)

#Llamamos a los metodos de la clase Estudiante
alumno_uno = Estudiante(nombre= None ,correo= None ,contrasenia= None)

alumno_uno.ingresarNombre(nombre)
alumno_uno.ingrearCorreo(correo)
alumno_uno.ingresarContraseña(contrasenia)
