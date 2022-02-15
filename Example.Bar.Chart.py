from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import dash_table as dt
from dash.dependencies import Input, Output, State
app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "Amount2": [4, 1, 2, 2, 4, 15],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})



app.layout = html.Div([


html.Button('Map', id='filter', n_clicks=0, className='mr15',
            style={'white-space': 'pre-wrap', 'word-break': 'break-all',
                   'border': '1px solid black', 'text-align': 'center',
                   'padding': '12px 12px 12px 12px', 'color': 'blue',
                   'margin-top': '3px'}
            ),
    html.Button('Button 2', id='btn-nclicks-2', n_clicks=0),
    html.Button('Button 3', id='btn-nclicks-3', n_clicks=0),
    # html.Div(id='container-button-timestamp')


    # dbc.Row([ dbc.Col(dbc.Button(children='Map', id='filter', n_clicks=0, className='mr-2')),
    #         dbc.Col(dbc.Button(children='Map1', id='filter1', n_clicks=0, className='mr-2')),
    #         dbc.Col(dbc.Button(children='Map2', id='filter2', n_clicks=0, className='mr-2')),


  #         ]),
    dcc.Graph( id='example-graph')
])
@app.callback(
    Output("example-graph", "figure"),
    [Input("filter", "n_clicks")])
def display_graph(n_clicks):
    if n_clicks % 2 == 0:
       x, y = "Fruit", "Amount"
    else:
       x, y = "Fruit", "Amount2"

    fig = px.bar(df, x=x, y=y, color="City", barmode="group")
   #fig = px.bar(df, x, y)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)