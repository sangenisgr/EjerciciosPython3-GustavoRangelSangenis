#TAREA 2
#Con expresiones regulares realizar las siguientes validaciones:

#Correo Electrónico
#Dominio + 1 extensión, Ejemplo: gustavo@padts.mx
#Dominio + 2 extensiones, Ejemplo: gustavo@padts.com.mx
#Subdominio + dominio +1 extensión, Ejemplo: gustavo@python.padts.mx

# Número Telefónico
#10 dígitos, Ejemplo 33 33 23 32 33
#Lada indicada en paréntesis 2 o 3 números: ejemplo (33) 33 23 32 33, (33) 33 23 32 33
#       Pueden existir espacios o guiones como separador, ejemplo: (33) 1234 5678, (331) 123-5678
#       Extra: Los separadores deben ser iguales

#Validar RFC Y CURP
#---------------------------------------------------------------------------------------------------

import re

print('Verificacion de correos: ')

correo = 'gustavo@padts.mx'
patron = '^\w+[\._]?\w+[@]\w+[.]\w{2}$'
if (re.search(patron, correo)):
    print(correo + ' correo VALIDO')
else:
    print('Invalid Email')

correo = 'gustavo@padts.com.mx'
patron = '^\w+[\._]?\w+[@]\w+[.]\w{3}[.]\w{2}$'
if (re.search(patron, correo)):
    print(correo + ' correo VALIDO')
else:
    print('Invalid Email')

correo = 'gustavo@python.padts.com'
patron = '^\w+[\._]?\w+[@]\w+[.]\w+[.]\w{3}$'
if (re.search(patron, correo)):
    print(correo + ' correo VALIDO')
else:
    print('Invalid Email')


print('\n')

#-----------------------TELEFONOS--------------------------


telefono = "3312345678"
patron = "[0-9]"

if re.search(patron, telefono):
    print(telefono + " Telefono VALIDO")
else:
    print("ERROR")


telefono = "(33)12345678"

patrondos = "(\w{2})\w"

if re.search(patrondos, telefono):
    print(telefono + " Telefono VALIDO")
else:
    print("ERROR")


telefono = "(331)12345678"

patron = "(\w{3})\w"

if re.search(patron, telefono):
    print(telefono + " Telefono VALIDO")
else:
    print("ERROR")


telefono = "(33) 1234 5678"

patron= "\(\w{2}\)\s\w{4}\s\w{4}"

if re.search(patron, telefono):
    print(telefono + " Telefono VALIDO")
else:
    print("ERROR")


telefono = "(331) 123 4567"

patron= "\(\w{3}\)\s\w{3}\s\w{4}"

if re.search(patron, telefono):
    print(telefono + " Telefono VALIDO")
else:
    print("ERROR")


telefono = "(33) 1234-5678"

patron= "\(\w{2}\)\w{3}\s|-\w{4}"

if re.search(patron, telefono):
    print(telefono + " Telefono VALIDO")
else:
    print("ERROR")


telefono = "(331) 234-5678"

patron= "\(\w{3}\)\w{3}\s|-\w{4}"

if re.search(patron, telefono):
    print(telefono + " Telefono VALIDO")
else:
    print("ERROR")


print('\n')

#---------------------------RFC Y CURP---------------------------------------
RFC = 'RASG880920SM4'
patron = '[a-zA-Z]{4}[0-9]{6}\w+'

if re.search(patron, RFC):
    print(RFC + ' RFC ---> VALIDO')
else:
    print('ERROR')


RFC = 'RASG8809201SM4jkl'
patron = '[a-zA-Z]{4}[0-9]{6}\w$'

if re.search(patron, RFC):
    print(RFC + ' RFC ---> VALIDO')
else:
    print(RFC + ' --ERROR--')


CURP = 'RASG880920HDFNNS06'
patron = '[a-zA-Z]{4}[0-9]{6}[a-zA-Z]{5}\w+'

if re.search(patron, CURP):
    print(CURP + ' CURP ---> VALIDO')
else:
    print(CURP + ' --ERROR--')


CURP = 'RASG8809206123HJKLKSHY'
patron = '[a-zA-Z]{4}[0-9]{6}[a-zA-Z]{5}\w+'

if re.search(patron, CURP):
    print(CURP + 'RFC ---> VALIDO')
else:
    print(CURP + ' --ERROR--')