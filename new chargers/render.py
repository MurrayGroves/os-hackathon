import pandas as pd
import plotly.express as px

df = pd.read_csv("../new chargers/heatmap_data.csv")

fig = px.density_mapbox(df, lat='lat', lon='lon', z='kw2', radius=10,
                        center=dict(lat=53, lon=-1), zoom=5,
                        mapbox_style="open-street-map")
fig.show()
