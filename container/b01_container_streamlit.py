import os, sys
sys.path.append(os.getcwd())
import streamlit as st 
from functions.function_format_num import formato_numero
from controller.a01_preproceso import DataStorage
from interface.grafico_mapa import DataStorageGrafico
from interface.grafico_linea_mario import DataStorageGrafico2

#Configuracion
st.set_page_config(layout='wide')
# Accede a los datos calculados de /controller_a01_preproceso de la funcion calcular_ventas 
df_ventas = DataStorage.df_ventas
suma_valor_total = DataStorage.suma_valor_total
suma_cantidad_total = DataStorage.suma_cantidad_total

# Accede a los datos calculados de /controller_a01_preproceso de la funcion calcular_ventas 
graf_mapa = DataStorageGrafico.graf_mapa
graf_linea = DataStorageGrafico2.graf_linea


st.title('Dashboard de Ventas :shopping_trolley:')
col1,col2=st.columns(2)

with col1:
    st.metric('**Total de Revenues**',formato_numero(suma_valor_total,'$'))
    #Se muestra el mapa 
    st.plotly_chart(graf_mapa,use_container_width=True)

with col2:
    st.metric('**Total de Ventas**',formato_numero(suma_cantidad_total))
    #st.plotly_chart(graf_linea, use_container_width = True)
st.dataframe(df_ventas)



