import os
import folium
import webbrowser

class MapRoute:
    def __init__(self, dataframe, best_route):
        self.dataframe = dataframe
        self.best_route = best_route

    def map(self, cities_col='cidade', lat_col='lat', long_col='long'):
        cities, coords = self.route(cities_col, lat_col, long_col)
        m = folium.Map(location=coords[0], zoom_start=5, control_scale=True)

        self.add_markers(m, cities, coords)
        self.add_line(m, coords)
        self.show(m)

    def show(self, map):
        path = os.path.join(os.getcwd(), 'caixeiro_viajante', 'data', 'temp', 'map.html')
        map.save(path)
        webbrowser.open(path, new=2)

    def route(self, cities_col='cidade', lat_col='lat', long_col='long'):
        cities_route = []
        coords_route = []
        for i in self.best_route:
            cities_route.append(self.dataframe[cities_col].iloc[i])
            coords_route.append((self.dataframe[lat_col].iloc[i], self.dataframe[long_col].iloc[i]))

        return cities_route, coords_route
    
    def add_markers(self, map, cities_route, coords_route):
        # Confere se a viagem será circular (primeira e última cidades são a mesma)
        if cities_route[0] == cities_route[-1]:
            cities_route.pop()

        for i, city in enumerate(cities_route):
            # Define a cor dos marcadores, diferenciando o ponto de saída das demais
            color = 'green'
            if i == 0:
                color = 'red'

            coordinate = coords_route[i]
            folium.Marker(
                location=coordinate,
                tooltip=city,
                popup=f'{i+1}º: {city}\n{coordinate}',
                icon=folium.Icon(color=color)
            ).add_to(map)

    def add_line(self, map, coords_route):
        folium.PolyLine(coords_route, color='blue').add_to(map)