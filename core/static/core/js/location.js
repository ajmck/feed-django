// copied from https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API

// variable here, intended to be lost on refresh
var geoactive = false;

function geoFindMe() {

	if (!navigator.geolocation){
		geoactive = false;
		window.localStorage.setItem("location-success", "false")
		console.log("Geolocation is not supported by your browser");
		document.getElementById("form-location-button").className = "input-group-prepend btn btn-warning"

		return;
	}

	function success(position) {
		geoactive = true;
		window.localStorage.setItem("location-success", "true")
		var latitude  = position.coords.latitude;
		var longitude = position.coords.longitude;

		document.getElementById("form-lat").value = latitude
		document.getElementById("form-lon").value = longitude
		document.getElementById("form-location-button").className = "input-group-prepend btn btn-success"

		/*
		var landmarks = $.ajax({
			url:"/api/meshblocks/?format=json&dist=5000&point=" + longitude + ',' + latitude + "&limit=5",
			dataType: "json",
			success: console.log("Data loaded"), //yeet
			error: function (xhr) {
				console.log(xhr.statusText)

			}
    	});


		$.when(landmarks).done(function () {
			console.log(landmarks);
		});

*/

	}

	function error() {
		geoactive = false;
		console.log("Unable to retrieve your location");
		window.localStorage.setItem("location-success", "false")
		document.getElementById("form-location-button").className = "input-group-prepend btn btn-warning"
	}

	if (!geoactive) {
        navigator.geolocation.getCurrentPosition(success, error);
    } else {
		// hide panel, reset button to grey
	}

}


// load location automatically if the user did last time
// window.onload = function ()  {
// 	if (window.localStorage.getItem("location-success") === "true") geoFindMe();
// }

// alt - load location every time because you can't trust users
window.onload = geoFindMe();