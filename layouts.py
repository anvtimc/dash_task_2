import dash_bootstrap_components as dbc
from dash import dcc, html


def create_layout():
    return dbc.Container([
        # Хедер
        html.Div([
            html.H1("Качество воздуха 🏗️🏙️", className="main-header"),
            html.H2("Мониторинг загрязнения воздуха в городах", className="main-subheader"),
        ], className="header"),

        # Фильтры
        dbc.Row([
            dbc.Col([
                html.Label("Город", className="filter-label"),
                dcc.Dropdown(
                    id="city-filter",
                    options=[
                        {'label': 'Лондон', 'value': 'London'},
                        {'label': 'Москва', 'value': 'Moscow'},
                        {'label': 'Токио', 'value': 'Tokyo'}
                    ],
                    value='Moscow',
                    className='filter-dropdown'
                )
            ], md=4),

            dbc.Col([
                html.Label("Час (0:00–23:00)", className="filter-label"),
                dcc.Dropdown(
                    id="time-filter",
                    options=[{'label': f'{h:02d}:00', 'value': h} for h in range(0, 24)],
                    value=3,
                    className='filter-dropdown'
                )
            ], md=4),

            dbc.Col([
                html.Label("Количество дней прогноза", className="filter-label"),
                dcc.Dropdown(
                    id="days-filter",
                    options=[{'label': f'{i} дней', 'value': i} for i in range(1, 5)],
                    value=3,
                    className='filter-dropdown'
                )
            ], md=4)
        ], className="filters-row"),

        # Карточка города
        dbc.Row([
            dbc.Col([
                dbc.Card(id='city-card', body=True, className="city-info-card"),
            ], md=12)
        ], className="mb-3"),

        # Графики
        dbc.Row([
            dbc.Col(dcc.Graph(id='co-graph'), width=6, md=4, xs=12),
            dbc.Col(dcc.Graph(id='no2-graph'), width=6, md=4, xs=12),
            dbc.Col(dcc.Graph(id='o3-graph'), width=6, md=4, xs=12),
        ], className="mb-3"),

        dbc.Row([
            dbc.Col(dcc.Graph(id='so2-graph'), width=6, md=4, xs=12),
            dbc.Col(dcc.Graph(id='pm25-graph'), width=6, md=4, xs=12),
            dbc.Col(dcc.Graph(id='pm10-graph'), width=6, md=4, xs=12),
        ], className="mb-3"),

    ], fluid=True)


