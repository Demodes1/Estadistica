import pandas as pd 
data = pd.read_csv('./data.csv') # Leemos la data del csv
data.head()
# El dato "total", te da la frecuencia
total = (data 
  .groupby("¿Usas cubrebocas en los lugares públicos?") # Aqui se tiene que escribir el nombre de la columna
  .agg(frequency=("¿Usas cubrebocas en los lugares públicos?", "count"))) # Y aqui tambien
# Estas funciones en base a la frecuencia, te dan la frecuencia acomulada
total["cum_frequency"] = total["frequency"].cumsum()
print(total) # Frecuenca
print(total/99) # Frecuencia relativa (99 es total de elementos)
