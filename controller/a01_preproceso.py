
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
    #Variable grafico de barras
    df_vista_revenue_productos=None
    
    

#Creacion variable total
df_ventas['valor_total']=(df_ventas['price']*df_ventas['cantidad_itens'])+(df_ventas['freight_value']*df_ventas['cantidad_itens'])
    # Cambio a datetime
df_ventas["order_purchase_timestamp"] = pd.to_datetime(df_ventas["order_purchase_timestamp"])

DataStorage.df_ventas=(df_ventas)
df_ventas=df_ventas.copy()

    

    
    
# Esta funcion crea el calculo de las variables
def calcular_ventas(data):
    suma_valor_total=data['valor_total'].sum()
    suma_cantidad_total=data['cantidad_itens'].sum()
    return suma_valor_total, suma_cantidad_total


# Calcula las ventas y guarda los resultados en el módulo DataStorage
DataStorage.suma_valor_total, DataStorage.suma_cantidad_total = calcular_ventas(df_ventas)


def crear_vista_grafico_mapa(data):
    data=data.groupby('geolocation_state').agg({
        'valor_total':'sum',
        'geolocation_lat':'mean',
        'geolocation_lng':'mean',
        
    }).reset_index().sort_values(by='valor_total',ascending=False)
    return data


DataStorage.df_mapa= crear_vista_grafico_mapa(df_ventas)

# Para el gráfico de ganancias mensuales a lo largo de los años-------------------------------------------------------------------------------Mario


def crear_ganancias_mensuales(data):
    revenues_monthly = data.set_index('order_purchase_timestamp').groupby(pd.Grouper(freq = 'ME'))['valor_total'].sum().reset_index()
    revenues_monthly['Year'] = revenues_monthly['order_purchase_timestamp'].dt.year
    revenues_monthly['Month'] = revenues_monthly['order_purchase_timestamp'].dt.month_name()
    revenues_monthly = revenues_monthly[revenues_monthly['Year']>2016]
    return revenues_monthly

DataStorage.revenues_monthly= crear_ganancias_mensuales(df_ventas)

# Grafico de barras-------------------------------------------------------------Gabo 
def crear_vista_grafico_de_barras(data):
    df_vista_revenue_productos=data.groupby('product_category_name')[['valor_total']].sum().sort_values('valor_total',ascending=True).reset_index().tail(10)
    return df_vista_revenue_productos
DataStorage.df_vista_revenue_productos= crear_vista_grafico_de_barras(df_ventas)