// copied from https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API
function geoFindMe() {

	if (!navigator.geolocation){
		console.log("Geolocation is not supported by your browser");
		document.getElementById("form-location-button").className = "input-group-prepend btn btn-warning"

		return;
	}

	function success(position) {
		var latitude  = position.coords.latitude;
		var longitude = position.coords.longitude;

		document.getElementById("form-lat").value = latitude
		document.getElementById("form-lon").value = longitude
		document.getElementById("form-location-button").className = "input-group-prepend btn btn-success"
	}

	function error() {
		console.log("Unable to retrieve your location");
		document.getElementById("form-location-button").className = "input-group-prepend btn btn-warning"
	}

	navigator.geolocation.getCurrentPosition(success, error);
}

window.onload = geoFindMe()