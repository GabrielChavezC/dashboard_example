
import os, sys
sys.path.append(os.getcwd())
# Lee los datos de ventas
import pandas as pd 

df_ventas = pd.read_csv('base/data/input/base_ventas.csv')

df_ventas.info()

# Módulo para almacenar las variables calculadas
class DataStorage:
    df_ventas = None
    suma_valor_total = None
    suma_cantidad_total = None
    #Variable Grafico
    df_mapa=None

# Esta funcion crea el calculo de las variables
def calcular_ventas(data):
    data['valor_total']=(data['price']*data['cantidad_itens'])+(data['freight_value']*data['cantidad_itens'])
    suma_valor_total=data['valor_total'].sum()
    suma_cantidad_total=data['cantidad_itens'].sum()
    return data, suma_valor_total, suma_cantidad_total


# Calcula las ventas y guarda los resultados en el módulo DataStorage
DataStorage.df_ventas, DataStorage.suma_valor_total, DataStorage.suma_cantidad_total = calcular_ventas(df_ventas)


def crear_vista_grafico_mapa(data):
    data['valor_total']=(data['price']*data['cantidad_itens'])+(data['freight_value']*data['cantidad_itens'])
    data=data.groupby('geolocation_state').agg({
        'valor_total':'sum',
        'geolocation_lat':'mean',
        'geolocation_lng':'mean',
        
    }).reset_index().sort_values(by='valor_total',ascending=False)
    return data


    
DataStorage.df_mapa= crear_vista_grafico_mapa(df_ventas)



# %%
