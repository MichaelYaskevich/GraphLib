import math
import unittest

from GraphLib.algorithms.pathSearch.dijkstra import dijkstra_shortest_paths
from GraphLib.algorithms.pathSearch.dijkstra_help_functions import initialise_distances, visit, update_distance
from GraphLib.dataStructures.di_graph import DiGraph
from GraphLib.dataStructures.edge import Edge


class Dijkstra(unittest.TestCase):
    def test_dijkstra_shortest_paths(self):
        graph = make_graph()
        actual_previous, actual_dist = dijkstra_shortest_paths(graph, 'a')

        expected_dist = {'a': 0, 'b': 1, 'c': 2}
        expected_previous = {'a': None, 'b': 'a', 'c': 'b'}

        assert actual_dist == expected_dist
        assert actual_previous == expected_previous

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
        graph = make_graph()
        visited = set()
        dist = {'a': 0, 'b': math.inf, 'c': math.inf}
        previous = {}
        sorted_nodes = [(0, 'a')]
        visit('a', visited, graph, dist, previous, sorted_nodes)
        visit('b', visited, graph, dist, previous, sorted_nodes)

        assert len(visited) == 2
        assert 'a' in visited
        assert 'b' in visited
        assert previous['c'] == 'b'
        assert previous['b'] == 'a'
        assert dist['c'] == 2
        assert dist['b'] == 1
        assert sorted_nodes == [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'c')]


def make_graph():
    graph = DiGraph()
    for v in ['a', 'b', 'c']:
        graph.add_node(v)
    graph.add_edge(Edge('a', 'c', 3))
    graph.add_edge(Edge('a', 'b', 1))
    graph.add_edge(Edge('b', 'c', 1))

    return graph
