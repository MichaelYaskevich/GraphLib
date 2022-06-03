import unittest

from GraphLib.dataStructures.di_graph import *


class Test(unittest.TestCase):
    def test_adding_nodes_to_DiGraph(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        assert len(graph.get_nodes()) == 2

    def test_adding_directed_edge_to_Graph(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(Edge(1, 2, 3))
        assert 2 in graph.adjacency_lists[1] \
               and 1 not in graph.adjacency_lists[2] and \
               graph.get_incident_edge(1, 2).weight == 3

    def test_getting_adjacent_nodes(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(Edge(1, 2, 3))
        result = graph.get_adjacent_nodes(1)
        assert len(result) == 1 and result[0] == 2

    def test_fails_adding_existing_node(self):
        graph = DiGraph()
        graph.add_node(1)
        try:
            graph.add_node(1)
            assert False
        except ValueError:
            assert True

    def test_fails_adding_existing_edge(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(Edge(1, 2, 3))
        try:
            graph.add_edge(Edge(1, 2, 5))
            assert False
        except ValueError:
            assert True

    def test_fails_adding_edge_between_non_existent_nodes(self):
        graph = DiGraph()
        try:
            graph.add_edge(Edge(1, 2, 3))
            assert False
        except ValueError:
            assert True

    def test_two_edges_are_not_equal_if_direction_is_different(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(Edge(1, 2, 3))
        graph.add_edge(Edge(2, 1, 3))
        assert graph.get_incident_edge(1, 2) != graph.get_incident_edge(2, 1)

    def test_two_nodes_are_not_adjacent_when_there_is_one_directed_edge(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
