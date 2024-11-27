import json

# Sample GeoJSON data
geojson_data = '''
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [45.0, 90.5]
      },
      "properties": {
        "name": "point"
      }
    }
  ]
}
'''

geo_data = json.loads(geojson_data)


for feature in geo_data['features']:
    geometry_type = feature['geometry']['type']
    coordinates = feature['geometry']['coordinates']
    print(f"Geometry: {geometry_type}, Coordinates: {coordinates}")
