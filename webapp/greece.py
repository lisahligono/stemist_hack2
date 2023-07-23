from flask import Flask
import folium
import geopandas as gpd
from color import *

app = Flask(__name__)

@app.route("/")
def base():
    map = folium.Map(
        location=[37.782953, 23.942564],
        zoom_start=13
    )

    shapefile_path = '/Users/lisahligono/practice-plus/flask/aoi/EMSR672_AOI01_GRA_PRODUCT_observedEventA_v2.shp'
    shapefile_data = gpd.read_file(shapefile_path)
    geojson_data = shapefile_data.to_crs('EPSG:4326').to_json()
    folium.GeoJson(geojson_data, style_function=purple, name='Copernicus').add_to(map)

    shapefile_path = '/Users/lisahligono/practice-plus/flask/foruploadshp/clipsambuiltup.shp'
    shapefile_data = gpd.read_file(shapefile_path)
    geojson_data = shapefile_data.to_crs('EPSG:4326').to_json()
    folium.GeoJson(geojson_data, style_function=red, name='Buildings').add_to(map)

    shapefile_path = '/Users/lisahligono/practice-plus/flask/foruploadshp/clipsamnature.shp'
    shapefile_data = gpd.read_file(shapefile_path)
    geojson_data = shapefile_data.to_crs('EPSG:4326').to_json()
    folium.GeoJson(geojson_data, style_function=cat, name='Natural landcover').add_to(map)

    shapefile_path = '/Users/lisahligono/practice-plus/flask/foruploadshp/clrmask.shp'
    shapefile_data = gpd.read_file(shapefile_path)
    geojson_data = shapefile_data.to_crs('EPSG:4326').to_json()
    folium.GeoJson(geojson_data, style_function=pink, name='FireCLR burn mask').add_to(map)

    shapefile_path = '/Users/lisahligono/practice-plus/flask/foruploadshp/differenceclr.shp'
    shapefile_data = gpd.read_file(shapefile_path)
    geojson_data = shapefile_data.to_crs('EPSG:4326').to_json()
    folium.GeoJson(geojson_data, style_function=yellow, name='Copernicus Vs CNN').add_to(map)

    shapefile_path = '/Users/lisahligono/practice-plus/flask/foruploadshp/differencesam.shp'
    shapefile_data = gpd.read_file(shapefile_path)
    geojson_data = shapefile_data.to_crs('EPSG:4326').to_json()
    folium.GeoJson(geojson_data, style_function=yellow, name='Copernicus Vs SAM').add_to(map)

    shapefile_path = '/Users/lisahligono/practice-plus/flask/foruploadshp/sammask.shp'
    shapefile_data = gpd.read_file(shapefile_path)
    geojson_data = shapefile_data.to_crs('EPSG:4326').to_json()
    folium.GeoJson(geojson_data, style_function=green, name='SAMGEO').add_to(map)

    folium.LayerControl().add_to(map)
    return map._repr_html_()


if __name__ == "__main__":
    app.run(debug=True)