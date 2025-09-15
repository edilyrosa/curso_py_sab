#* ⛹🏽‍♀️⛹🏽‍♂️⛹🏽🏋🏽‍♀️ EJERCICIO # 1: El programa debe pedirle al usuario con input() que ingrese una 
# cadena de texto (una palabra o frase), para verifica si es un palíndromo. Un palíndromo es 
# una palabra o frase que se lee igual de izquierda a derecha y de derecha a izquierda, ignorando 
# los espacios y las mayúsculas, ejemplo: "reconocer“ y "Anita lava latina“.
# 1. Pedir entrada al usuario


#*********************************⛹🏽‍♀️⛹🏽‍♂️⛹🏽🏋🏽‍♀️ EJERCICIO 1********************************
#* replace(" ", "")
# cadena.replace(substring_antiguo, substring_nuevo, conteo)
# substring_antiguo → el texto que queremos reemplazar.
# substring_nuevo → el texto por el que lo queremos cambiar.
# conteo (opcional) → cuántas veces queremos reemplazarlo (por defecto reemplaza todas).
text = "Anita lava latina"
sin_spac = text.replace(' ', '')
print(text, sin_spac)
# 2. Normalizar: quitar espacios y pasar a minúsculas

#* Acceso y modificación por rangos (slicing)
# De múltiples elementos a la vez usando el operador de corte [:].
# lista[inicio:fin:paso]
# inicio → índice donde comienza (incluido).
# fin → índice donde termina (excluido).
# paso → salto entre elementos (opcional, por defecto 1).

# lista[inicio:fin:paso]

mi_lista = [1, 2, 3, 4, 5, 6]
print(mi_lista[1:4]) #[2, 3, 4]
print(mi_lista[:4]) #[1, 2, 3, 4]
print(mi_lista[1:]) #[2, 3, 4, 5, 6]

print(mi_lista[:]) #[1, 2, 3, 4, 5, 6]

mi_lista = [1, 2, 3, 4, 5, 6]
print(mi_lista[2:5:1]) #[3, 5]

print(mi_lista[::-1]) #[6, 5, 4, 3, 2, 1]


#* ⛹🏽‍♀️⛹🏽‍♂️⛹🏽🏋🏽‍♀️ EJERCICIO # 1: El programa debe pedirle al usuario con input() que ingrese una 
# cadena de texto (una palabra o frase), para verifica si es un palíndromo. Un palíndromo es 
# una palabra o frase que se lee igual de izquierda a derecha y de derecha a izquierda, ignorando 
# los espacios y las mayúsculas, ejemplo: "reconocer“ y "Anita lava latina“.

entrada = input('Ingrese una palabra o frase: ')
# normaliza la entrada
text_limpio = entrada.replace(' ', '').lower()

if text_limpio == text_limpio[::-1]:
    print('es palíndromo')
else: print('NO es palíndromo')

