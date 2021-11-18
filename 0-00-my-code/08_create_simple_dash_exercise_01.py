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
import plotly.graph_objs as go
import numpy as np
import pandas as pd

# Launch the application
app = dash.Dash()

# Create a DataFrame from the csv file
df = pd.read_csv('Data/OldFaithful.csv')

# Create a Dash Layout that contains a Graph component
app.layout = html.Div(
    [dcc.Graph(
        id='old_faithful_plot',
        figure = {
            'data':[
                go.Scatter(
                    x = df['X'],
                    y = df['Y'],
                    mode='markers'
                )
            ],
            'layout':
                go.Layout(
                    title='Old Faithful Eruptions',
                    xaxis={'title':'Duration of Eruption (Minutes)'},
                    yaxis={'title':'Interval to next eruption (Minutes)'}
                )
        }
    )]
)

if __name__ == '__main__':
    app.run_server()

# Server clause
