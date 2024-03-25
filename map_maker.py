import folium
import pandas as pd

# Charger les données depuis le CSV
data = pd.read_csv("datas_complete/25-03-2024 17H03_airbnb.csv", sep=";")

print(data.head())

most_line_of_id = data['ID'].value_counts()
print(most_line_of_id)

# Créer une carte centrée sur Lyon
latitude, longitude = 45.75, 4.85 # Lyon
map = folium.Map(location=[latitude, longitude], zoom_start=14)

for row in data.itertuples():
    html = f"<b>Hôte :</b> {row.Hote}</br></br><a href='{row.URL}' target='_blank'>{row.Title}</a>"
    iframe = folium.IFrame(html)

    popup = folium.Popup(iframe,
                     min_width=250,
                     max_width=600,
                     min_height=250,
                     max_height=600)

    folium.Marker(
        location=[row.Latitude, row.Longitude],
        popup=popup
        ).add_to(map)

map.save("lyon.html")