
import os, sys
sys.path.append(os.getcwd())
# Lee los datos de ventas
import pandas as pd 

df_ventas = pd.read_csv('base/data/input/base_ventas.csv')

# Módulo para almacenar las variables calculadas
class DataStorage:
    df_ventas = None

#Creacion variable total
df_ventas['valor_total']=(df_ventas['price']*df_ventas['cantidad_itens'])+(df_ventas['freight_value']*df_ventas['cantidad_itens'])
    # Cambio a datetime
df_ventas["order_purchase_timestamp"] = pd.to_datetime(df_ventas["order_purchase_timestamp"])

df_ventas['tipo_producto'] = df_ventas['product_category_name'].str.split('_').str[0]


DataStorage.df_ventas=(df_ventas)
df_ventas=df_ventas.copy()

    