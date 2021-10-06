var os = require("./os-transform.js")
var chargers = require("./chargers.json")
var fs = require('fs');
var grid = []

function output_grid() {
  // iterate through the list of chargers and convert this to our format
  chargers["ChargeDevice"].forEach((c) => {
    // just to simplify
    const loc = c["ChargeDeviceLocation"]
    var kw = 0
    // Add up KW for all connectors at the charging point
    c["Connector"].forEach((cn) => {
      kw += parseFloat(cn["RatedOutputkW"])
    })
    // convert long/lat to BNG
    let transform = os.Transform.fromLatLng({ lat: parseFloat(loc["Latitude"]), lng: parseFloat(loc["Longitude"]) })
    // add the converted charging point to the list
    grid.push({ 
      x: Math.floor(transform.ea / 1000), 
      y: Math.floor(transform.no / 1000), 
      kw: Math.round(kw * 10) / 10
    })
  })
  // write output
  fs.writeFile('charging_grid.json', JSON.stringify(grid), 'utf8', () => { console.log("Written to [charging_grid.json]") });
}
output_grid()
