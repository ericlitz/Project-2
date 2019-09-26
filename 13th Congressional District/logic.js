// Creating map object
const map = L.map("map", {
    //lat and lon for Springfield, IL
    center: [39.5298504,-89.3480005],
    zoom: 11
  });
  
  // Adding tile layer
  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: attribution,
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
  }).addTo(map);
  
  const link = "13th Congressional District.geojson";
  
  // Grabbing our GeoJSON data..
  d3.json(link).then(function(data) {
    // Creating a GeoJSON layer with the retrieved data
    L.geoJson(data).addTo(map);
  }).catch(function(error) {
    console.log(error);
  });

  //Create Function to determine Color of each district here
  //function chooseColor(district) {
  // switch (district) {
  
    //case "":
    //  return "yellow";
   
    //}
  //}
  

  d3.json(link).then(function(data) {
    console.log(data);
    // Creating a geoJSON layer with the retrieved data
    L.geoJson(data, {
      // Style each feature 
      style: function(feature) {
        return {
          color: "white",
          // Call the chooseColor function to decide which color to color our precinct
          fillColor: chooseColor(feature.properties),
          fillOpacity: 0.5,
          weight: 1.5
        };
      },
      // Called on each feature
      onEachFeature: function(feature, layer) {
        // Set mouse events to change map styling
        layer.on({
          // When a user's mouse touches a map feature, the mouseover event calls this function, that feature's opacity changes to 90% so that it stands out
          mouseover: function(event) {
            layer = event.target;
            layer.setStyle({
              fillOpacity: 0.9
            });
          },
          // When the cursor no longer hovers over a map feature - when the mouseout event occurs - the feature's opacity reverts back to 50%
          mouseout: function(event) {
            layer = event.target;
            layer.setStyle({
              fillOpacity: 0.5
            });
          },
          // When a feature (precinct) is clicked, it is enlarged to fit the screen
          click: function(event) {
            map.fitBounds(event.target.getBounds());
          }
        });
        // Giving each feature a pop-up with information pertinent to it
        layer.bindPopup("<h1>" + feature.properties.Name + "</h1> <hr> <h2>" + feature.properties + "</h2>");
  
      }
    }).addTo(map);
  }).catch(function(error) {
    console.log(error);
  });
  
  


