// Range Slider
function updateTextInput(val) {
          document.getElementById('textInput').value=val; 
        }

//location map
function initMap() {
        // The location of northwales
        const northwales = { lat: 53.081996, lng: -3.659492 };
        // The map, centered at northwales
        const map = new google.maps.Map(document.getElementById("map"), {
          zoom: 10,
          center: northwales,
        });
        // The marker, positioned at northwales
        const marker = new google.maps.Marker({
          position: northwales,
          map: map,
        });
      }

