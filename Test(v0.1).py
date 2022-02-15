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

df = pd.read_csv("data/City.csv")

fig = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population", "Status"],
                        color_discrete_sequence=["green"], zoom=3, height=500)
fig.update_layout(mapbox_style="light", mapbox_accesstoken=token)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# dfc = len(df['Status'].unique())
dfc = df.Color.value_counts().green
dfc1 = df.Color.value_counts().yellow
dfc2 = df.Color.value_counts().red
dfc3 = df.Color.value_counts().black

card1 = dbc.CardBody(html.H5(dfc), className='mt-2 text-center'),
card2 = dbc.CardBody(html.H5(dfc1), className='mt-2 text-center'),
card3 = dbc.CardBody(html.H5(dfc2), className='mt-2'),
card4 = dbc.CardBody(html.H5(dfc3), className='mt-2'),

b1 = dbc.Button("Normal conditions ", color="success", className='text-center text-dark'),
b2 = dbc.Button("Non critical error", color="warning", className='text-center text-dark md-6'),
b3 = dbc.Button("Critical error", color="danger", className='text-center text-dark me-6'),
b4 = dbc.Button("Lift doesn`t work", color="dark", className='text-center text-primary me-6'),


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
                # dbc.Row([
                #         html.Div(
                #                 [
                #                         dbc.Button("Normal conditions ", color="success", className='text-center text-dark me-6', ),
                #                         dbc.Button("Non critical error", color="warning", className='text-center text-dark me-6'),
                #                         dbc.Button("Critical error", color="danger", className='text-center text-dark me-6'),
                #                         dbc.Button("Lift doesn`t work", color="dark", className='text-center text-primary me-6'),
                #
                #
                #                 ]
                #         )
                #
                #        ] ),
                dbc.Row([dbc.Col(b1, width=2),
                         dbc.Col(b2, width=2),
                         dbc.Col(b3, width=2),
                         dbc.Col(b4, width=2)], justify="around"),
               
                dbc.Row([dbc.Col(card1, width=2),
                         dbc.Col(card2, width=2),
                         dbc.Col(card3, width=2),
                         dbc.Col(card4, width=2)], justify="around"),
                
                
                
                dbc.Row([
                        
                

                dbc.Row([
                
                        dbc.Col(
                          dcc.Graph(id='map', figure=fig)
                        
                        ),
                        ])
            ])
        ])
 

                



if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
