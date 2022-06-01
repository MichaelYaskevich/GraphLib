import unittest

from GraphLib.algorithms.pathSearch.floyd import find_shortest_paths_from_all_to_all, get_path
from GraphLib.algorithms.pathSearch.floyd_help_functions import *
from GraphLib.dataStructures.di_graph import DiGraph
from GraphLib.dataStructures.edge import Edge


class Dijkstra(unittest.TestCase):
    def test_floyd_shortest_paths(self):
        graph = make_graph()
        distances_actual, _ = find_shortest_paths_from_all_to_all(graph)

        distances_expected = {1: {1: 0, 2: 1, 3: 2, 5: 4},
                              2: {1: math.inf, 2: 0, 3: 1, 5: 3},
                              3: {1: math.inf, 2: math.inf, 3: 0, 5: math.inf},
                              5: {1: math.inf, 2: math.inf, 3: 2, 5: 0}}

        assert distances_actual == distances_expected

    def test_get_path(self):
        graph = make_graph()
        _, prior_matrix = find_shortest_paths_from_all_to_all(graph)
        assert get_path(2, 1, prior_matrix) is None
        assert get_path(3, 1, prior_matrix) is None
        assert get_path(3, 2, prior_matrix) is None
        assert get_path(3, 5, prior_matrix) is None
        assert get_path(5, 1, prior_matrix) is None
        assert get_path(5, 2, prior_matrix) is None

        assert get_path(1, 1, prior_matrix) == [1]
        assert get_path(2, 2, prior_matrix) == [2]
        assert get_path(3, 3, prior_matrix) == [3]
        assert get_path(5, 5, prior_matrix) == [5]

        assert get_path(1, 2, prior_matrix) == [1, 2]
        assert get_path(1, 3, prior_matrix) == [1, 2, 3]
        assert get_path(1, 5, prior_matrix) == [1, 2, 5]
        assert get_path(2, 3, prior_matrix) == [2, 3]
        assert get_path(2, 5, prior_matrix) == [2, 5]
        assert get_path(5, 3, prior_matrix) == [5, 3]

    def test_initialise_prior_matrix(self):
        graph = make_graph()
        matrix = initialise_prior_matrix(graph)

        for i in graph.get_nodes():
            for j in graph.get_nodes():
                if i == j or j in graph.adjacency_lists[i]:
                    assert matrix[i][j] == j
                else:
                    assert matrix[i][j] is None

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

        prior_matrix = {0: {0: 0, 1: 0, 2: 0},
                        1: {0: 1, 1: 0, 2: 0},
                        2: {0: 0, 1: 0, 2: 0}}
        update_distance(distances, prior_matrix, w, i, j)

        assert distances[i][j] == 3
        assert prior_matrix[i][j] == 1


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
