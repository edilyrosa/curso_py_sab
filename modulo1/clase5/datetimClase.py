from datetime import datetime
hoy = datetime.now()
print(hoy) #2025-09-27 21:07:19.089166

dia_semana = hoy.weekday()
print(dia_semana) #5
dias = ['Lunes', 'Martes', "Miercoles", "Ju", 'Vi', "sab", 'Dom']
print(dias[dia_semana]) #sab

f_formateada = hoy.strftime('%d/%m/%y %H:%M:%S.%f') #27/09/25 21:14:46.172299
f_formateada = hoy.strftime('%a %d %b %Y, %I:%M%p') #Sat 27 Sep 2025, 09:15PM
print(f_formateada)