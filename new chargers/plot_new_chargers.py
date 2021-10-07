import pandas as pd
import plotly.express as px

df = pd.read_csv("../new chargers/data.csv")

fig = px.scatter_mapbox(df, lat='lat', lon='lon',
                        center=dict(lat=53, lon=-1), zoom=5,
                        mapbox_style="open-street-map")
fig.show()
