import csv
f = open('./data.csv')
csv_f = csv.reader(f)
count, s2, s4, s6, ze = 0, 0, 0, 0, 0
for row in csv_f:
    count += 1
    if row[10] == 'Menos de 3':
        s2 += 1
    elif row[10] == 'Entre 3 y 5':
        s4 += 1
    elif row[10] == '7 o más':
        s6 += 1
    else:
        ze += 1
print("Total: {} \n2do: {} \n4to: {} \n6to: {}. \nCero: {}".format(count,s2,s4,s6,ze))

frecR2, frecR4, frecR6 = s2/count, s4/count, s6/count
countFR = frecR2+frecR4+frecR6
print("Total frecuencia relativa: {} \n2do: {} \n4to: {} \n6to: {}".format(countFR,frecR2,frecR4,frecR6))


