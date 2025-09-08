
# *************EJEMPLO 1****************

print(' 1️⃣ Primera linea del flujo del programa')
x = False
if x == True:
    print('Camino 1: la var es True')
    print('Camino 1: mas programacion de este camino')
else:
    print('Camino 2: la var es False')
    print('Camino 2: mas programacion de este camino')
    


# *************EJEMPLO 2****************

edad = 18
if edad >= 18:
    print('Eres mayor')
    


# *************EJEMPLO 3: Anidacion de if/else dentro de else****************
# determinar e imprimir en consola si z es mayor, menor o igual a 0
z = 1
if z > 0: 
    print('z es mayor a 0')
else:
    if z < 0:
        print('z es menor a 0')
    else: 
         print('z es igual 0')


# *************EJEMPLO 3: elif****************

if z > 0:
     print('z es mayor a 0')
elif z < 0:
    print('z es menor a 0')
else: 
    print('z es igual 0')
    
print('Fin del programa')


# *************EJERCICIO #1 ****************
#? Ejercicio: agregar múltiples condiciones(elif), Califica a un estudiante según su calificación, 
# con rangos de {
# +90,  -> # Excelente 🥳
# +80,  -> # Muy bien 👏
# +70,  -> # Bien 👍
# +60,  -> # Suficiente 👌
# -59 -> # Insuficiente 😞
# }



#? EJERCICIO # 2: num es par y despues saber si es positivo?
num = 0 
if num % 2 == 0:
    if num > 0: #anidacion del if
        print(f'el num {num} es par es POSITIVO')
    elif num < 0:
        print(f'el num {num} es par es NEGATIVO')
    else: 
        print(f'el num {num} es igual a 0 ')
else:
    print(f'el num {num} es INpar')
    



#? EJERCICIO # 3: usuario puede conducir?
# condion: tener licencia o ser mayor de edad.
MAYORIDAD = 18
tiene_licencia = True
edad1 = int(input('Diga su edad: '))

# if (edad >= MAYORIDAD ) or (tiene_licencia == True): 
if (edad1 >= MAYORIDAD) or tiene_licencia:
    print('✅Usuario Puede manejar')
else:
    print('❌Usuario NOO Puede manejar')

# condicon para que el bloque if seaÑ print('❌Usuario NOO Puede manejar')

if (edad < MAYORIDAD) and ( not tiene_licencia):
    print('❌Usuario NOO Puede manejar')

else:
    print('✅Usuario Puede manejar')


#? EJERCICIO 4: Condicion compuesta para votar: para determinar si usuario tiene la Nacionalidad y (es mayor de edad o esta emancipado).

nacionalidad = input('Tiene la nacionalidad de este pais: si/no: ').strip().lower()
emancipado = True
edad = 17

if nacionalidad == 'si' and (edad >= MAYORIDAD or emancipado):
    print('✅Puede')
else: 
    print('❌No Puede')






# ************Ejemplo # 5: anidacion de if, para condciones mas espeficas *************
# determinar si es numero es par y luego si es positivo


   
# ************Ejemplo # 6: condciones complejas con oepradores logicos *************
#Condicion compuesta para conducir, ser mayor de edad o tener licencia


#todo: EJERCICIO: Condicion compuesta para votar: para determinar si usuario tiene la Nacionalidad y (es mayor de edad o esta emancipado).
# ciudadano = input("¿Es usted ciudadano? (si/no): ").strip().lower() #Entrada con input(prompt) y normalización de la respuesta
