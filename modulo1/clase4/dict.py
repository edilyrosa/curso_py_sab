# #***********************************************DICT**************************************
# *TDD dict
# Se crea con llaves {}. 
# Colección de datos que almacena información en pares de clave:valor. 

# Con Asignación puedes crear un nuevo par (c:v) 
# o actualiza, utilizando la clave (como indice) para acceder al valor. 
# Con la asignacion, Si la clave ya existe haces actualizacion, sino creacion del elemento.

# Cada elemento es un par (c:v), y deben estar separados por “,”
# ? ⁉️QUE TDD PUEDEN SER CLAVE Y VALUE?


# clave: debe ser TDD inmutable (como un str, int, o tuple).
# valor: puede ser de cualquier TDD.
#***CREACION****
#***ACCESO A VALUES****
# ************************************************Codigo explicacion....******************************************

gustos = ['***************caminar', 'programar', 'leer']
persona = {
    'nombre': 'Juan',
    'peso': 12.12,
    'genero': True,
    'gustos': gustos,
    #clave TDD num
    102: 'Maria',
    #clave TDD bool
    True: 'mayor',
    'hobby': ['futbol', 'programar', 'leer'],
    'contacto': {
        'email': "ed@hasattr",
        'telefono': 123456789
    },
    #clave TDD tuple
    ('latutud', 'longitud'): [12.123, 34.567] 
}

print(persona[True])                        #mayor
print(persona[('latutud', 'longitud')])     #[12.123, 34.567]
print(persona[('latutud', 'longitud')][1])  #34.567
print(persona['contacto'])                  #{'email': 'ed@hasattr', 'telefono': 123456789}                   #mayor
print(persona['contacto'][ 'telefono'] )    #123456789                             #mayor
persona['contacto'][ 'telefono'] = 1234                            #mayor
print('Tlf mofificado', persona['contacto'][ 'telefono'] )    #123456789                             #mayor
print(persona)

# list = (1, 4, 5)
# list[2]

#*METODOS
# Tamaño: con len(dict), retorna el número de elementos.
# Mutabilidad: Son mutables, puedes agregar, eliminar y modificar elementos. Las claves son irrepetibles.
#Actualizar o crear depende de si la clave YA existe.

# Acceder al Valor: 
    # dict[clave]: Lanza error si la clave no existe
    # valor = mi_diccionario.get(clave): Retorna None o un valor por defecto si la clave no existe.

# Eliminar un Elemento:
    # dict.pop(clave): Elimina el elemento y retorna el valor
    # dict.popitem(): Elimina el ultimo elemento.
    # del dict[clave] Elimina el elemento sin retornar nada.

# Vaciar Diccionario: Elimina todos los elementos.
    # dict.clear()

# Verificar Clave: Comprueba si una clave existe. Retorna bool.
    # clave in dict
# ************************************************Codigo explicacion....******************************************

print('Tamaño del diccionario:', len(persona)) #8


persona['nombre'] = 'Edily'
persona['edad'] = 30

# edad = int(input('actualiza edad: '))
# persona['edad'] = edad

#print(persona['nefermedad'])    #!KeyError
print(persona.get('enefermedad')) #*None

persona.pop('nombre')
persona.popitem()
print(persona)

print(102 in persona) #True
print('nombre' in persona) #False

# for e in [1,2,3,4]:
#     print(e)

#*RECORRERLOS O ITERRALOS
# Ordenados: mantienen el orden de inserción de los elementos.
# for clave in dict -> defalult, itera sobre las claves
# dict.values() -> itera sobre los valores
# dict.items() -> itera sobre los pares clave-valores al mismo tiempo
# ************************************************Codigo explicacion....******************************************

for clave in persona: #Defalult, itera sobre las claves
    # print(clave, '->', persona[clave])
    print(clave)
    
print('------------------')
for v in persona.values(): #itera sobre los valores
    print(v)
print('------------------')
for clave,valor in persona.items(): #itera sobre los valores
    print(clave ,valor)
    
    
    

#TODO: ⛹🏽‍♂️⛹🏽‍♀️💡EJERCICIO # 2: CREA UN DICT CON 5 ELEMENTOS, LAS CLAVES SERAN {1,2,3,4,5} 
# Y LOS VALORES SERAN EL CUADRADO DE LAS CLAVES
# CREA EL DICT VACIO, LUEGO MEDIANTE UN FOR ITERA UN RANGE(1,6) PARA CREAR LOS PARES (c:v)
# ************************************************Codigo Solucion....******************************************
mi_dic = {}
for x in range(1, 6):
# for x in [1,2,3,4,5]:
    mi_dic[x] =  x**2
print(mi_dic) # {1:1, 2:4, 3:9, 4:16, 5:25}


#📖👀⁉️ A diferencia de las listas, a un dict vacío sí puedes asignar directamente valores usando una clave nueva, 
# incluso si el dict está inicialmente vacío.
lista_vacia = []
#lista_vacia[0] = 'hola'  #! Esto produce IndexError: list assignment index out of range
# Esto ocurre porque la lista inicialmente no tiene elementos y no se puede asignar directamente a un índice inexistente.
# Para agregar elementos a una lista vacía debes usar métodos como: append() para añadir al final



#*COPIAR UN DICT
#  ? Copia Superficial: .copy() || dict()
# Crea un nuevo sdict, pero si el original contiene objetos mutables
# (list o dict), ambos diccionarios apuntarán a los mismos objetos. 
# Cualquier cambio en esos objetos anidados afectará a ambas copias.
# Uso: Si solo contiene TDD inmutables (str, int, tuple).

d1 = {'a': [1, 2]}
d2 = d1.copy()
d2['a'].append(3)
print(d1) #{'a': [1, 2, 3]}



# que pasa si una copia superficial cambia el valor de un mulable por un inmutable? esto sera compartido por la copia?
# Cuando una copia superficial (shallow copy) comparte referencias a objetos mutables y luego en una de esas copias se
# asigna un valor inmutable (como un número, string, o tupla), la referencia de ese valor deja de estar compartida: 
# solo el objeto que recibe el valor inmutable tiene la nueva referencia
d1 = {'a': [1, 2]}
d2 = d1.copy()
d2['a'] = 99        # Ahora en d2 'a' apunta a un entero

print(d1)           # {'a': [1, 2]}
print(d2)           # {'a': 99}



# ?Copia Profunda: import copy; copy.deepcopy()
# Crea un diccionario totalmente independiente, replicando todos los objetos anidados. 
# Uso: El contiene objetos mutables anidados que necesitas que sean independientes de la copia original.
edily = {
    'genero':'F',
    "edad":30,                                                    # ✅TDD valor es int: INmutable, los cambios NO afectan al otro
    ("materias", 'calificaciones'): [['math', 'bio'], [20, 19]],  # ⚠️TDD valor es List: Mutable, los cambios SI afectan al otro
    "telefonos":{                                                 # ⚠️TDD valor es dict: Mutable, los cambios SI afectan al otro
        "casa":42499,
        "ofi":42400,
    }
}
# ************************************************Codigo explicacion....******************************************

#copia_edily = edily.copy()  #Copia Superficial
import copy     
copia_edily = copy.deepcopy(edily)  #Copia Profunda
copia_edily['edad'] = 500
copia_edily[ ("materias", 'calificaciones')] 

print('LA LISTA', copia_edily[("materias", 'calificaciones')]) #LA LISTA [['math', 'bio'], [20, 19]]
print(copia_edily[("materias", 'calificaciones')][0][0]) # math
copia_edily[("materias", 'calificaciones')][0][0] = 'Historia'

print('copia', copia_edily)
print('Original', edily)



