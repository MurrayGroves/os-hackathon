# convert.py
## Inputs
- List of squares with capacity deficit
## Outputs
- CSV of squares with lat/lon co-ords and capacity deficit
## Process
- Convert BSG to lat/lon and remove entries with excess capacity

# render.py
## Inputs
- CSV of squares with lat/lon co-ords and capacity deficit
## Outputs
- Interactable heatmap of capacity deficit across UK
## Process
Use plotly and mapbox to plot heatmap of each square's capacity deficit