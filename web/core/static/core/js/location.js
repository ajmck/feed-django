// copied from https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API
window.onload  = function geoFindMe() {

	if (!navigator.geolocation){
		console.log("Geolocation is not supported by your browser");
		return;
	}

	function success(position) {
		var latitude  = position.coords.latitude;
		var longitude = position.coords.longitude;

		document.getElementById("form-lat").value = latitude
		document.getElementById("form-lon").value = longitude

	}

	function error() {
		console.log("Unable to retrieve your location");
	}
	
	navigator.geolocation.getCurrentPosition(success, error);
}
