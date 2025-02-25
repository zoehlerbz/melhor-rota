import pandas as pd
from itertools import permutations
from caixeiro_viajante.src.services.dist_matrix import DistMatrix
from caixeiro_viajante.src.services.find_route import BestRoute
from caixeiro_viajante.src.services.map_route import MapRoute

class App:
    def __init__(self, path, start_city, end_city):
        self.dataframe = pd.read_csv(path)
        self.start_index = self.dataframe[self.dataframe['cidade'] == start_city].index[0]
        self.end_index = self.dataframe[self.dataframe['cidade'] == end_city].index[0]

    def run(self):
        Dists = DistMatrix(dataframe=self.dataframe, lat_col='lat', long_col='long')
        matrix = Dists.matrix()

        tsp = BestRoute(matrix=matrix, start_index=self.start_index, end_index=self.end_index)
        best_route, min_distance = tsp.brute_force()

        Map = MapRoute(self.dataframe, best_route)
        Map.map()

        if best_route and min_distance:
            route = [self.dataframe['cidade'].iloc[i] for i in best_route]
            print("Rota mais curta:", " ➝  ".join(route))
            print(f"Distância total: {min_distance: .2f} km")
        else:
            print("Erro: Nenhuma rota encontrada.")