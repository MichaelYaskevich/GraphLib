import unittest

from GraphLib.algorithms.pathSearch.floyd import floyd_shortest_path
from GraphLib.algorithms.pathSearch.floyd_help_functions import *
from GraphLib.dataStructures.di_graph import DiGraph
from GraphLib.dataStructures.edge import Edge


class Dijkstra(unittest.TestCase):
    def test_floyd_shortest_path(self):
        graph = make_graph()
        distances_actual = floyd_shortest_path(graph)

        distances_expected = {1: {1: 0, 2: 1, 3: 2, 5: 4},
                              2: {1: math.inf, 2: 0, 3: 1, 5: 3},
                              3: {1: math.inf, 2: math.inf, 3: 0, 5: math.inf},
                              5: {1: math.inf, 2: math.inf, 3: 2, 5: 0}}

        assert distances_actual == distances_expected

    def test_initialise_matrix_of_distances(self):
        graph = make_graph()
        distances_actual = initialise_matrix_of_distances(graph)

        distances_expected = {1: {1: 0, 2: 1, 3: 3, 5: math.inf},
                              2: {1: math.inf, 2: 0, 3: 1, 5: 3},
                              3: {1: math.inf, 2: math.inf, 3: 0, 5: math.inf},
                              5: {1: math.inf, 2: math.inf, 3: 2, 5: 0}}

        assert distances_expected == distances_actual

    def test_update_distance(self):
        distances = {0: {0: 0, 1: 0, 2: 0},
                     1: {0: 0, 1: 0, 2: 0},
                     2: {0: 0, 1: 0, 2: 0}}
        w, i, j = 0, 1, 2
        distances[i][j] = 4
        distances[i][w] = 1
        distances[w][j] = 2

        update_distance(distances, w, i, j)

        assert distances[i][j] == 3


def make_graph():
    graph = DiGraph()
    for node in [1, 2, 3, 5]:
        graph.add_node(node)
    graph.add_edge(Edge(1, 2, 1))
    graph.add_edge(Edge(1, 3, 3))
    graph.add_edge(Edge(2, 3, 1))
    graph.add_edge(Edge(2, 5, 3))
    graph.add_edge(Edge(5, 3, 2))

    return graph
