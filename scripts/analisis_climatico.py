import pandas as pd

# Leer dataset
df = pd.read_csv('../datos/dataset_climatico.csv')

# Mostrar primeras filas
print(df.head())

# Calcular promedio de temperatura
promedio = df['temperatura'].mean()

print('Temperatura promedio:', promedio)