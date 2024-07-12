import plotly_express as px
import pandas as pd 
    

def crear_grafico_barras(data):
    df_vista_revenue_productos=data.groupby('product_category_name')[['valor_total']].sum().sort_values('valor_total',ascending=True).reset_index().tail(10)
   
    graf_barras=px.bar(df_vista_revenue_productos,
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

