import unittest

from GraphLib.dataStructures.graph import *


class Test(unittest.TestCase):
    def testAddingNodesToGraph(self):
        graph = Graph()
        graph.add_node(1)
        graph.add_node(2)
        assert len(graph.get_nodes()) == 2

    def testAddingEdgeToGraph(self):
        graph = Graph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(Edge(1, 2, 3))
        assert 2 in graph.adjacency_lists[1] \
               and 1 in graph.adjacency_lists[2] and graph.get_incident_edge(1, 2).weight == 3

    def testGettingAdjacentNodes(self):
        graph = Graph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(Edge(1, 2, 3))
        result = graph.get_adjacent_nodes(1)
        assert len(result) == 1 and result[0] == 2

    def testFailsWhenAddingAlreadyExistingNode(self):
        graph = Graph()
        graph.add_node(1)
        try:
            graph.add_node(1)
            assert False
        except ValueError as e:
            assert True

    def testFailsWhenAddingAlreadyExistingEdge(self):
        graph = Graph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(Edge(1, 2, 3))
        try:
            graph.add_edge(Edge(1, 2, 5))
            assert False
        except ValueError:
            assert True

    def testFailsWhenAddingEdgeBetweenNonExistentNodes(self):
        graph = Graph()
        try:
            graph.add_edge(Edge(1, 2, 3))
            assert False
        except ValueError:
            assert True
