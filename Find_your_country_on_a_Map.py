import plotly.express as px
import pycountry

# Get user input for country name
country_name = input("Enter the country name: ")

# Safely convert the country name to ISO 3166-1 alpha-3 code
try:
    country = pycountry.countries.get(name=country_name)
    if not country:
        raise ValueError("Country not found. Please check the name and try again.")
    country_alpha_3 = country.alpha_3
except Exception as e:
    print(f"Error: {e}")
    exit()

# Data for the map
data = {
    'Country': [country_alpha_3],
    'Value': [100]
}

# Create the choropleth map
fig = px.choropleth(
    data,
    locations='Country',
    color='Value',
    color_continuous_scale='Inferno',
    title=f'Country Map Highlighting {country_name}'
)
fig.show()
