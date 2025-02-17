import math
import pandas as pd
import numpy as np

class DistMatrix:
    def __init__(self, dataframe, lat_col='lat', long_col='long'):
        self.dataframe = dataframe
        self.lat_col = lat_col
        self.long_col = long_col

    def table(self):
        return pd.DataFrame(self.matrix(), index=[self.dataframe.index], columns=[self.dataframe.index])

    def matrix(self):
        matriz_distancias = np.zeros((len(self.dataframe.index), len(self.dataframe.index)))

        for i in self.dataframe.index:
            self.dataframe_i = list(self.dataframe[['lat', 'long']].iloc[i])
            for j in self.dataframe.index:
                self.dataframe_j = list(self.dataframe[['lat', 'long']].iloc[j])

                matriz_distancias[i, j] = self.haversine(self.dataframe_i, self.dataframe_j)

        return matriz_distancias

    def haversine(self, ponto1, ponto2, R=6371.0):  # Raio médio da Terra em km
        lat1, long1, lat2, long2 = map(math.radians, [*ponto1, *ponto2])
        delta_lat, delta_long = lat2 - lat1, long2 - long1

        a = math.sin(delta_lat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_long/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        return R * c