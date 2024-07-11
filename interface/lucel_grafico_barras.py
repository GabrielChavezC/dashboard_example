"""
Vendedores
"""

import plotly_express as px
from controller.a01_preproceso import DataStorage

review_vendedors = DataStorage.df_review


class DataStoragePizza:
    graf_pizza=None


def crear_grafico_pizza(df):
	colors = ['#0077b6', '#1A4D83', '#063970', '#2f567D', '#4B6A92']
	fig = px.pie(df,
		values = 'total_ventas',
		names = 'review_score',
		title = 'Calificación de las Ventas',
		color_discrete_sequence = colors
	)

	fig.update_layout(yaxis_title = 'Calificación', xaxis_title='Ventas', showlegend=False)
	fig.update_traces(textposition = 'inside', textinfo='percent+label', insidetextfont=dict(size=16))

	return fig

DataStoragePizza.graf_pizza = crear_grafico_pizza(review_vendedors)