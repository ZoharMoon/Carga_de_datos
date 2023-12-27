# main.py
import pandas as pd
from dataset import dataset

# Convertir el conjunto de datos en un DataFrame de Pandas
df = pd.DataFrame(dataset)

# Mostrar el DataFrame
print(df)

# Separar el dataframe en dos según el valor de la columna 'is_dead'
df_perecieron = df[df['is_dead'] == 1]
df_no_perecieron = df[df['is_dead'] == 0]

# Calcular los promedios de las edades de cada dataset e imprimir.
promedio_edad_perecieron = df_perecieron['Edad'].mean()
promedio_edad_no_perecieron = df_no_perecieron['Edad'].mean()

print("Promedio de edades de personas que perecieron:", promedio_edad_perecieron)
print("Promedio de edades de personas que no perecieron:", promedio_edad_no_perecieron)
