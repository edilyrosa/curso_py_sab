# #***********************************************WHILE**************************************
# Para repetir un bloque de código mientras una condición se cumpla (es verdadera).  
# El código dentro del bucle se ejecuta repetidamente hasta que la condición se vuelve falsa.

#* SINTAXIS
# inicialización de la variable de control ⚠️
# ⭐while condición:
#     # Bloque de código a ejecutar mientras la condición sea True
#     # Actualización de la variable de control ⚠️🚩

# *⁉️Cómo funciona
# Se evalúa la condición.
# Si la condición es verdadera (True), se ejecuta el bloque de código.
# Luego se vuelve a evaluar la condición.
# Cuando la condición es falsa (False), se sale del bucle y se continúa con el resto del programa.
# ************************************************Codigo explicacion....******************************************

contador = 5
while contador > 0:
    print("Contador:", contador)
    contador -= 1  # Decrementa el contador en 1 
       
print(" 1. Programa del flujo ordinario")
  
  

# *⭐Uso típico del while
# Cuando no sabemos de antemano cuántas veces se repetirá el ciclo.
# Cuando la repetición depende de una condición dinámica cambiante, o del usuario.
# En combinación con break para salir anticipadamente.
# ************************************************Codigo explicacion....******************************************

while True: 
    entrada = input('escribe "salir" para salir del ciclo infinito: ')
    if  entrada == 'salir':
        break

print(" 2. Programa del flujo ordinario")

# Isauth = True
# password and Username
# while Isauth:
#     consumir contenido 
#     eschar si quiere seguir consumiendo
#     el pago sis


#*⛹🏽‍♂️⛹🏽‍♀️💡EJERCICIO #1: Genere y muestre la tabla de multiplicar de un número específico.💡⛹🏽‍♂️⛹🏽‍♀️
# El programa debe pedirle al usuario que ingrese un número entero y luego,
# utilizando un bucle, debe imprimir la tabla de multiplicar de ese número del 1 al 10.
# ************************************************Codigo Solucion....******************************************


# num = int(input("Ingrese un número entero para ver su tabla de multiplicar: "))
# i = 0
# while i <= 10:
#     print(f"{i} X {num} = {i*num}")
#     #i += 1
#     i += 2 #modificacion: para pares 
# print(" 3. Programa del flujo ordinario")



numero = int(input("Ingresa un número entero:"))
base= 0 #inicialización de la variable de control AFUERA ⚠️
while base <= 10:
    print(f"{base}*{numero}={base*numero}")
    base += 1 # Actualización de la variable de control ADENTRO ⚠️🚩
    
print(" 3. Programa del flujo ordinario")

