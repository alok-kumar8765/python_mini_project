# This script uses the 'folium' library to create a simple interactive HTML map
# centered at a specific location, with a single marker placed on it.

import folium

# -----------------
# Create Map
# -----------------
# Initialize a Folium Map object.
# location=[28.61, 77.23] sets the initial center (New Delhi coordinates).
# zoom_start=5 sets the initial zoom level.
m = folium.Map(location=[28.61, 77.23], zoom_start=5)

# -----------------
# Add Marker
# -----------------
# Add a marker to the map at the same coordinates.
# The 'popup' argument sets the text that appears when the marker is clicked.
folium.Marker(
    [28.61, 77.23],
    popup="New Delhi"
).add_to(m)

# -----------------
# Save Map
# -----------------
# Save the generated map as an interactive HTML file named "map.html".
m.save("map.html")

# Display the map object (common in notebook environments to render inline).
m
