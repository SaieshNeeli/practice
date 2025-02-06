import streamlit as st
import folium
from folium.plugins import MarkerCluster
from geopy.distance import geodesic

# Function to calculate the path on Google Maps
def create_map(start_lat, start_lon, end_lat, end_lon):
    # Create a Map centered at the midpoint between the start and end points
    map_center = [(start_lat + end_lat) / 2, (start_lon + end_lon) / 2]
    m = folium.Map(location=map_center, zoom_start=12)
    
    # Adding start and end markers
    folium.Marker([start_lat, start_lon], popup="Start", icon=folium.Icon(color='green')).add_to(m)
    folium.Marker([end_lat, end_lon], popup="End", icon=folium.Icon(color='red')).add_to(m)

    # Draw a line between the two points
    folium.PolyLine([(start_lat, start_lon), (end_lat, end_lon)], color='blue', weight=2.5, opacity=1).add_to(m)

    # Add a MarkerCluster to display multiple points (optional)
    marker_cluster = MarkerCluster().add_to(m)
    folium.Marker([start_lat, start_lon], popup="Start", icon=folium.Icon(color='green')).add_to(marker_cluster)
    folium.Marker([end_lat, end_lon], popup="End", icon=folium.Icon(color='red')).add_to(marker_cluster)

    return m

# Streamlit user interface
st.title("Google Maps Path Visualization")
st.write("Enter the latitude and longitude for two points to see the path on the map.")

# User inputs for start and end coordinates
start_lat = st.number_input("Start Latitude", value=40.7128, format="%.4f")
start_lon = st.number_input("Start Longitude", value=-74.0060, format="%.4f")
end_lat = st.number_input("End Latitude", value=34.0522, format="%.4f")
end_lon = st.number_input("End Longitude", value=-118.2437, format="%.4f")

# Display the map with a path between the two points
map_obj = create_map(start_lat, start_lon, end_lat, end_lon)

# Render map on Streamlit
st.markdown("### Path on Google Maps:")
folium_static(map_obj)

# Calculate and display the distance
distance = geodesic((start_lat, start_lon), (end_lat, end_lon)).km
st.write(f"Distance between points: {distance:.2f} km")
