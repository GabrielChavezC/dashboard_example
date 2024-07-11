import plotly.express as px
from controller.a01_preproceso import DataStorage

# Módulo para almacenar las variables calculadas
class DataStorageGrafico2:
    #Variable Grafico
    graf_linea=None

revenues_monthly = DataStorage.revenues_monthly

def crear_grafico_linea(df):  
    fig = px.line(revenues_monthly,
                  x = 'Month',
                  y = 'valor_total',
                  markers = True,
                  range_y = (0, revenues_monthly.max()),
                  color = 'Year',
                  line_dash = 'Year',
                  title = 'Ingresos mensuales')
    
    fig.update_layout(yaxis_title = 'Ingresos ($)')
    return fig

# Calcula las ventas y guarda los resultados en el módulo DataStorage
DataStorageGrafico2.graf_linea = crear_grafico_linea(revenues_monthly)
graf_linea = crear_grafico_linea(revenues_monthly)
