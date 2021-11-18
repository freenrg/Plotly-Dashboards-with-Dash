import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input-comp-id',value='Initial Text',type='text'),
    html.Div(id='output-comp-id')
])

@app.callback(Output(component_id='output-comp-id',component_property='children'),
              [Input(component_id='input-comp-id',component_property='value')])
def update_output_div(input_value):
    return "You entered: {}".format(input_value)
    #return f"You entered: {input_value}"


if __name__ == '__main__':
    app.run_server()
