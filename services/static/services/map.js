console.log("Map");

var map = L.map('map').setView([0, 0], 2); // Set the initial center and zoom

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

var originSelect = document.getElementById("departure").innerText.trim();
var destinationSelect = document.getElementById("destination").innerText.trim();

console.log(originSelect, destinationSelect);

// Call drawConnection function immediately after initializing variables
drawConnection();

function drawConnection() {
    var originCity = originSelect;
    var destinationCity = destinationSelect;

    console.log("value:", originCity);

    // Function to get coordinates from OpenCage Geocoding API
    function getCoordinates(city, callback) {
        var apiUrl = 'https://api.opencagedata.com/geocode/v1/json?q=' + encodeURIComponent(city) + '&key=79ce7d6e97184926b002b8d88f0238ce';
        console.log(encodeURIComponent(city));

        // Make a GET request to the OpenCage Geocoding API
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                if (data.results && data.results.length > 0) {
                    var coordinates = data.results[0].geometry;
                    callback(coordinates.lat, coordinates.lng);
                } else {
                    console.error('Could not get coordinates for ' + city);
                }
            })
            .catch(error => {
                console.error('Error fetching coordinates:', error);
            });
    }

    // Get coordinates for the origin city
    getCoordinates(originCity, function(originLat, originLng) {
        // Get coordinates for the destination city
        getCoordinates(destinationCity, function(destLat, destLng) {
            var originCoords = L.latLng(originLat, originLng);
            var destinationCoords = L.latLng(destLat, destLng);

            // Remove previous layers
            map.eachLayer(function(layer) {
                if (layer instanceof L.Polyline) {
                    map.removeLayer(layer);
                }
            });

            // Create a polyline to connect the two cities
            var polyline = L.polyline([originCoords, destinationCoords], {
                color: 'red'
            }).addTo(map);

            // Fit the map to the polyline
            map.fitBounds(polyline.getBounds());
        });
    });
}
