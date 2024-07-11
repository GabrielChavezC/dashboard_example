import plotly_express as px
from controller.a01_preproceso import DataStorage

df_mapa = DataStorage.df_mapa

# Módulo para almacenar las variables calculadas
class DataStorageGrafico:
    #Variable Grafico
    graf_mapa=None


def crear_grafico_mapa(graf_mapa):
    graf_mapa=px.scatter_geo(graf_mapa,
                                lat='geolocation_lat',
                                lon='geolocation_lng',
                                scope='south america',
                                template='seaborn',
                                size='valor_total',
                                hover_name='geolocation_state',
                                hover_data={ 'geolocation_lat':False,'geolocation_lng':False},
                                title='Ingresos por estado',
                                
                                )
    return graf_mapa

# Calcula las ventas y guarda los resultados en el módulo DataStorage
DataStorageGrafico.graf_mapa = crear_grafico_mapa(df_mapa)
