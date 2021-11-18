import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('Data/gapminderDataFiveYear.csv')

app = dash.Dash()

year_options = []
for year in df['year'].unique():
    year_options.append({'label': str(year), 'value': year})

app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(
        id='year-picker',
        options=year_options,
        value=df['year'].min()
    )
])

# @app.callback(Output(component_id='graph',component_property='figure'),
#               [Input(component_id='year-picker',component_property='value')])
@app.callback(Output('graph','figure'),
              [Input('year-picker','value')])
def update_figure(selected_year):
    filtered_df = df[df['year']==selected_year]

    traces = []
    for this_continent in filtered_df['continent'].unique():
        df_for_this_continent = filtered_df[filtered_df['continent']==this_continent]
        traces.append(go.Scatter(
            x = df_for_this_continent['gdpPercap'],
            y = df_for_this_continent['lifeExp'],
            text = df_for_this_continent['country'],
            mode='markers',
            opacity=0.7,
            marker={'size':15},
            name=this_continent
        ))
    return {
            'data': traces,
            'layout': go.Layout(title='My Plot',
                                xaxis={'title':'GDP Per Cap', 'type':'log'},
                                yaxis={'title':'Life Expectancy'})
           }


if __name__ == '__main__':
    app.run_server()
