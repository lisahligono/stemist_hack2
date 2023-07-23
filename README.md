# ABOUT THE CHALLENGE 

This repository is a part of our team's 'InfernoTech' submission for the STEMist Hacks II hackathon. 

<h2>Study area</h2>

<h2>Problem</h2>
On July 17, 2023, wildfires hit the Greece town of Attica due to a heatwave that has been experienced in Southern Europe.

<h2>Methodology</h2>
In this section we describe how we utilized python libraries and packages to obtain our solution:

<b>SAMGEO</b>

Segment-Geospatial (samgeo) is an open-source Python package designed to simplify the process of segmenting geospatial data with the Segment Anything Model [@Kirillov2023]. The package leverages popular Python libraries, such as leafmap [@Wu2021], ipywidgets [@Grout2021], rasterio [@Gillies2013], geopandas [@Jordahl2021], and segment-anything-py [@Wu2023], to provide a straightforward interface for users to segment remote sensing imagery and export the results in various formats, including vector and raster data.

https://github.com/opengeos/segment-geospatial/blob/main/paper/paper.md

<b>FLASK</b>

We used flask to design a web application for our project. 
Flask is a lightweight web server gateway interface (WSGI) for web application development using python. 
Importing and Setting Up: The Flask application starts by importing the Flask class from the flaskmodule. It then creates a Flask app instance using Flask(__name__). The __name__ parameter is a special Python variable that represents the name of the current module, and it is used by Flask to locate resources such as templates and static files.
Routing and View Function: Flask uses routing to map URLs to view functions. In this application, the root URL ('/') is associated with the base() function. When a user accesses the root URL, the base()function is called, and it generates the interactive map.
Map Rendering and HTML Generation: Inside the base() function, the interactive map is created using Folium. The map is generated with a specified location and zoom level. The GeoJSON data from the shapefile is then added to the map using the folium.GeoJson() method, with a custom style function for coloring the features based on their categories.
Layer Control Integration: To enable users to toggle the visibility of different shapefile layers on the map, a LayerControl is added using folium.LayerControl(). This allows users to interactively switch between different layers of the map.
Running the Flask App: Finally, the Flask app is run using app.run(debug=True). The debug=Trueparameter enables Flask's debug mode, which provides helpful error messages and auto-reloading of the server when code changes are detected. The server starts listening for incoming requests, and when a user accesses the root URL, Flask serves the HTML content of the map to the user's web browser.

<b>FOLIUM</b>

Folium is a powerful Python library used for creating interactive maps and visualizations. It is built on top of Leaflet.js, a widely-used JavaScript library for interactive maps. Folium allows you to create dynamic maps with various data overlays and custom styling, making it a popular choice for data visualization, geospatial analysis, and web mapping applications.
Here's a description of the Folium library as used in the Flask application:
Importing and Setting Up: The Flask application starts by importing the required modules: Flask, folium, and geopandas. The Flask app is created using Flask(__name__), and the base() function is defined as the route handler for the root URL.
Map Initialization: Inside the base() function, a folium map is initialized using folium.Map(). The map is centered at latitude 37.782953 and longitude 23.942564and is set to an initial zoom level of 13.
Custom Style Function: A custom style function is defined to control how the shapefile features are styled on the map. This function uses the style_function parameter of folium.GeoJson() to dynamically set the colors and styles of the shapefile features based on their categories.
Reading and Adding Shapefile Layers: The application reads the shapefile data using geopandas and converts it to GeoJSON format using to_json(). Then, the GeoJSON data is added to the folium map using folium.GeoJson(). The custom style function is applied to each shapefile layer using the style_function parameter, resulting in the shapefile features being colored based on their categories.
Layer Control: A LayerControl is added to the map using folium.LayerControl(). This control allows users to toggle the visibility of different layers, making it easier to view and compare multiple layers on the same map.
Running the Flask App: Finally, the Flask app is run in debug mode using app.run(debug=True), allowing the server to listen for incoming requests and serve the map when the root URL is accessed.

<h2>Solution</h2>
