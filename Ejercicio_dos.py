#Ejercicio 2
#Definir patrones para cadenas de texto que:
import re
#No tenga letras
print('NO tenga letras')
cadena = '123G456U789S'
patron = '[0-9]*$'
resultado = re.match(patron, cadena)
if resultado:
    print(True)
else:
    print(cadena, False)


#Solo tenga números
print('Solo tenga numeros')
cadena = '1234567890'
patron = '[0-9]'
resultado = re.match(patron, cadena)
if resultado:
    print(cadena, True)
else:
    print(False)


#Solo tenga letras mayúsculas
print('Solo tenga letras mayusculas')
cadena = 'GUSTAVO ALFONSO RANGEL SANGENIS'
patron = '[A-Z]'
resultado = re.match(patron, cadena)
if resultado:
    print(cadena, True)
else:
    print(False)


#Solo tenga letras minúsculas
print('Solo tenga letras minusculas')
cadena = 'gustavo alfonso rangel sangenis'
patron = '[a-z]'
resultado = re.match(patron, cadena)
if resultado:
    print(cadena, True)
else:
    print(False)


#No tenga numeros
print('NO tenga numeros')
cadena = 'Esta cadena no tiene numeros 1'
patron = '[a-z][A-Z]'
resultado = re.match(patron, cadena)
if resultado:
    print(True)
else:
    print(cadena, False)



