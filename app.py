from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Helper function to reshape dataset
def reshape_data(df, value_name):
    df_melted = pd.melt(
        df,
        id_vars=["Province/State", "Country/Region", "Lat", "Long"],
        var_name="Date",
        value_name=value_name,
    )
    df_melted["Date"] = pd.to_datetime(df_melted["Date"], format="%m/%d/%y", errors="coerce")
    df_melted = df_melted.dropna(subset=["Date"])  # Remove rows with invalid dates
    return df_melted

# Load and reshape datasets
confirmed_cases = reshape_data(
    pd.read_csv(r"data\processed\cleaned_confirmed_cases.csv"),
    "Confirmed Cases",
)
deaths = reshape_data(
    pd.read_csv(r"C:\Users\sanga\Documents\COVID19_EDA_Project\data\processed\cleaned_deaths.csv"),
    "Deaths",
)
vaccinations = reshape_data(
    pd.read_csv(r"data\processed\cleaned_vaccinations.csv"),
    "Vaccinations",
)
recoveries = reshape_data(
    pd.read_csv(r"data\processed\cleaned_recovered.csv"),
    "Recoveries",
)

# Initialize Dash app with Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.title = "COVID-19 Dashboard"

# Default image URLs
default_image_url = "https://upload.wikimedia.org/wikipedia/commons/5/56/Coronavirus_artistic-illustration.jpg"
visualization_image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a0/COVID-19-vaccine.jpg"

# Title style
title_style = {
    "background": "linear-gradient(to right, #ff7e5f, #feb47b)",
    "color": "white",
    "textAlign": "center",
    "padding": "15px",
    "border-radius": "15px",
    "box-shadow": "0px 4px 10px rgba(0,0,0,0.2)",
}

# App layout
app.layout = html.Div(
    style={"background": "linear-gradient(to bottom, #e3f2fd, #ffffff)", "padding": "20px"},
    children=[
        # Banner Section
        dbc.Row(
            dbc.Col(
                html.Div(
                    [
                        html.Img(
                            src=default_image_url,
                            id="default-image",
                            style={"width": "100%", "border-radius": "10px", "margin-bottom": "20px"},
                        ),
                        html.Div(html.H1("COVID-19 Interactive Dashboard", style=title_style)),
                    ]
                )
            )
        ),
        # Introduction Section
        dbc.Row(
            dbc.Col(
                html.Div(
                    [
                        html.H3("Dashboard Overview", style={"margin-bottom": "10px", "color": "#2c3e50"}),
                        html.P(
                            """
                            This interactive dashboard provides real-time insights into the spread and impact 
                            of COVID-19 worldwide. It visualizes key metrics, including confirmed cases, recoveries, 
                            deaths, and vaccination progress for individual countries. Explore trends, compare data, 
                            and understand the impact of the pandemic across the globe.
                            """,
                            style={"text-align": "justify", "color": "#34495e"},
                        ),
                    ],
                    style={
                        "background": "white",
                        "padding": "15px",
                        "border-radius": "10px",
                        "box-shadow": "0px 4px 10px rgba(0,0,0,0.1)",
                        "margin-bottom": "20px",
                    },
                )
            )
        ),
        # Country Dropdown Section
        dbc.Row(
            dbc.Col(
                html.Div(
                    [
                        html.Label("Select a Country:", style={"font-weight": "bold", "color": "#2c3e50"}),
                        dcc.Dropdown(
                            id="country-dropdown",
                            options=[
                                {"label": country, "value": country}
                                for country in confirmed_cases["Country/Region"].unique()
                            ],
                            placeholder="Search for a country",
                            style={"margin-bottom": "20px"},
                        ),
                    ],
                    style={
                        "background": "white",
                        "padding": "15px",
                        "border-radius": "10px",
                        "box-shadow": "0px 4px 10px rgba(0,0,0,0.1)",
                    },
                )
            )
        ),
        # Summary Table and Visualizations Section
        dbc.Row(
            id="summary-and-visualizations-section",
            children=[
                html.Div(
                    "Select a country from the dropdown above to view visualizations.",
                    style={
                        "text-align": "center",
                        "color": "#7f8c8d",
                        "padding": "20px",
                        "font-size": "18px",
                    },
                )
            ],
        ),
    ],
)

# Callbacks for dynamic updates
@app.callback(
    [
        Output("summary-and-visualizations-section", "children"),
        Output("default-image", "src"),
    ],
    [Input("country-dropdown", "value")],
)
def update_visualizations(selected_country):
    if not selected_country:
        # No country selected: show default message
        return [
            html.Div(
                "Select a country from the dropdown above to view visualizations.",
                style={
                    "text-align": "center",
                    "color": "#7f8c8d",
                    "padding": "20px",
                    "font-size": "18px",
                },
            ),
            default_image_url,
        ]

    # Filter data for the selected country
    cases_country = confirmed_cases[confirmed_cases["Country/Region"] == selected_country]
    deaths_country = deaths[deaths["Country/Region"] == selected_country]
    vacc_country = vaccinations[vaccinations["Country/Region"] == selected_country]
    recoveries_country = recoveries[recoveries["Country/Region"] == selected_country]

    # Calculate Totals
    total_cases = cases_country["Confirmed Cases"].sum()
    total_deaths = deaths_country["Deaths"].sum()
    total_vaccinations = vacc_country["Vaccinations"].sum()
    total_recoveries = recoveries_country["Recoveries"].sum()

    # Summary Table
    summary_table = dbc.Table(
        [
            html.Thead(html.Tr([html.Th("Metric"), html.Th("Value")])),
            html.Tbody(
                [
                    html.Tr([html.Td("Total Cases"), html.Td(f"{total_cases:,}")]),
                    html.Tr([html.Td("Total Recoveries"), html.Td(f"{total_recoveries:,}")]),
                    html.Tr([html.Td("Total Deaths"), html.Td(f"{total_deaths:,}")]),
                    html.Tr([html.Td("Total Vaccinations"), html.Td(f"{total_vaccinations:,}")]),
                ]
            ),
        ],
        bordered=True,
        striped=True,
        hover=True,
        responsive=True,
        style={"margin-bottom": "20px"},
    )

    # Daily Cases Plot
    daily_cases_fig = px.line(
        cases_country,
        x="Date",
        y="Confirmed Cases",
        title=f"Daily Confirmed Cases in {selected_country}",
        template="plotly_white",
    )

    # Daily Deaths Plot
    daily_deaths_fig = px.line(
        deaths_country,
        x="Date",
        y="Deaths",
        title=f"Daily Deaths in {selected_country}",
        template="plotly_white",
    )

    # Vaccination Progress Plot
    vaccination_fig = px.line(
        vacc_country,
        x="Date",
        y="Vaccinations",
        title=f"Vaccination Progress in {selected_country}",
        template="plotly_white",
    )

    # Recovery Progress Plot
    recovery_fig = px.line(
        recoveries_country,
        x="Date",
        y="Recoveries",
        title=f"Recovery Progress in {selected_country}",
        template="plotly_white",
    )

    # Pie Chart for Proportions
    pie_fig = px.pie(
        names=["Total Cases", "Total Recoveries", "Total Deaths", "Total Vaccinations"],
        values=[total_cases, total_recoveries, total_deaths, total_vaccinations],
        title="Proportion of Cases, Recoveries, Deaths, and Vaccinations",
    )

    # Visualizations Layout
    visualizations = dbc.Row(
        [
            dbc.Col(dcc.Graph(figure=daily_cases_fig), md=6),
            dbc.Col(dcc.Graph(figure=daily_deaths_fig), md=6),
            dbc.Col(dcc.Graph(figure=vaccination_fig), md=6),
            dbc.Col(dcc.Graph(figure=recovery_fig), md=6),
            dbc.Col(dcc.Graph(figure=pie_fig), md=6),
        ]
    )

    return [summary_table, visualizations], visualization_image_url


# Run the app
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)

