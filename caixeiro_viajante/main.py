import pandas as pd
from itertools import permutations
from caixeiro_viajante.src.services.dist_matrix import DistMatrix
from caixeiro_viajante.src.services.find_route import BestRoute

class App:
    def __init__(self, path):
        self.path = path

    def run(self):
        dataframe = pd.read_csv(self.path)
        Dists = DistMatrix(dataframe=dataframe, lat_col='lat', long_col='long')
        matrix = Dists.matrix()

        tsp = BestRoute(matrix)
        best_route, min_distance = tsp.brute_force()

        if best_route and min_distance:
            route = [dataframe['cidade'].iloc[i] for i in best_route]
            print("Rota mais curta:", " ➝  ".join(route))
            print("Distância total:", round(min_distance, 2), "km")
        else:
            print("Erro: Nenhuma rota encontrada para 'Meu Algoritmo'.")