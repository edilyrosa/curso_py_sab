# La diagonal principal de una matriz cuadrada, son los elementos donde el índice de fila es 
# igual al índice de columna, es decir, donde i == j.
matriz = [
    [0, 1, 1],  # fila 0
    [1, 0, 1],  # fila 1
    [1, 1, 0]   # fila 2
]

for i in range(len(matriz)):          # recorre 0, 1, 2 - indices de filas
    for j in range(len(matriz[i])):   # recorre 0, 1, 2 - indices de columnas en fila i
       if i == j:
            print(f"Diagonal[{i}][{j}] = {matriz[i][j]}")