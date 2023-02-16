import dash
from dash import dcc  # dash core components
from dash import html  # dash html components
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(
    [
        html.H1(
            "Modificación aplicación"),
        html.Div(children=[
            "Ingrese su username: ",
            dcc.Input(id='input-username',
                      placeholder="username",
                      type="text",
                      value="")
        ]),
        html.Div(children=[
            "Digite una contraseña: ",
            dcc.Input(id='input-password',
                      placeholder="password",
                      type="password",
                      value="")
        ]),
        html.Br(),
        html.Div("", id='output')
    ]
)


@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input-username', component_property='value'),
     Input(component_id="input-password", component_property='value')]
)
def update_output_div(input_value, input_value2):
    if input_value != "":
        if input_value2 != "":
            return f'-> Gracias por registrarte, {input_value}'
        else:
            return f'-> Por favor llene la contraseña'
    else:
        return "-> Por favor digite un username"


if __name__ == '__main__':
    app.run(debug=True)
