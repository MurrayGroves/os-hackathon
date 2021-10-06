# Converting existing charging points into a usable format
## Running
```bash
node index.js
```
thats it!
see [charging_grid.json](charging_grid.json) for the JSON output
## Format
```json
{
  "x": [int],
  "y": [int],
  "kw": [float]
}
```
## Example
This is for the charging point at 51.431454N, 0.031175W
```json
{
  "x": 541,
  "y": 172,
  "kw": 10.7
}
```
