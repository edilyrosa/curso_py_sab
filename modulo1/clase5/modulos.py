
#============================================================================
# **************************************MODULOS
# Un módulo, al igual que un programa, es un archivo de Python (.py) que contiene código preescrito,
# incluyendo variables, constantes, funciones y clases, que puedes importar y reutilizar en tus propios 
# programas. 
# La diferencia entre un modulo y un programa ordinario, es que el código del programa modulo es 
# reutilizable en otros programas, con su importación.
# A los módulos se les llama librerías y bibliotecas y pueden ser propias, integradas y de terceros.

# # *SINTAXIS
# 1. Importar el modulo: con o sin "as" para nickname del modulo.
# import modulo_nombre   || Import modulo_nombre as ms
# 1.1. varias importaciones a la vez:
# import math, sys, os

# 2. Uso: de los elementos del modulo (funciones, variales, constantes)
# modulo_nombre.elemento || ms.elemento
 
# 2.1.  importar solo los elementos necesarios del modulo, no todo el modulo.
# from modulo_nombre import elemento

# 1. help('modules'): Módulos integrados y algunos instalados, Consola interactiva de Python
# 2. pip list o pip freeze: Módulos de terceros instalados vía pip, Terminal, CMD, PowerShell 
# o consola del sistema operativo
# 3. sys.modules: Módulos cargados en el entorno actual, Código Python (cualquier entorno o script)

# & ******************Codigo Ejemplo


#*Definir los elementos: funciones, constantes...
def pot(base, exp):
    return pow(base, exp)
user_name = 'Edily@'
user_passw = 123456

# print(pot(5, 2)) #25
