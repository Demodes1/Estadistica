import pandas as pd 
import csv
data = pd.read_csv('./data.csv')
data.head()
# El dato total te da la frecuencia
total = (data 
  .groupby("¿Usas cubrebocas en los lugares públicos?")
  .agg(frequency=("¿Usas cubrebocas en los lugares públicos?", "count")))
# Estas funciones en base a la frecuencia, te dan la frecuencia acomulada
total["cum_frequency"] = total["frequency"].cumsum()
print(total)
