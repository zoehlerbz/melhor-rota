from itertools import permutations

class BestRoute:
    def __init__(self, matrix, start_index=0, end_index=0):
        self.matrix = matrix
        self.start_index = start_index
        self.end_index = end_index

    def brute_force(self):
        if self.start_index == self.end_index:
            cities = list(range(len(self.matrix) + 1))  # Adiciona um índice ao final para simular a cidade de retorno
            end = cities[-1]
        else:
            cities = list(range(len(self.matrix)))
            end = self.end_index

        min_distance = float('inf')
        best_route = None

        for perms in permutations(cities):  # Ordem de cidades, sem repetições
            if perms[0] == self.start_index and perms[-1] == end:
                perms = list(perms)  # Converte 'perms' para lista
                if self.start_index == self.end_index:
                    perms[-1] = self.start_index  # Substitui o último índice pela cidade de início

                route = list(perms)
                distance = sum(self.matrix[route[i], route[i+1]] for i in range(len(route) - 1))
                if distance < min_distance:
                    min_distance = distance
                    best_route = route

        return best_route, min_distance