# -*- coding: utf-8 -*-

# Ejecute esta aplicación con
# python app1.py
# y luego visite el sitio
# http://127.0.0.1:8050/
# en su navegador.


import dash
from dash import dcc  # dash core components
from dash import html  # dash html components
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(name=__name__, external_stylesheets=external_stylesheets)
server = app.server

# en este primer ejemplo usamos unos datos de prueba que creamos directamente
# en un dataframe de pandas
df = pd.DataFrame(
    {
        "Votos": [5, 9, 4, 9, 2, 3, 4, 9, 5],
        "Candidato": ["Federico Gutierrez", "Gustavo Petro", "Rodolfo Hernández", "Federico Gutierrez", "Gustavo Petro", "Rodolfo Hernández", "Federico Gutierrez", "Gustavo Petro", "Rodolfo Hernández"],
        "Departamento": ["Cundinamarca", "Cundinamarca", "Cundinamarca", "Meta", "Meta", "Meta", "Guaviare", "Guaviare", "Guaviare"],
    }
)

fig = px.bar(df, x="Candidato", y="Votos",
             color="Departamento", barmode="relative")

app.layout = html.Div(children=[
    html.H1(children='Elecciones Colombia 2022'),

    html.Div(children='''
        Gráfico de Barras de votos recibidos por candidadto y por departamento
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    html.Div(children='''
        En este gráfico se observa el número de votos recibidos por cada uno de los candidatos según el departamento.
    '''),

    html.Div(
        className="Columnas",
        children=[
            html.Ul(id='my-list', children=[html.Li(i) for i in df.columns])
        ],
    )
]
)

if __name__ == '__main__':
    app.run(debug=True)
