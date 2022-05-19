import unittest

from GraphLib.algorithms.pathSearch.floyd_help_functions import *


class Dijkstra(unittest.TestCase):
    def test_initialise_matrix_of_distances(self):
        pass
        # wait for graph
        # initialise_matrix_of_distances()

    def test_update_distance(self):
        # distances = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        distances = []
        for i in range(3):
            distances.append([])
            for j in range(3):
                distances[i] = math.inf
        w, i, j = 0, 1, 2
        distances[i][j] = 4
        distances[i][w] = 1
        distances[w][j] = 2

        update_distance(distances, w, i, j)

        assert distances[i][j] == 3
