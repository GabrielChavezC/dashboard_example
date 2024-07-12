import os, sys
sys.path.append(os.getcwd())
import streamlit as st 
import pandas as pd 
from functions.function_format_num import formato_numero
from controller.a01_preproceso import DataStorage
from interface.grafico_mapa import crear_grafico_mapa
from interface.grafico_linea_mario import crear_grafico_linea
from interface.grafico_barras import crear_grafico_barras
from interface.lucel_grafico_pizza import crear_grafico_pizza

#Configuracion
st.set_page_config(layout='wide')
# Accede a los datos calculados de /controller_a01_preproceso de la funcion calcular_ventas 
df_ventas = DataStorage.df_ventas

#Configuramos los filtros----------------------------------------------------------

st.sidebar.title('Filtros')

estados = sorted(list(df_ventas['geolocation_state'].unique()))
ciudades = st.sidebar.multiselect('Estados', estados)

productos = sorted(list(df_ventas['tipo_producto'].dropna().unique()))
productos.insert(0, 'Todos')
producto = st.sidebar.selectbox('Productos', productos)

años = st.sidebar.checkbox('Todo el periodo', value=True)
if not años:
	año = st.sidebar.slider('Año', df_ventas['order_purchase_timestamp'].dt.year.min(), df_ventas['order_purchase_timestamp'].dt.year.max())

# Interacción de filtros------------------------------------------------------------
if ciudades:
    df_ventas=df_ventas[df_ventas['geolocation_state'].isin(ciudades)]


graf_mapa=crear_grafico_mapa(df_ventas)
graf_linea=crear_grafico_linea(df_ventas)
graf_barras=crear_grafico_barras(df_ventas)
graf_pizza=crear_grafico_pizza(df_ventas)

# Contenedor de la visualizacion
st.title('Dashboard de Ventas :shopping_trolley:')
col1,col2=st.columns(2)

with col1:
    st.metric('**Total de Revenues**',formato_numero(df_ventas['valor_total'].sum(),'$'))
    #Se muestra el mapa 
    st.plotly_chart(graf_mapa,use_container_width=True)
    #Se muestra el grafico de barras
    st.plotly_chart(graf_barras,use_container_width=True)

with col2:
    st.metric('**Total de Ventas**',formato_numero(df_ventas['cantidad_itens'].sum()))
    #Agregando grafico de linea 
    st.plotly_chart(graf_linea, use_container_width = True)
    #Agregando grafico de pizza 
    st.plotly_chart(graf_pizza, use_container_width = True)
st.dataframe(df_ventas)



