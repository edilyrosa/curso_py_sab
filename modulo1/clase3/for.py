
# # **************************CICLOS O LOOP
# # #*****************FOR
# # Recorre o itera sobre una secuencia (list, str, range, etc.) ejecutando un bloque para cada 
# # elemento del iterable.
# # Sintaxis:
# # for variable in iterable:
# #     # bloque de código
# # variable: almacena el valor actual de la iteración.
# # iterable: cualquier secuencia como una lista, tupla, cadena o rango.

# trutas  = ['uva', 'pera', 'mango', 'banana']
# for fruta in trutas:
#     print(fruta)

# for letras in 'hola':
#     print(letras)

# for ele in range(1, 11):
#     print(ele)


# *break, continue y pass: se usan en los bucles para alterar el flujo normal del ciclo.
# break sale del bucle.
# continue salta a la siguiente iteración.
# pass no hace nada, solo ocupa un lugar en el código.

for e in range(10):
    if e == 6:
        break #es fatal, se sale del ciclo para siempre
    print(e)
    
for e in range(10):
    if e == 6:
        continue # se salta la iteracion y CONTINUA  en el ciclo para siempre
    print(e)
 

# #***************** MATRICES Y SU RECORRIDO: FOR ANIDADO
# Una matriz en Python se representa comúnmente como una lista de listas 
# (una lista donde cada elemento es otra lista que representa una fila). Para recorrer todos sus elementos con un for, 
# lo ideal es usar bucles anidados (un for dentro de otro).

matriz = [
    [0, 1, 1],  # fila 0
    [1, True, 1],  # fila 1
    [1, 1, 'Edily', [12, 33]]   # fila 2
]

print(matriz[2][2]) #Edily
print(matriz[1][1]) #[12, 33]
print(matriz[2][3][1]) #33



matriz = [
    [0, 8, 9, 0],  # fila 0
    [1, 0, 1, 0],  # fila 1
    [1, 1, 0, 0],   # fila 2
    [1, 1, 0, 0]   # fila 2
]
# matriz[0][0] == 0
# matriz[0][1] == 8
# matriz[0][2] == 9

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
       if i == j:
        print(f'Diagonal matriz[{i}][{j}] = {matriz[i][j]}')

   
 
