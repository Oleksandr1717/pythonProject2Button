import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

mapbox_access_token = 'pk.eyJ1Ijoib2xla3NhbmRyMTcxNyIsImEiOiJja3piZW55eHkwN21vMnZwODloenR0Z2p3In0.NYw3yhwYd6QJfEB23IcgIQ'

df = pd.read_csv("data/City.csv")
dfc = df.Color.value_counts().green
dfc1 = df.Color.value_counts().yellow
dfc2 = df.Color.value_counts().red
dfc3 = df.Color.value_counts().black

card1 = dbc.Card(
        dbc.CardBody(
                [
                        dbc.Button(
                                "Predictive action", color="success",
                                className='text-center text-dark me-3',
                                id='btn-nclicks-1', n_clicks=0
                        ),
                        html.H5(dfc, className="card-title", style={'text-align': 'center'}),
                
                ]
        )
),
card2 = dbc.Card(
        dbc.CardBody(
                [
                        dbc.Button(
                                "Non critical error", color="warning",
                                className='text-center text-dark me-3'
                        ),
                        html.H5(dfc1, className="card-title"),
                
                ]
        )
),
card3 = dbc.Card(
        dbc.CardBody(
                [
                        dbc.Button(
                                "Critical error", color="danger",
                                className='text-center text-dark me-3'
                        ),
                        html.H5(dfc2, className="card-title"),
                
                ]
        )
),
card4 = dbc.Card(
        dbc.CardBody(
                [
                        dbc.Button(
                                "Lift doesn`t work", color="dark",
                                className='text-center text-primary me-3'
                        ),
                        html.H5(dfc3, className="card-title"),
                
                ]
        )
)


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )


#-----------------------------------------------------------
# LAYOUT

app.layout = dbc.Container(children=[
        dbc.Row(
                dbc.Col(
                       html.H3("Equipment status - Main View"),
                        width={'size': 6, 'offset': 0},style={'margin-top': '8px'},
                ),
        
        ),
        dbc.Row([
                dbc.Col(card1, width=3
                
                ),
                dbc.Col(card2, width=3
        
                ),
                dbc.Col(card3, width=3
        
                ),
                dbc.Col(card4, width=3
        
                )], justify="start"
        
        ),
        dbc.Row(
                dbc.Col(
                
                        dcc.Checklist(
                                id='Status_item',
                                options=[{'label': str(b), 'value': b} for b in sorted(df['Status'].unique())],
                                value=[b for b in sorted(df['Status'].unique())],
                                labelClassName="mr-10"
                
                        ),
                        width=12
                )
        
        ),
        dbc.Row(
                dbc.Col(
                        dcc.Graph(
                                id='map1',
                                config={'displayModeBar': False, 'scrollZoom': True},
                                style={'height': '50vh'}
                        )
        
                ),
        
        ),
        dbc.Row(
                dbc.Col(
                        html.H3("Client Locations"),
                        width={'size': 6, 'offset': 0},
                ),
        
        ),
        dbc.Row(
                dbc.Col(
                        dcc.Graph(
                                id='map2',
                                config={'displayModeBar': False, 'scrollZoom': True},
                                style={'height': '50vh'}
                        )
        
                ),
        
        )

],
         # style={'margin-left': '25px',
         #       'margin-right': '25px'},
       
)

#-----------------------------------------------------------
# CALLBACKS
@app.callback(
        Output('map1', 'figure'),
        [Input('Status_item', 'value')]
)
def update_figure(chosen_Status):
    df_sub = df[(df['Status'].isin(chosen_Status))
    ]
    
    # Create figure
    locations = [go.Scattermapbox(
            lon=df_sub['lon'],
            lat=df_sub['lat'],
            mode='markers',
            marker={'color': df_sub['Color'], 'size': 8},
            unselected={'marker': {'opacity': 1}},
            selected={'marker': {'opacity': 0.5, 'size': 15}},
            hoverinfo='text',
            hovertext=df_sub['Color']
    )]
    
    # Return figure
    return {
            'data': locations,
            'layout': go.Layout(
                    uirevision='foo',  # preserves state of figure/map after callback activated
                    clickmode='event+select',
                    hovermode='closest',
                    margin={"r": 0, "t": 0, "l": 0, "b": 0},
                    hoverdistance=2,
                    #            title=dict(text="Lift location",font=dict(size=25, color='green')),
                    mapbox=dict(
                            accesstoken=mapbox_access_token,
                            bearing=0,
                            style='light',
                            center=dict(
                                    lat=38.0608445,
                                    lon=-97.9297743
                            ),
                            pitch=40,
                            zoom=4
                    ),
            )
        
    }


@app.callback(
        Output('map2', 'figure'),
        [Input('Status_item', 'value')]
)
def update_figure(chosen_Status):
    df_sub = df[(df['Status'].isin(chosen_Status))
    ]
    
    # Create figure
    locations = [go.Scattermapbox(
            lon=df_sub['lon'],
            lat=df_sub['lat'],
            mode='markers',
            marker={'color': df_sub['Color'], 'size': 8},
            unselected={'marker': {'opacity': 1}},
            selected={'marker': {'opacity': 0.5, 'size': 15}},
            hoverinfo='text',
            hovertext=df_sub['Color']
    )]
    
    # Return figure
    return {
            'data': locations,
            'layout': go.Layout(
                    uirevision='foo',  # preserves state of figure/map after callback activated
                    clickmode='event+select',
                    hovermode='closest',
                    margin={"r": 0, "t": 0, "l": 0, "b": 0},
                    hoverdistance=2,
                    #            title=dict(text="Lift location",font=dict(size=25, color='green')),
                    mapbox=dict(
                            accesstoken=mapbox_access_token,
                            bearing=0,
                            style='light',
                            center=dict(
                                    lat=38.0608445,
                                    lon=-97.9297743
                            ),
                            pitch=40,
                            zoom=4
                    ),
            )
        
    }


if __name__== "__main__":
    app.run_server(debug=True, port=8001)
