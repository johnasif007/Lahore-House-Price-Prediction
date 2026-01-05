// 1. Function to get the selected BHK value from the radio buttons
function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for(var i in uiBHK) {
    if(uiBHK[i].checked) {
        return parseInt(i) + 1; // Returns 1, 2, 3, etc.
    }
  }
  return -1; // Default/Invalid
}

// 2. Function to get the selected Bathroom value from the radio buttons
function getBathValue() {
  var uiBath = document.getElementsByName("uiBath");
  for(var i in uiBath) {
    if(uiBath[i].checked) {
        return parseInt(i) + 1;
    }
  }
  return -1;
}

// 3. MAIN FUNCTION: Sends data to Flask and displays the price
function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var marla = document.getElementById("uiMarla");
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");

  // URL of your Python Flask Server
// CHANGED THIS:
// var url = "http://127.0.0.1:5000/predict_home_price"; 

// TO THIS:
var url = "/predict_home_price";
  // Use jQuery POST to send data to the backend
  $.post(url, {
      total_sqft: parseFloat(marla.value), // Sending Marla count as the 'Area'
      bhk: bhk,
      bath: bathrooms,
      location: location.value
  }, function(data, status) {
      console.log("Prediction received: ", data.estimated_price);

      // Formatting the output (e.g., 28,000,000 PKR)
      // Since your model was trained on PKR values
      var formattedPrice = data.estimated_price.toLocaleString('en-PK');
      estPrice.innerHTML = "<h2>" + formattedPrice + " PKR</h2>";
      console.log("Status: " + status);
  });
}

// 4. ON PAGE LOAD: Automatically populates the location dropdown
function onPageLoad() {
  console.log("Document loaded, fetching locations...");
// CHANGED THIS:
// var url = "http://127.0.0.1:5000/get_location_names"; 

// TO THIS:
var url = "/get_location_names";
  
  $.get(url, function(data, status) {
      console.log("Got response for get_location_names");
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty(); // Clear default text

          for(var i in locations) {
              // Create an option for each location in your 93 columns
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
}

// Call onPageLoad when the browser window opens

window.onload = onPageLoad;
