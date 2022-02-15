import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import Dash, Input, Output, callback, dash_table



token = mapbox_access_token = 'pk.eyJ1Ijoib2xla3NhbmRyMTcxNyIsImEiOiJja3piZW55eHkwN21vMnZwODloenR0Z2p3In0.NYw3yhwYd6QJfEB23IcgIQ'

df = pd.read_csv("data/City.csv")
fig = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population", "Status"],
                        color_discrete_sequence=["green"], zoom=3, height=500)
fig.update_layout(mapbox_style="light", mapbox_accesstoken=token)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


df1 = pd.read_csv('https://git.io/Juf1t')


app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{'name': 'viewport',
                'content': 'width=device-width, initial-scale=1.0'}]
    )

# -----------------------------------------------------------
# LAYOUT

app.layout = dbc.Container(
        children=[
                dbc.Row(
                        dbc.Col(
                                html.H3("Address View"),
                                width={'size': 6, 'offset': 0}, style={'margin-top': '8px'},
                        ),
                
                ),
                dbc.Row(
                        dbc.Col([
                                dcc.Graph(id='map', figure=fig)
        
                        ], width=6),
                
                ),
                dbc.Row(
                        dbc.Col(
                                html.H3("List elevators here"),
                                width={'size': 6, 'offset': 0}, style={'margin-top': '8px'},
                        ),
                
                ),
                dbc.Row(
                        dash_table.DataTable(df1.to_dict('records'),[{"name": i, "id": i} for i in df1.columns], id='tbl'),
                
                ),
                
        
        ],
        # style={'margin-left': '25px',
        #       'margin-right': '25px'},

)


# -----------------------------------------------------------
# CALLBACKS



if __name__ == "__main__":
    app.run_server(debug=True, port=8002)
