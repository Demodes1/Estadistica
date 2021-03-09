import csv
f = open('./data.csv') # Accedemos a la data
csv_f = csv.reader(f) # Leemos la data
count, r1, r2, r3, r0 = 0, 0, 0, 0, 0 # Declaramos variables para los X numero de posibilidades de respuesta
for row in csv_f:
    count += 1 # Tomar cuenta de toda la data (debe dar 100, incluye el titulo de la columna
    if row[10] == 'Menos de 3': # En row ponemos el numero de columna que estudiamos y en la comparacion el dato de fila
        r1 += 1
    elif row[10] == 'Entre 3 y 5':
        r2 += 1
    elif row[10] == '7 o más':
        r3 += 1
    else:
        r0 += 1 # Si no hay respuesta o es valida, la tomamos como nula
print("Total: {} \n1ro: {} \n2do: {} \n3ro: {}. \nCero: {}".format(count,r1,r2,r2,r0)) #Imprimimos el total de frecuencia

frecR1, frecR2, frecR3 = r1/count, r2/count, r3/count # Obtenemos la frecuencia relativa
countFR = frecR1 + frecR2 + frecR3
print("Total frecuencia relativa: {} \n1ro: {} \n2do: {} \n3ro: {}".format(countFR,frecR1,frecR2,frecR3)) #Imprimimos la frecuencia relativa


