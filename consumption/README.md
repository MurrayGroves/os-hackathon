## Inputs
List of dicts of population data for each square
## Outputs
List of dicts of charging capacity requirements for each square
## Process
For each square, multiply the population value by a constant determined by `cars per person * EV consumption per mile * average car mileage`, also replace null values (-9999) with 0