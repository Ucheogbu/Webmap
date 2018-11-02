import folium
import pandas as pd


# make an object of the volcano.txt file using pandas read_csv function
df = pd.read_csv('volcano.txt')
# Get mean of the latitude column
latmean = df['LAT'].mean()
# Get mean of the longitude column
lonmean = df['LON'].mean()
# make a map object

# Use the computed mean variables to place our map on the center of the volcano locations
map = folium.Map(location=[latmean, lonmean], zoom_start=5, tiles='Stamen Terrain')

# generate unique color for different range of elevation to enable color coding of data


def color(elev):
    if elev in range(0, 1000):
        col = 'green'
    elif elev in range(1001, 2000):
        col = 'orange'
    elif elev in range(2000, 2999):
        col = 'blue'
    else:
        col = 'red'
    return col
# place markers on the map showing the geo location of the volcanoes
for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color(elev), icon='cloud')).add_to(map)


# save map to a html file
map.save('test4.html')
