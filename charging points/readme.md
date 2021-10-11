# Converting existing charging points into a usable format
## Running
```bash
node index.js
```
thats it!
see [charging_grid.json](charging_grid.json) for the array output.

Array represents England in BNG (in 1k KM squares) where values are KW/h of the square.
```py
grid[x][y] = [kw]
```
