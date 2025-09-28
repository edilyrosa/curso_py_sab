# ********************************************Unpacking de TDD Iterables
# 1. Para asignación simultanea y rápida de los elementos de un iterable (lista, tupla, str, etc.) a variables individuales.
# 2. Para crear combinación de colecciones o cambiar el TDD de la secuencia.
# 3. ⏰Para pasar argumentos dinámicos a funciones de forma clara y concisa.


# *1. Asignación simultánea de elementos de ITERABLES a variables individuales
# Ejemplo 1: Unpacking con list, lo mismo con str, set, dict (pero en diccionarios solo las llaves)
# ************************************************Codigo explicacion....******************************************

lista = [1, 2, 3]
uno = lista[0]
dos = lista[1]

print(lista[0])
print(uno)

x, y, z = lista # Unpacking
print(x, y, z ) #1 2 3
resultado = x + y + z
print(resultado) #6
print(y **2) #6

primero, segundo = ['hola', 'mundo']
print(primero) #hola
print(segundo) #mundo