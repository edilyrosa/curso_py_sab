
with open('mi_archivo_clase.txt', 'w') as f:
    f.write('Esta sera la primera linea. \n')
    f.write('Esta sera la segunda linea. \n')
    f.write('Esta sera la tercera linea. \n')
    f.write('Testing. \n')
    f.write('Estamos . \n')
    
with open('mi_archivo_clase.txt', 'a') as f:
    f.write('Desde la funcion de append. \n')
    
    

with open('mi_archivo_clase.txt', 'r') as f:
    # linea1 = f.readline()
    # linea2 = f.readline()
    # linea3 = f.readline()
    # resto = f.read()
    # print('📖Leyendo linea a linea')
    # print(linea1, linea2, linea3)
    # print(resto)
    todo = f.readlines() #<class 'list'>
    for i, e in enumerate(todo, start=1):
        print(f'{i}. {e}')
       
 
#  TODO: TERMINAR ACA CON CREAR Y ELIMINAR ARCHIVOS 