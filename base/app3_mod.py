import dash
from dash import dcc  # dash core components
from dash import html  # dash html components
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
print(df.columns)

# Create the agg data
filtered_df = df.groupby(['year', 'continent']).agg(
    meanLifeExp=('lifeExp', 'mean'), maxLifeExp=('lifeExp', 'max'), minLifeExp=('lifeExp', 'min'), stdLifeExp=('lifeExp', 'std')).reset_index()

# Initialize the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# Variables
continents = df["continent"].unique()
marks = {0: 'Todos'}
cont = 1
for continent in continents:
    marks[cont] = continent
    cont += 1
colors = {
    'Asia': 'LightSkyblue',
    'Europe': 'LightSalmon',
    'Africa': 'LightSeaGreen',
    'Americas': 'LightSlateGray',
    'Oceania': 'MediumPurple'
}

# Layout
app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='continent-slider',
        min=0,
        max=5,
        value=0,
        marks=marks,
        step=None
    )
])

# Update


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('continent-slider', 'value')])
def update_figure(selected_continent):

    if marks[selected_continent] == 'Todos':
        fig = go.Figure()

        for continent in continents:
            final_df = filtered_df[filtered_df.continent ==
                                   continent]

            fig.add_trace(go.Scatter(
                x=final_df["year"],
                y=final_df["meanLifeExp"],
                mode='lines',
                name='mean'+continent,
                line=dict(color=colors[continent], width=2),
            ))

        return fig

    else:
        final_df = filtered_df[filtered_df.continent ==
                               marks[selected_continent]]

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=final_df["year"],
            y=final_df["meanLifeExp"]-final_df["stdLifeExp"],
            # y=final_df["minLifeExp"],
            mode='lines',
            name='std_min',
            opacity=0.75,
            line=dict(color=colors[marks[selected_continent]], width=0.5),
            showlegend=False
        ))

        fig.add_trace(go.Scatter(
            x=final_df["year"],
            y=final_df["meanLifeExp"],
            mode='lines',
            name='mean',
            fill='tonexty',
            line=dict(color=colors[marks[selected_continent]], width=2),
        ))

        fig.add_trace(go.Scatter(
            x=final_df["year"],
            y=final_df["meanLifeExp"]+final_df["stdLifeExp"],
            # y=final_df["maxLifeExp"],
            mode='lines',
            name='std_max',
            opacity=0.75,
            fill='tonexty',
            line=dict(color=colors[marks[selected_continent]], width=0.5),
            showlegend=False
        ))

        return fig


if __name__ == '__main__':
    app.run(debug=True)
