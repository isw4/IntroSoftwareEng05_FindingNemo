// Default coordinates for the city of Eugene
var def_eugene = [44.0521, -123.0868, 14]

// Markers to place on the map
var here = L.AwesomeMarkers.icon({
    icon: 'user',
    prefix: 'glyphicon',
    markerColor: 'green'
})
var sushi = L.AwesomeMarkers.icon({
    icon: 'grain',
    prefix: 'glyphicon',
    markerColor: 'darkred'
})

// Event listener for successfully finding the user location
function onLocationFound(e) {
	console.log("user location found");
	mymap = mymap.setView(e.latlng, def_eugene[2]);
	geocodeService.reverse().latlng(e.latlng).run(function(error, result) {
    	L.marker(result.latlng, {icon: here}).addTo(mymap).bindPopup(result.address.Match_addr).openPopup()
    });
	//L.marker(e.latlng, {icon: here}).addTo(mymap);
}

// Event listener for failing to find user location
function onLocationError(e) {
	console.log("user location not found");
	mymap = mymap.setView([def_eugene[0], def_eugene[1]], def_eugene[2]);
}

// Initialise geocoding service
var geocodeService = L.esri.Geocoding.geocodeService();

// Initialise the map
var mymap = L.map('mapid').fitWorld();

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	maxZoom: 18,
	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
		'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
		'Imagery © <a href="http://mapbox.com">Mapbox</a>',
	id: 'mapbox.streets',
	accessToken: 'pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw'
}).addTo(mymap);

// Add event listeners
mymap.on('locationfound', onLocationFound)
mymap.on('locationerror', onLocationError)

// Finding user location
mymap.locate({maxZoom: def_eugene[2]})

// Geocoding restaurants
L.esri.Geocoding.geocode().text('3215 W 11th Ave, Eugene, OR, 97402').run(function(err, results, response){
  	console.log(results.results[0].text);
  	L.marker(results.results[0].latlng, {icon: sushi}).addTo(mymap).bindPopup("Sushi Island Japanese Restaurant");
});