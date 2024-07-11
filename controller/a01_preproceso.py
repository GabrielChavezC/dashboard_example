
import os, sys
sys.path.append(os.getcwd())
# Lee los datos de ventas
import pandas as pd 

df_ventas = pd.read_csv('base/data/input/base_ventas.csv')

# Módulo para almacenar las variables calculadas
class DataStorage:
    df_ventas = None
    suma_valor_total = None
    suma_cantidad_total = None
    #Para gráfico 2
    revenues_monthly = None
    #Variable Grafico
    df_mapa=None
    #variable Ventas
    revenues_monthly=None
    
    
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

# Para el gráfico de ganancias mensuales a lo largo de los años-------------------------------------------------------------------------------Mario

# para el gráfico línea
def convertir_time(df):
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    
    return df

# Convirtiendo
df_ventas = convertir_time(df_ventas)

def crear_ganancias_mensuales(data):
    revenues_monthly = data.set_index('order_purchase_timestamp').groupby(pd.Grouper(freq = 'ME'))['valor_total'].sum().reset_index()
    revenues_monthly['Year'] = revenues_monthly['order_purchase_timestamp'].dt.year
    revenues_monthly['Month'] = revenues_monthly['order_purchase_timestamp'].dt.month_name()
    revenues_monthly = revenues_monthly[revenues_monthly['Year']>2016]
    return revenues_monthly

# %%
DataStorage.revenues_monthly= crear_ganancias_mensuales(df_ventas)