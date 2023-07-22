from flask import Flask
import folium
import geopandas as gpd

app = Flask(__name__)

@app.route("/")
def base():
    map = folium.Map(
        location=[38.0458, 23.8585]
    )

    shapefile_path = '/Users/lisahligono/practice-plus/flask/aoi/EMSR672_AOI01_GRA_PRODUCT_observedEventA_v2.shp'
    shapefile_data = gpd.read_file(shapefile_path)
    geojson_data = shapefile_data.to_crs('EPSG:4326').to_json()
    folium.GeoJson(geojson_data).add_to(map)

    folium.LayerControl().add_to(map)
    return map._repr_html_()




    shapefile_path = '/Users/lisahligono/practice-plus/flask/StudyArea/Grand_Bahama.shp'
    shapefile_data = gpd.read_file(shapefile_path)
    geojson_data = shapefile_data.to_crs('EPSG:4326').to_json()
    folium.GeoJson(geojson_data).add_to(shortest_route_map)

    folium.LayerControl().add_to(shortest_route_map)
    shortest_route_map.save('any.html')
    return shortest_route_map._repr_html_()


if __name__ == "__main__":
    app.run(debug=True)