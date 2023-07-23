# ABOUT THE CHALLENGE 

This repository is a part of our team's 'InfernoTech' submission for the STEMist Hacks II hackathon. 

<h2>Study area</h2>

<h2>Problem</h2>
On July 17, 2023, wildfires hit the Greece town of Attica due to a heatwave that has been experienced in Southern Europe.

<h2>Methodology</h2>

<h2>Step 1: Modelling</h2>

The objective is to train the model for detecting the burning area in Attica, Greece during June 26 to July 14, 2023. With the result of the model, we can estimate the damage in the area and provide the information for the future fire event. To achieve this objective, we utilised satellite images and open source models to detect the burnt area using the models as follows:

<b>FireCLR</b>

<img width="452" alt="s1" src="https://github.com/lisahligono/stemist_hack2/assets/72496335/68304541-3341-4384-a746-c6abc6603848">


The model is implemented from the research model (Zhang, 2022). We use the trained FireCLR model that is based on their data to extract the features from satellite images. Next step is to compute the difference between pre-fire and post-fire images, we subtract the features of these images to get the significant change of the area. Lastly, the calculated image was clustered using KMean to segment the area of burnt and unburnt .

<img width="452" alt="s2" src="https://github.com/lisahligono/stemist_hack2/assets/72496335/abc8da54-4ee1-4ad3-a7b9-fa776796e6ce">


The above images on the left hand side is a label of burnt area that we obtain from Copernicus and the right hand side is the burnt area segmentation from the FireCLR model.
The yellow area is the burnt area and purple area is the unburnt area.

<img width="456" alt="s3" src="https://github.com/lisahligono/stemist_hack2/assets/72496335/d6ff3ec4-d720-41de-ba80-32ba78e4b3f5">

The confusion matrix evaluated that accuracy is 0.775, precision score is 0.93 and recall score is 0.595 which made F1-score is 0.726. Moreover, it represented that the FireCLR model predicted the unburnt area more than the burnt area which made False Negative almost as much as True Positive. This model has made Type 2 Error (False Negative) significantly more than Type 1 Error (Type 1 Error) which can cause some lack of response to recover large burnt areas and future preparation. To improve this, we must clarify the factor that made the model cluster the burnt areas as the unburnt areas to decrease recall score.

<b>SAM</b>

<img width="452" alt="s4" src="https://github.com/lisahligono/stemist_hack2/assets/72496335/9f687a26-6bf9-44e4-b353-38899a37d7e1">


The above images on the left hand side is a label of burnt area that we obtained from Copernicus and the right hand side is the burnt area segmentation from the SAM model which segmented smoother and more precisely.

<img width="444" alt="s5" src="https://github.com/lisahligono/stemist_hack2/assets/72496335/1bf0d3e4-22f0-41df-aa56-0312515b41f3">


The result in statistics evaluated that SAM model giving accuracy 0.885, Precision score 0.919, Recall score 0.844 and F1-score 0.880. From the confusion matrix, the model predictions have more Type 2 Error (False Negative) than Type 1 Error (False Positive). 


<h2>Step 2: Spatial Analysis using GIS</h2>

<h2>Step 3: Web Application</h2>

<b>FLASK</b>

 
Flask is a lightweight web server gateway interface (WSGI) for web application development using python. 

<i>Importing and Setting Up</i>: The Flask application starts by importing the Flask class from the flaskmodule. It then creates a Flask app instance using Flask(__name__). The __name__ parameter is a special Python variable that represents the name of the current module, and it is used by Flask to locate resources such as templates and static files.

<i>Routing and View Function</i>: Flask uses routing to map URLs to view functions. In this application, the root URL ('/') is associated with the base() function. When a user accesses the root URL, the base()function is called, and it generates the interactive map.

<i>Map Rendering and HTML Generation</i>: Inside the base() function, the interactive map is created using Folium. The map is generated with a specified location and zoom level. The GeoJSON data from the shapefile is then added to the map using the folium.GeoJson() method, with a custom style function for coloring the features based on their categories.

<i>Layer Control Integration</i>: To enable users to toggle the visibility of different shapefile layers on the map, a LayerControl is added using folium.LayerControl(). This allows users to interactively switch between different layers of the map.

<i>Running the Flask App</i>: Finally, the Flask app is run using app.run(debug=True). The debug=Trueparameter enables Flask's debug mode, which provides helpful error messages and auto-reloading of the server when code changes are detected. The server starts listening for incoming requests, and when a user accesses the root URL, Flask serves the HTML content of the map to the user's web browser.

<b>FOLIUM</b>

Folium is a powerful Python library used for creating interactive maps and visualizations. It is built on top of Leaflet.js, a widely-used JavaScript library for interactive maps. Folium allows you to create dynamic maps with various data overlays and custom styling, making it a popular choice for data visualization, geospatial analysis, and web mapping applications.

<i>Importing and Setting Up</i>: The Flask application starts by importing the required modules: Flask, folium, and geopandas. The Flask app is created using Flask(__name__), and the base() function is defined as the route handler for the root URL.

<i>Map Initialization</i>: Inside the base() function, a folium map is initialized using folium.Map(). The map is centered at latitude 37.782953 and longitude 23.942564and is set to an initial zoom level of 13.

<i>Custom Style Function</i>: A custom style function is defined to control how the shapefile features are styled on the map. This function uses the style_function parameter of folium.GeoJson() to dynamically set the colors and styles of the shapefile features based on their categories.

<i>Reading and Adding Shapefile Layers</i>: The application reads the shapefile data using geopandas and converts it to GeoJSON format using to_json(). Then, the GeoJSON data is added to the folium map using folium.GeoJson(). The custom style function is applied to each shapefile layer using the style_function parameter, resulting in the shapefile features being colored based on their categories.

<i>Layer Control</i>: A LayerControl is added to the map using folium.LayerControl(). This control allows users to toggle the visibility of different layers, making it easier to view and compare multiple layers on the same map.

<i>Running the Flask App</i>: Finally, the Flask app is run in debug mode using app.run(debug=True), allowing the server to listen for incoming requests and serve the map when the root URL is accessed.

<h2>Solution</h2>

Wildfires are natural disasters that can have devastating impacts on both the environment and human communities. Some areas like our study areas frequently contend with such wildfire occurrences. Disaster managers need to identify and assess damaged areas to prioritise response efforts, allocate resources, and plan for recovery and reconstruction activities. So, our disaster management is separated to following phase:

<b>Pre-Disaster</b>

Preparation

The Greek government has an alarm system to predict the probability of risk of fire. With the implementation of our web map that demonstrates the previous fire burnt area, they can have better management to put out the fire and protect the citizens and their properties.

<b>Post-Disaster</b>

Response

The government rolled out the fire forest protection guidelines for their people and suggested that the citizens work from home and avoid going outside. For the fire fighting forces, they have requested the help of national and got the help from the other countries to help extinguish the fire from both land and air. Moreover, as of 18 July , about 900 people had evacuated from the burning area. 
Recovery
The government had to pay the compensation to their people in case the citizen property was burnt.With our web map,we can examine the urban area, crop land and burnt areas to plan the recovery strategy. Moreover,  from our analysis the most affected area is cropland, with this analysis can help farmers to plan and pick the right crop to plant in the area and also avoid the area that is often burnt.


<h2>References</h2>
Zhang, B. (2022, November 26). Unsupervised Wildfire Change Detection based on Contrastive Learning. arXiv.org. https://arxiv.org/abs/2211.14654
