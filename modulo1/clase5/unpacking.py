#================================================================================
# **************************************Unpacking de TDD Iterables
# 1. Para asignación simultanea de elementos de un iterable a variables individuales.
# 2. Para crear combinación de colecciones o cambiar su TDD.
# 3. ⏰Para pasar argumentos dinámicos a funciones de forma clara y concisa.

# *1. Asignación simultánea de elementos de ITERABLES a variables individuales
# Ejemplo 1: Unpacking con list, lo mismo con str, set, dict (pero en diccionarios solo las llaves)
# & ******************Codigo Ejemplo
lista = [1, 2, 3, 4, 5]
# ele1 = lista[0]
# ele1 = lista[1]
# ele2 = lista[2]
# ele3 = lista[3]
ele1, ele2, ele3, ele4, ele5 = lista
print(ele1, ele2, ele3, ele4, ele5) # 1 2 3 4 5


# Ejemplo 2: Unpacking con dict, para las CLAVES.
producto = { 'nombre':'laptop', 'precio':1200, 'stock':30}
producto['nombre']
n, p, s = producto #por default me unpacking las claves
print(n, p, s)  # nombre precio stock
n_v, p_v, s_v = producto.values()
print(n_v, p_v, s_v) #laptop 1200 30
for k in producto: #por default me da las claves
    pass

# *⚠️💡👀 Cuando haces unpacking en variables, debes:
#  Tener tantas variables como elementos tenga el iterable en ese momento, o lanzará ValueError.
# O usa el operador * para capturar varios elementos o el resto.
# Ejemplo 3: Unpacking con operador *
  # & ******************Codigo Ejemplo
saludo = 'Hola mundo desde Python' #H o ['l', 'a', ' ', 'm', 'u', 'n', 'd', 'o', ' ', 'd', 'e', 's', 'd', 'e', ' ', 'P', 'y', 't', 'h', 'o', 'n'] 
saludo = ['Hola', 'mundo', 'desde', 'Python'] #Hola mundo ['desde', 'Python']
x, y, *resto = saludo
print(x, y, resto)
  
# *2. Combinación de colecciones o cambiar sus TDD.
s = 'Hola'
print(*s) #H o l a
s_lista = [*s]    #['H', 'o', 'l', 'a']
s_lista = list(s) #['H', 'o', 'l', 'a']
print(s_lista) 

#? Unpaking de 2 colecciones y las fusionamos en un TDD
otro_s = 'mundo'
s_com = [*s, *otro_s]
print(s_com) #['H', 'o', 'l', 'a', 'm', 'u', 'n', 'd', 'o']

#?  Con ** unpackind del dic como Argumentos por palabra clave, en función:

def mostrar(nombre, precio, stock):
    print('Los valores de mis argumentos son:', nombre, precio, stock)


producto = { 'nombre':'laptop', 'precio':1200, 'stock':30}
mostrar(**producto) #Los valores de mis argumentos son: laptop 1200 30


print(**producto) #TypeError: 'nombre' is an invalid keyword argument for print()





#?  Con ** sirve para fusionar diccionarios:
# & ******************Codigo Ejemplo
