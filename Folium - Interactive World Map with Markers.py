# This script uses the 'folium' library to create an interactive world map
# and place markers on multiple major cities.

import folium
from IPython.display import display

# -----------------
# Setup
# -----------------
# Initialize a Folium Map object.
# location=[20,0] sets the initial center near the world center.
# zoom_start=2 sets a low zoom level to show the entire world.
map_world = folium.Map(location=[20,0], zoom_start=2)

# Define a dictionary of cities with their corresponding latitude and longitude coordinates.
cities = {
    "New York":[40.7128,-74.0060],
    "Tokyo":[35.6895,139.6917],
    "Delhi":[28.6139,77.2090]
}

# -----------------
# Add Markers
# -----------------
# Iterate through the dictionary of cities.
for city, coords in cities.items():
    # Create a marker for each city.
    # location=coords sets the position.
    # popup=city sets the text displayed when the marker is clicked.
    folium.Marker(location=coords, popup=city).add_to(map_world)

# -----------------
# Display Map
# -----------------
# Display the generated map object in the output (common in notebook environments).
display(map_world)
