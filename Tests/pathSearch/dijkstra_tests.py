import math
import unittest

from GraphLib.algorithms.pathSearch.dijkstra_help_functions import initialise_distances, visit, update_distance
from GraphLib.dataStructures.di_graph import DiGraph


class Dijkstra(unittest.TestCase):
    def test_initialise_distances(self):
        nodes = [1, 3, 5]
        source = 3
        actual_distances = initialise_distances(nodes, source)

        expected_distances = {1: math.inf, 3: 0, 5: math.inf}

        assert actual_distances == expected_distances

    def test_update_distance_with_better_distance(self):
        current_node = 1
        neighbor = 2
        dist = {1: 1, 2: 4}
        weight = 2
        previous = {neighbor: 0}
        sorted_nodes = [(2, 3), (4, 4)]
        update_distance(current_node, neighbor, weight, dist, previous, sorted_nodes)

        new_dist = dist[current_node] + weight
        assert new_dist == 3
        assert dist[neighbor] == new_dist
        assert previous[neighbor] == current_node
        assert sorted_nodes == [(2, 3), (new_dist, neighbor), (4, 4)]

    def test_update_distance_with_worse_distance(self):
        current_node = 1
        neighbor = 2
        dist = {1: 1, 2: 4}
        weight = 4
        previous = {neighbor: 0}
        sorted_nodes = [(2, 3), (4, 4)]
        update_distance(current_node, neighbor, weight, dist, previous, sorted_nodes)

        new_dist = dist[current_node] + weight
        assert new_dist == 5
        assert dist[neighbor] == 4
        assert previous[neighbor] == 0
        assert sorted_nodes == [(2, 3), (4, 4)]

    def test_visit(self):
        pass
        # current_node = 1
        # visited = set()
        # graph = DiGraph()
        # dist = {}
        # previous = {}
        # sorted_nodes = []
        # visit(current_node, visited, graph, dist, previous, sorted_nodes)
        #
        # assert len(visited) == 1
        # assert current_node in visited


