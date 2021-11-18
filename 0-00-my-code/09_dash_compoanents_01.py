################################################################
# Objective: To build a dashboard that imports OldFaithful.csv
# and displays a scatterplot
# Fields:
#   'D' = month of recording
#   'X' = duration of eruption in minutes (precision: 0.1 min.)
#   'Y' = waiting time until the next eruption in minutes
################################################################

import dash
import dash_core_components as dcc
import dash_html_components as html
#import plotly.graph_objs as go
#import numpy as np
#import pandas as pd

# Launch the application
app = dash.Dash()

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label':'New York City','value':'NYC'},
            {'label':'San Francisco','value':'SF'},
        ],
        value='SF'
    ),
    html.Label('Slider'),
    dcc.Slider( min=-10,max=10,step=0.5,value=0,
                marks={i: i for i in range(-10,10)}),
    html.P(html.Label('Some Radio Items')),
    dcc.RadioItems(
        options=[
            {'label':'New York City','value':'NYC'},
            {'label':'San Francisco','value':'SF'},
        ],
        value='SF'
    )
])

if __name__ == '__main__':
    app.run_server()

# Server clause
