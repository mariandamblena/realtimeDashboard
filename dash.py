import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

# Sample data
import numpy as np
x = np.linspace(0, 10, 100)
volume_dispensed = np.random.normal(5, 1, 100)
volume_setpoint = np.full(100, 5)

temperature_sensor_1 = np.random.normal(25, 2, 100)
temperature_sensor_2 = np.random.normal(26, 2, 100)
temperature_sensor_3 = np.random.normal(24, 2, 100)

co2 = np.random.normal(400, 50, 100)
o2 = np.random.normal(21, 1, 100)
humidity = np.random.normal(50, 10, 100)

# Initialize app with dark theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = dbc.Container(
    [
        html.H1("Pump and Environmental Sensor Dashboard", className="text-center text-light"),
        dcc.Graph(id='volume-graph'),
        dcc.Graph(id='temperature-graph'),
        dcc.Graph(id='co2-graph'),
        dcc.Graph(id='o2-graph'),
        dcc.Graph(id='humidity-graph'),
        dcc.Graph(id='env-sensors-graph'),
        dcc.Graph(id='all-pumps-graph'),
    ]
)

# Callbacks to update graphs
@app.callback(
    Output('volume-graph', 'figure'),
    Input('volume-graph', 'id')
)
def update_volume_graph(_):
    return {
        'data': [
            go.Scatter(x=x, y=volume_dispensed, mode='lines', name='Volume Dispensed'),
            go.Scatter(x=x, y=volume_setpoint, mode='lines', name='Volume Setpoint'),
        ],
        'layout': go.Layout(
            title='Volume Dispensed vs Setpoint',
            xaxis={'title': 'Time'},
            yaxis={'title': 'Volume (ml)'},
            template='plotly_dark'
        )
    }

@app.callback(
    Output('temperature-graph', 'figure'),
    Input('temperature-graph', 'id')
)
def update_temperature_graph(_):
    return {
        'data': [
            go.Scatter(x=x, y=temperature_sensor_1, mode='lines', name='Temperature Sensor 1'),
            go.Scatter(x=x, y=temperature_sensor_2, mode='lines', name='Temperature Sensor 2'),
            go.Scatter(x=x, y=temperature_sensor_3, mode='lines', name='Temperature Sensor 3'),
        ],
        'layout': go.Layout(
            title='Temperature Sensors',
            xaxis={'title': 'Time'},
            yaxis={'title': 'Temperature (°C)'},
            template='plotly_dark'
        )
    }

@app.callback(
    Output('co2-graph', 'figure'),
    Input('co2-graph', 'id')
)
def update_co2_graph(_):
    return {
        'data': [
            go.Scatter(x=x, y=co2, mode='lines', name='CO2'),
        ],
        'layout': go.Layout(
            title='CO2 Levels',
            xaxis={'title': 'Time'},
            yaxis={'title': 'CO2 (ppm)'},
            template='plotly_dark'
        )
    }

@app.callback(
    Output('o2-graph', 'figure'),
    Input('o2-graph', 'id')
)
def update_o2_graph(_):
    return {
        'data': [
            go.Scatter(x=x, y=o2, mode='lines', name='O2'),
        ],
        'layout': go.Layout(
            title='Oxygen Levels',
            xaxis={'title': 'Time'},
            yaxis={'title': 'Oxygen (%)'},
            template='plotly_dark'
        )
    }

@app.callback(
    Output('humidity-graph', 'figure'),
    Input('humidity-graph', 'id')
)
def update_humidity_graph(_):
    return {
        'data': [
            go.Scatter(x=x, y=humidity, mode='lines', name='Humidity'),
        ],
        'layout': go.Layout(
            title='Humidity Levels',
            xaxis={'title': 'Time'},
            yaxis={'title': 'Humidity (%)'},
            template='plotly_dark'
        )
    }

@app.callback(
    Output('env-sensors-graph', 'figure'),
    Input('env-sensors-graph', 'id')
)
def update_env_sensors_graph(_):
    return {
        'data': [
            go.Scatter(x=x, y=temperature_sensor_1, mode='lines', name='Temperature Sensor 1'),
            go.Scatter(x=x, y=co2, mode='lines', name='CO2'),
            go.Scatter(x=x, y=o2, mode='lines', name='Oxygen'),
            go.Scatter(x=x, y=humidity, mode='lines', name='Humidity'),
        ],
        'layout': go.Layout(
            title='Environmental Sensors',
            xaxis={'title': 'Time'},
            yaxis={'title': 'Values'},
            template='plotly_dark'
        )
    }

@app.callback(
    Output('all-pumps-graph', 'figure'),
    Input('all-pumps-graph', 'id')
)
def update_all_pumps_graph(_):
    return {
        'data': [
            go.Scatter(x=x, y=volume_dispensed, mode='lines', name='Pump 1 Volume Dispensed'),
            # Add more pumps here if needed
        ],
        'layout': go.Layout(
            title='All Pumps',
            xaxis={'title': 'Time'},
            yaxis={'title': 'Volume (ml)'},
            template='plotly_dark'
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)
