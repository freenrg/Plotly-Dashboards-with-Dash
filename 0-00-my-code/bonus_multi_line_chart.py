# basic.py
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('SourceData/nst-est2017-alldata.csv')

df2 = df[df['DIVISION'] == '1']
df2.set_index('NAME', inplace=True)

list_of_pop_cols = [col for col in df2.columns if col.startswith('POP')]
df2 = df2[list_of_pop_cols]

#print(df2)
#print(df2.loc['Vermont'])

data = [ go.Scatter(x=df2.columns,
                    y=df2.loc[name],
                    mode='lines',
                    name=name) for name in df2.index]

pyo.plot(data)


'''
x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

trace0 = go.Scatter( x       = x_values,
                     y       = y_values+5,
                     mode    = 'markers',
                     name    = 'mymarkers'
                  )

trace1 = go.Scatter( x       = x_values,
                     y       = y_values,
                     mode    = 'lines',
                     name    = 'mylines'
                  )

trace2 = go.Scatter( x       = x_values,
                     y       = y_values-5,
                     mode    = 'lines+markers',
                     name    = 'myfavorite'
                  )

data = [trace0,trace1,trace2]

layout = go.Layout( title       = 'Line Charts')

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)
'''
