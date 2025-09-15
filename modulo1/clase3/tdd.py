
# **************************TEORIA: Tipos de Datos 
# ***********************list
# Las listas son Colecciones ordenadas de datos, el orden es secuencial y preciso.
# Cada dato coleccionado en la lista es un elemento.
# La lista puede contener cualquier tipo de dato, incluso otras listas.
# La lista se representa encerrando sus elementos entre corchetes. No es necesario establecer su tamaño al declararse.


#*list
my_list= [1, 2, 3, 4, 5] 
print(my_list, type(my_list))
print(my_list[0]) #1
my_list[0]  = 100
# print(my_list)    #[100, 2, 3, 4, 5]

my_list = []
my_list = list('Hola12') #['H', 'o', 'l', 'a', '1', '2']
mi_tupla_list = ('hola', True, 12.12)
my_list = list(mi_tupla_list)
print(my_list)          # ['hola', True, 12.12]

# de str a list con srt.split('separador')
nombre = 'Edily Mora Morales'
fecha = '12-12-2020'
nombre_list = nombre.split()
fecha_list = fecha.split('-')

print(nombre_list) #['Edily', 'Mora', 'Morales']
print(fecha_list) #['Edily', 'Mora', 'Morales']

#? explicacion de comillas en str
# print(f'esto {nombre_list} y {fecha.split("-")}')
# print('esto',  nombre_list, "y", fecha.split("-"))
# print("""hola mi nombre es "edily" """)
print('=='*30) #['12', '12', '2020']

list_repetido = ['hola'] * 8
print(list_repetido) #['hola', 'hola', 'hola', 'hola', 'hola', 'hola', 'hola', 'hola']
print(len(list_repetido)) #8 tamb valido para tupla


# ? METODOS DE LIST
# vieron: append(), insert(), extend(), pop(), remove(), clear(), index(), count(), sort(), reverse(), copy()
#* formas de agregar elementos a la list
# append(), 
# insert(), 
# extend(), 
# *formas de eliminar elementos a la list
# pop(i | defalult -1 ),  pop(0)
# remove(x),
# clear(list),

# sort(), reverse()

list_ordenar = [100, 500, 23, 21, 0.12]
# list_ordenar.reverse()
# list_ordenar.sort()
lista_ya_ordenada = sorted(list_ordenar)
# list_ordenar.sort(reverse=True)
print(list_ordenar)
print(lista_ya_ordenada)

# *return el index del ele parametro, desde 0
# *uno  ordena segun Unicode (o ASCII), el otro revierte su orden de secuencial.
# * Casi todos los metodos mofican la lista in situ y returnan None, salvo sorted()

#*CLONACION O COPIA DE LIST
#* Asignacion con alias: afectacion total uno al otro
# Alias (b = a) → no hay copia, ambas variables son el mismo objeto (a is b es True).
a = [1, 2, ['Carlos, Edily'] ]
b = a 
print(a, b)
b[0] = 0.12
print('a', a)
print('b', b)

# *copia superficial: afectacion de los obj mulatables, uno al otro
# (shallow copy) la copia solo duplica la lista en el primer nivel, por lo que sus elementos objetos internos mutables 
# ( e.g: estructurales, list, dict, set)) son compartidos, pues siguen apuntando a los mismos objetos en memoria. 
# NO Los tipos básicos como int, float, str, bool, tuple (inmutable) son inmutables en Python. Si asignas un nuevo valor, 
# se crea otro objeto nuevo y se rompe la referencia compartida.





a = [1, 2, [3, 4]] #1 y 2 tienen referencias independientes en memoria, no asi para el obj mutable como la list
c = a.copy()
print('c', c) #[1, 2, [3, 4]]
a[0] = 100                  #? NO afectara c, TDD basico (INMUTABLE)
a[2][1] = 40                #? SI afectara c, TDD OBJETO MUTABLE

print('c', c) #[1, 2, [3, 40]] #?cambio solo el obj mutable
print('a', a) #[100, 2, [3, 40]]



# *copia profunda:
import copy
d = copy.deepcopy(a)
print('d',d)
a[0] = 500                   #? NO afectara "d", TDD basico (INMUTABLE)
a[2][1] = 400                #? TDD OBJETO MUTABLE, pero es una copia profunda, no afectara a "d"
print('a', a )               # a [500, 2, [3, 400]]
print('d',d)                 #d [100, 2, [3, 40]]

















# # #*Tuple
# my_tupla = (1, 2, 3, 4, 5)
# print(my_tupla, type(my_tupla))
# print(my_tupla[-2]) #4
# #my_tupla[0]  = 100 #!TypeError: 'tuple' object does not support item assignment
# # print(my_tupla)    #[100, 2, 3, 4, 5]

# list_para_tupla = [12, 12, 56, 'Edily']
# my_tupla = tuple(list_para_tupla)
# print(my_tupla)  #(12, 12, 56, 'Edily')