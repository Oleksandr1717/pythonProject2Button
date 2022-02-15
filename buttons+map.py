import dash
import dash_core_components as dcc
import dash_html_components as html
# from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
#import pandas_datareader.data as web
# import datetime

#token = open("pk.eyJ1Ijoib2xla3NhbmRyMTcxNyIsImEiOiJja3piZW55eHkwN21vMnZwODloenR0Z2p3In0.NYw3yhwYd6QJfEB23IcgIQ").read() # you will need your own token
token = mapbox_access_token = 'pk.eyJ1Ijoib2xla3NhbmRyMTcxNyIsImEiOiJja3piZW55eHkwN21vMnZwODloenR0Z2p3In0.NYw3yhwYd6QJfEB23IcgIQ'

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["green"], zoom=3, height=500)
fig.update_layout(mapbox_style="light", mapbox_accesstoken=token)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})




app = dash.Dash( __name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{'name': 'viewport',
                'content': 'width=device-width, initial-scale=1.0'}]
    )

# Layout section: Bootstrap (https://hackerthemes.com/bootstrap-cheatsheet/)
# ************************************************************************
app.layout = dbc.Container(
        [
                
                dbc.Row(
                        dbc.Col(
                            html.H1(
                                "Superviser",
                                className='text-center text-dark mb-4'
                                ),
                            width=12
                            )
                ),
                dbc.Row([
                        html.Div(
                                [
                                        dbc.Button("Normal conditions", color="success", className='text-center text-dark me-4'),
                                        dbc.Button("Non critical error", color="warning", className='text-center text-dark me-4'),
                                        dbc.Button("Critical error", color="danger", className='text-center text-dark me-4'),
                                        dbc.Button("Lift doesn`t work", color="dark", className='text-center text-primary me-4'),
                                        
                                        
                                ]
                        )
                        
                       ] ),
                dbc.Row([
                        
                
# html.Div([
#
#
# html.Button('Map', id='filter', n_clicks=0, className='mr15',
#             style={'white-space': 'pre-wrap', 'word-break': 'break-all',
#                    'border': '1px solid black', 'text-align': 'center',
#                    'padding': '12px 12px 12px 12px', 'color': 'blue',
#                    'margin-top': '3px'}
#             ),
#     html.Button('Button 2', id='btn-nclicks-2', n_clicks=0),
#     html.Button('Button 3', id='btn-nclicks-3', n_clicks=0),
#
#                 ] ),
                dbc.Row([
                
                        dbc.Col(
                          dcc.Graph(id='map', figure=fig)
                        
                        ),
                        ])
            ])
        ])
 

                



if __name__ == '__main__':
    app.run_server(debug=True, port=8000)

# https://youtu.be/0mfIK8zxUds