# get_suitability.py
## Inputs
- List of car parks and their location as BNG co-ords
- 2D array of charging capacity of each square
- 2D array of charging capacity demand of each square
## Outputs
- List of car parks and their location, with suitability criteria
## Process
For each car park, find square's current capacity and capacity demand, and attach to car park data

# suitability.py
## Inputs
- List of car parks with suitability criteria
## Outputs
- List of car parks with suitability values
# Process
Calculate proportion of demand to current capacity, if no current capacity, massively boost suitability

# select_top.py
## Inputs
- List of car parks with suitability values
## Outputs
- List of car parks with suitability values
## Process
Sort list by suitability value and only keep top 1000