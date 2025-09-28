#  ******************************FRUNCIONES CON def *********************************************
# Bloque de código de sentencias que realiza una tarea específica en el programa, 
# siendo reusable. Usamos funciones para modular y evitar la repetición. 
# La keyword "def" es usada para definir una función.
# 
# ⭐Argumentos: datos que pueda necesitar una función para realizar su tarea, y
# serán pasados dentro de sus parentesis de ejecucion, separados por ","
# pasa tantos, como parámetros se haya declarado en su definición, 
# a menos que sean variables globales.  
# 
# ⭐La función podría o no retornar un valor o resultado, con la instrucción return.
# return termina una función y opcionalmente devuelve un valor.

# *SINTAXIS:
#  def nombre_funcion(parámetros_opcionales):
#     # Bloque de código indentado que define lo que hace la función
#     instrucciones
#     return valor_retorno_opcional
# & ******************Codigo Ejemplo
#* 1️⃣ FUNC SIN PARAMETROS, SIN RETURN 
def saludar_estander():
    print('Hola usuario') #Esto es una instruccion, NO es un una orden de retornar
saludar_estander()

#* 2️⃣ FUNC CON USO DE VAR GLOBAL. SIN PARAMETROS, SIN RETURN 
var_global = 'Usuari@'
def saludar_var_global():
    print(f'Hola usuario {var_global}') #Esto es una instruccion, NO es un una orden de retornar
saludar_var_global() #Hola usuario Usuari@


#* 3️⃣ FUNC CON PARAMETROS, SIN RETURN 

def saludar_especifico(nombre):
    print(f'Hola usuario {nombre}') #Esto es una instruccion, NO es un una orden de retornar
#saludar_especifico() #! TypeError: saludar_especifico() missing 1 required positional argument: 'nombre'
saludar_especifico('Edily') # Hola usuario Edily
saludar_especifico(12)      # Hola usuario 12

#* 4️⃣ FUNC CON PARAMETROS, CON RETURN 
def suma(a, b):
    return a+b

result = suma(12, 10) + 22
print(suma(12, 10)) #22
print(result)       #44

#*💡⭐Retornando mas 1 un elemento
def retorna_max_min(list):
    maximo = max(list)
    minimo = min(list)
    return maximo, minimo
print(retorna_max_min([100, -23, 505, 55])) # (505, -23)
desconocido = 1,2,3 
desconocido2 = (1) #int
desconocido3 = (1, ) #tuple
print( type(desconocido), type(desconocido2), type(desconocido3) ) #<class 'tuple'> <class 'int'> <class 'tuple'>


#  ******************************ÁMBITO DE VARIABLES GLOBALES EN FUNCIONES*********************************************
# ⭐Por default, en ámbito local, solo podemos leer una variables globales, 
# ❌NO modificarla.
# Dentro de un ámbito local (función), puedes modificar una variable global, 
# usar la keyword global antes de intentar modificarla. Como 1era declaracion en la func
# ⚠️Cuidado, la modificación afectara el valor de la variable, local y globalmente.
# Esto NO es una buena practica⚠️
x = 100
def cambiando_x():
    global x
    x+=100    # !nboundLocalError: local variable 'x' referenced before assignment
    #x = 200 #var local
    print('x local = ', x) #200

print('x global', x) #100
cambiando_x()
print('x global', x) #200


# ?📖💡⭐La imposibilidad de modificar variables globales en ámbitos de d funciones, 
# NO ocurre en los bucles, porque estos NO crea un nuevo ámbito. 
# Estárias trabajando directamente en el ámbito global donde la variable fue definida.
# & ******************Codigo Ejemplo
# NO PASA CON LOS CICLOS
# contador = 0 declara afuera iterador
# while True:
#     contador += 1 actualiza


#*ARGUMENTOS POSICIONALES Y POR PALABRA CLAVE EN FUNCIONES
# Cuando ""llamas""" a una función, puedes pasar los """argumentos""" de dos maneras:
# & ******************Codigo Ejemplo
# *1️⃣Argumentos posicionales: Se pasan en el mismo orden en que los PARÁMETRO están definidos.
def saludar_orden(nombre, apellido):
    print(f'Hola {nombre}, tu apellido es: {apellido}?') 

saludar_orden('Rosa', 'Mora') # Hola Rosa, tu apellido es: Mora?
saludar_orden('Mora', 'Rosa') # ⚠️Hola Mora, tu apellido es: Rosa?

# *2️⃣Argumentos por palabra clave: Puedes especificar los argumentos usando los nombres de los PARÁMETRO, 
# te permite cambiar el orden.
saludar_orden(apellido= 'Mora', nombre='Rosa') # Hola Rosa, tu apellido es: Mora?

# *3️⃣Valores por defecto: Puedes asignar un valor por defecto a un PARÁMETRO al definir la función. 
# Esto hace que ese parámetro sea opcional. Si el usuario no lo proporciona, se usará el valor por defecto. 
# ⚠️❌Los parámetros con valores por defecto siempre deben ir después de los parámetros sin valores por defecto, 
# de lo contrario generaras un Error ❌
def saludar_default(apellido, nombre = 'Usuario'):
    print(f'Hola {nombre}, tu apellido es: {apellido}?') 
saludar_orden(apellido= 'Mora')

#*⛹🏽‍♂️⛹🏽‍♀️💡EJERCICIO #1:Funciones
# Crear un programa que verifique si una persona es mayor de edad. 
# Para ello, debes crear una función que reciba 
# la edad como parámetro y devuelva True si la persona 
# es mayor de edad o False si no lo es.


#*⛹🏽‍♂️⛹🏽‍♀️⛹🏽‍♂️⛹🏽‍♀️💡EJERCICIO #2:Funciones
# Crea una función que calcule el precio final de un producto después de aplicar un descuento. 
# La función debe recibir de usuario con input(), el precio original, el porcentaje de descuento, 
# y si aplica el descuento (si/no), y devolver el precio final, lo que dependerá de si aplica o no 
# el descuento.
