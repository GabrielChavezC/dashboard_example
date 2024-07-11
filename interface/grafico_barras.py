import plotly_express as px
from controller.a01_preproceso import DataStorage

df_barras = DataStorage.df_vista_revenue_productos

# Módulo para almacenar las variables calculadas
class DataStorageGraficoBarras:
    #Variable Grafico
    graf_barras=None
    

def crear_grafico_mapa(graf_mapa):
    graf_barras=px.bar(graf_mapa,
                       x='valor_total',
                       y='product_category_name',
                       text='valor_total',
                       title='Top Ingresos por Producto ($)'
                                
                                )
    graf_barras.update_layout(yaxis_title='Pruductos',
                              xaxis_title='Ingresos ($)',
                              showlegend=False)
    graf_barras.update_traces(texttemplate='%{text:.3s}')
    return graf_barras

# Calcula las ventas y guarda los resultados en el módulo DataStorage
DataStorageGraficoBarras.graf_barras = crear_grafico_mapa(df_barras)
