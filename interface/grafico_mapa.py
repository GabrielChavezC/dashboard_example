import plotly_express as px
import pandas as pd


def crear_grafico_mapa(df):
    fig_mapa=df.groupby('geolocation_state').agg({
        'valor_total':'sum',
        'geolocation_lat':'mean',
        'geolocation_lng':'mean',
        
    }).reset_index().sort_values(by='valor_total',ascending=False)
    
    fig_mapa=px.scatter_geo(fig_mapa,
                                lat='geolocation_lat',
                                lon='geolocation_lng',
                                scope='south america',
                                template='seaborn',
                                size='valor_total',
                                hover_name='geolocation_state',
                                hover_data={ 'geolocation_lat':False,'geolocation_lng':False},
                                title='Ingresos por estado',
                                
                                )
    return fig_mapa


