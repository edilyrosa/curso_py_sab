
# *IMPORTAR
# import modulos #* tengo que usarla con el nombre completo: modulos.user_passw 
import modulos as m
from math import pi
import math

print(pi) #3.141592653589793
pi = 10.10
print(pi) #10.1

print(m.pot(5, 2)) #25
print(math.pow(5, 2)) #25.0

def saludo(user, passw):
    print(f'Hola {user} tu passwoerd es {passw}')
    
saludo(m.user_name, m.user_passw) #Hola Edily@ tu passwoerd es 123456


print(dir(math))