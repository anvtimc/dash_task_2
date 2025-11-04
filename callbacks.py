from utils.data_loader import load_data
import plotly.graph_objects as go
import plotly.io as pio
from dash import Input, Output, html
import assets.design as ds


pio.templates['custom'] = pio.templates['plotly'].update(
    layout=dict(colorway=ds.MY_PALETTE)
)

pio.templates.default = 'custom'


def register_callbacks(app):

    @app.callback(
        Output('city-card', 'children'),
        Output('co-graph', 'figure'),
        Output('no2-graph', 'figure'),
        Output('o3-graph', 'figure'),
        Output('so2-graph', 'figure'),
        Output('pm25-graph', 'figure'),
        Output('pm10-graph', 'figure'),
        Input('city-filter', 'value'),
        Input('time-filter', 'value'),
        Input('days-filter', 'value')
    )
    def update_dashboard(city, time_range, days):
        data = load_data(city, days, time_range)

        co_fig = go.Figure(
            data=[go.Bar(x=data['days_labels'], y=data['co_avg'])],
        )
        co_fig.update_layout(
            title="Содержание CO в воздухе",
            title_font_size=ds.GRAPH_TITLE_FONT_SIZE,
            title_x=ds.GRAPH_TITLE_ALIGN,
            title_font_weight=ds.GRAPH_FONT_WEIGHT,
            xaxis_title='День прогноза',
            yaxis_title='Индекс по CO',
            font=dict(family=ds.GRAPH_FONT_FAMILY),
            xaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, tickfont=dict(size=ds.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, tickfont=dict(size=ds.GRAPH_FONT_SIZE)),
            plot_bgcolor=ds.PLOT_BACKGROUND_COLOR,
            paper_bgcolor=ds.PAPER_BACKGROUND_COLOR,
        )

        no2_fig = go.Figure(
            data=[go.Bar(x=data['days_labels'], y=data['no2_avg'])],
        )
        no2_fig.update_layout(
            title="Содержание NO₂ в воздухе",
            title_font_size=ds.GRAPH_TITLE_FONT_SIZE,
            title_x=ds.GRAPH_TITLE_ALIGN,
            title_font_weight=ds.GRAPH_FONT_WEIGHT,
            xaxis_title='День прогноза',
            yaxis_title='Индекс по NO₂',
            font=dict(family=ds.GRAPH_FONT_FAMILY),
            xaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, tickfont=dict(size=ds.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, tickfont=dict(size=ds.GRAPH_FONT_SIZE)),
            plot_bgcolor=ds.PLOT_BACKGROUND_COLOR,
            paper_bgcolor=ds.PAPER_BACKGROUND_COLOR,
        )

        o3_fig = go.Figure(
            data=[go.Bar(x=data['days_labels'], y=data['o3_avg'])],
        )
        o3_fig.update_layout(
            title="Содержание O₃ в воздухе",
            title_font_size=ds.GRAPH_TITLE_FONT_SIZE,
            title_x=ds.GRAPH_TITLE_ALIGN,
            title_font_weight=ds.GRAPH_FONT_WEIGHT,
            xaxis_title='День прогноза',
            yaxis_title='Индекс по O₃',
            font=dict(family=ds.GRAPH_FONT_FAMILY),
            xaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, tickfont=dict(size=ds.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, tickfont=dict(size=ds.GRAPH_FONT_SIZE)),
            plot_bgcolor=ds.PLOT_BACKGROUND_COLOR,
            paper_bgcolor=ds.PAPER_BACKGROUND_COLOR,
        )

        so2_fig = go.Figure(
            data=[go.Bar(x=data['days_labels'], y=data['so2_avg'])],
        )
        so2_fig.update_layout(
            title="Содержание SO₂ в воздухе",
            title_font_size=ds.GRAPH_TITLE_FONT_SIZE,
            title_x=ds.GRAPH_TITLE_ALIGN,
            title_font_weight=ds.GRAPH_FONT_WEIGHT,
            xaxis_title='День прогноза',
            yaxis_title='Индекс по SO₂',
            font=dict(family=ds.GRAPH_FONT_FAMILY),
            xaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, tickfont=dict(size=ds.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, tickfont=dict(size=ds.GRAPH_FONT_SIZE)),
            plot_bgcolor=ds.PLOT_BACKGROUND_COLOR,
            paper_bgcolor=ds.PAPER_BACKGROUND_COLOR,
        )

        pm25_fig = go.Figure(
            data=[go.Bar(x=data['days_labels'], y=data['pm25_avg'])],
        )
        pm25_fig.update_layout(
            title="Содержание частиц размером <2.5 мкм",
            title_font_size=ds.GRAPH_TITLE_FONT_SIZE,
            title_x=ds.GRAPH_TITLE_ALIGN,
            title_font_weight=ds.GRAPH_FONT_WEIGHT,
            xaxis_title='День прогноза',
            yaxis_title='Индекс по частицам',
            font=dict(family=ds.GRAPH_FONT_FAMILY),
            xaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, tickfont=dict(size=ds.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, tickfont=dict(size=ds.GRAPH_FONT_SIZE)),
            plot_bgcolor=ds.PLOT_BACKGROUND_COLOR,
            paper_bgcolor=ds.PAPER_BACKGROUND_COLOR,
        )

        pm10_fig = go.Figure(
            data=[go.Bar(x=data['days_labels'], y=data['pm10_avg'])],
        )
        pm10_fig.update_layout(
            title="Содержание частиц размером <10 мкм",
            title_font_size=ds.GRAPH_TITLE_FONT_SIZE,
            title_x=ds.GRAPH_TITLE_ALIGN,
            title_font_weight=ds.GRAPH_FONT_WEIGHT,
            xaxis_title='День прогноза',
            yaxis_title='Индекс по частицам',
            font=dict(family=ds.GRAPH_FONT_FAMILY),
            xaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, tickfont=dict(size=ds.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=ds.GRAPH_FONT_SIZE, tickfont=dict(size=ds.GRAPH_FONT_SIZE)),
            plot_bgcolor=ds.PLOT_BACKGROUND_COLOR,
            paper_bgcolor=ds.PAPER_BACKGROUND_COLOR,
        )

        city_card = html.Div([
            html.H4("Текущие показатели"),
            html.P(f"Город: {data['city_name']}"),
            html.P(f"Температура: {data['temp']} °C"),
            html.P(f"{data['last_updated']}"),
            html.P(f"{data['condition']}"),
            html.Img(src=f"https:{data['icon']}")
            ])

        return city_card, co_fig, no2_fig, o3_fig, so2_fig, pm25_fig, pm10_fig
