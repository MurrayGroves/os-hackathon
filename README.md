# OS Map & Hack 2021
Our entry to OS Map & Hack 2021. Our goal was to identify the need for EV chargers and where they should be located.

Datasets used:
- [OS Places API](https://osdatahub.os.uk/docs/places/overview) to fetch a list of car parks
- [2011 Census](https://data.gov.uk/dataset/ca2daae8-8f36-4279-b15d-78b0463c61db/uk-gridded-population-2011-based-on-census-2011-and-land-cover-map-2015) for population data
- [National Chargepoint Registry](https://www.gov.uk/guidance/find-and-use-data-on-public-electric-vehicle-chargepoints) for current EV chargers and capacity.

## Method
- First, split the UK into 1 KM squares. These are essentially just British National Grid squares, but 1 kilometre in size, rather than 1 metre.
- Then we find the population for each of these squares from the Census data.
- From this we can estimate the charging capacity each square would require, assuming all ICE vehicles are replaced with EVs.
- We then subtract the current charging capacity from this projected demand.
- From this data we can attach a suitability value to each potential site, based on the demand of its square, proportional to its current capacity.
- We can then simply sort the list of potential sites by the suitability value.


## Visualisations
### Top 1000 potential charge point locations
![Top 1000 potential charge point locations](https://i.imgur.com/2q5Z1MN.png)
### Heatmap of charge capacity deficit
Warmer colours mean more charging capacity is needed  
![Heatmap of charge capacity deficit](https://i.imgur.com/NNXn5T8.png)  
![Zoomed heatmap of charge capacity deficit](https://i.imgur.com/8xqnzLy.png)  
