import unittest

from GraphLib.algorithms.pathSearch.bellman_ford import shortest_paths_bellman_ford
from GraphLib.algorithms.pathSearch.bellman_ford_help_functions import *
from GraphLib.dataStructures.di_graph import DiGraph
from GraphLib.dataStructures.edge import Edge


class Bellman_Ford(unittest.TestCase):
    def test_shortest_paths_bellman_ford(self):
        # TODO: shortest_paths_bellman_ford()
        pass

    def test_find_negative_cycle(self):
        graph = DiGraph()
        for v in ['a', 'b', 'c', 'd']:
            graph.add_node(v)

        graph.add_edge(Edge('a', 'b', 1))
        graph.add_edge(Edge('b', 'c', 2))
        graph.add_edge(Edge('c', 'a', -4))
        graph.add_edge(Edge('c', 'd', 1))

        dist = {'a': 0, 'b': math.inf, 'c': math.inf, 'd': math.inf}
        previous = {'a': 'c', 'b': 'a', 'c': 'b', 'd': 'c'}

        try:
            find_negative_cycle(graph, dist, previous)
        except Exception as e:
            assert e.args[0] == "Negative cycle was found b-c-a-b"

    def test_update_distances(self):
        dist = {'a': 0, 'b': 3, 'c': 1}

        update_distances(make_graph(), dist, {})

        assert dist == {'a': 0, 'b': 2, 'c': 1}

    def test_get_better_edges(self):
        graph = make_graph()
        dist = {'a': 0, 'b': 3, 'c': 1}

        actual_edges = list(get_better_edges(graph, dist))

        expected_edges = [('c', 'b')]

        assert actual_edges == expected_edges

    def test_update_dist(self):
        current = 1
        neighbor = 2
        weight = 2
        dist = {neighbor: 4, current: 1}
        previous = {neighbor: 0}
        update_dist(current, neighbor, dist, weight, previous)

        new_dist = dist[current] + weight
        assert new_dist == 3
        assert dist[neighbor] == new_dist
        assert previous[neighbor] == current

    def test_raise_error(self):
        previous = {'a': 'c', 'b': 'a', 'c': 'b', 'd': 'c'}
        source = 'b'
        prev = 'a'

        try:
            raise_error(prev, source, previous)
        except Exception as e:
            assert e.args[0] == "Negative cycle was found b-c-a-b"

    def test_build_cycle_with_empty_previous_list(self):
        try:
            build_cycle(3, 1, [])
        except Exception as e:
            assert e.args[0] == "There isn't enough information to build a cycle"

    def test_build_cycle(self):
        prev = 3
        source = 1
        previous = {prev: 2, 2: source}
        cycle = build_cycle(prev, source, previous)

        assert cycle == [1, 2, 3, 1]

    def test_build_cycle_without_some_nodes(self):
        cycle = build_cycle(3, 1, {2: 1, 3: 1})

        assert cycle == [1, 3, 1]

    def test_initialise_distances(self):
        nodes = [1, 3, 5]
        source = 3
        actual_distances = initialise_distances(nodes, source)

        expected_distances = {1: math.inf, 3: 0, 5: math.inf}

        assert actual_distances == expected_distances


def make_graph():
    graph = DiGraph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_edge(Edge('a', 'b', 3))
    graph.add_edge(Edge('a', 'c', 1))
    graph.add_edge(Edge('c', 'b', 1))

    return graph
