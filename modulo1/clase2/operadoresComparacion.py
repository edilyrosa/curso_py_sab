print('Operadores de Comparacion')
print('Comprar TDD Numericos')
print('7 == 7 es', 7 == 7)                   # True
print('7 == 7.0 es', 7 == 7.0)               # True
print('7 == "7" es', 7 == '7')               #! Flase
print('7 == int("7") es', 7 == int('7'))     # True
print('7 != 7 es', 7 != 7)                   # False
print('7 > 7 es', 7 > 7)                     # False
print('7 >= 7 es', 7 >= 7)                   # True


# print( 'vamos a sumar 7 + 7 = ', 7+7) #Suma
# print( 'vamos a sumar 7 + "7"', 7+int("7")) #Concatenacion

# print('---'*8)
# num = int(input('digite un num: '))
# print('digito = ', num)
# print('TDD digito = ', type(num))
# print(' lo digitado mas 100 = ', num+100)



print('---'*8)
print('Comprar TDD Bool')
print('True == 1 es', True == 1)    # True
print('False == 0 es', False == 0)  # True
print('False == 1 es', False == 1)  # True

print('---'*8)
print('Comprar TDD Str')
print(ord('a'), ord('A'), ord("\a")) #97 65 7
print('"a" == "a" es', "a" == "a")    # True
print('"a" == "A" es', "a" == "A")    #! False
print('"a"> "A" es', "a" > "A")       # True
print('7 == ord("\a") es', 7 == ord("\a"))    # True

