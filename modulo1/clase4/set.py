# *******************************************************set
# colección no ordenada de elementos únicos, irrepetibles y mutables. 
# Puedes agregar o quitar elementos después de crear el set.
# *Características:
#No hay duplicados.
#Desordenados, NO puedes accederlos por índice.
# Solo pueden contener elementos inmutables (por ejemplo, números, strings, tuplas).
# Usados para para eliminar duplicados y realizar operaciones de conjuntos matemáticos (unión, intersección, diferencia).
# Creacion con llaves {}:
# ************************************************Codigo explicacion....******************************************

s = {1, 2, 3, 4, 4, 4, 5}
print(s) # {1, 2, 3, 4, 5}

l = [1, 2, 2, 3, 4, 4, 5]
list_a_set = set(l)
print(list_a_set) # {1, 2, 3, 4, 5}

list_a_set.add(6)
list_a_set.remove(1)
print(list_a_set) # {2, 3, 4, 5, 6}

print(1 in list_a_set) #False

# Operaciones de conjuntos
a = {1, 2, 3}
b = {3, 4, 4, 5}
print(a.union(b)) # {1, 2, 3, 4, 5}
print(a.difference(b)) # {1, 2}
print(a.intersection(b)) #{3}
