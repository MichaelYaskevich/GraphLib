import unittest

from GraphLib.algorithms.pathSearch.algorithm_for_DAG import *
from GraphLib.algorithms.pathSearch.algorithm_for_DAG_help_methods import *
from GraphLib.dataStructures.di_graph import DiGraph
from GraphLib.dataStructures.edge import Edge


class Algorithm_for_DAG(unittest.TestCase):
    def test_topological_sort_no_cycle(self):
        adjacency_lists = {'a': ['b', 'c'], 'b': ['c'], 'c': []}

        sorted_vertexes = topological_sort(adjacency_lists)

        assert sorted_vertexes == ['a', 'b', 'c']

    def test_topological_sort_with_cycle(self):
        adjacency_lists = {'a': ['b'], 'b': ['c'], 'c': ['a']}
        try:
            topological_sort(adjacency_lists)
        except CycleError as e:
            assert e.args[0] == "There is a cycle"

        adjacency_lists = {'a': ['b'], 'b': ['c'], 'c': ['d'], 'd': ['b']}
        try:
            topological_sort(adjacency_lists)
        except CycleError as e:
            assert e.args[0] == "There is a cycle"

    def test_find_shortest_paths(self):
        # TODO: find_shortest_paths()
        pass

    def test_shortest_paths_for_dag(self):
        # TODO: shortest_paths_for_dag()
        pass

    def test_initialize_input_degrees(self):
        adjacency_lists = {'a': ['b', 'c'], 'b': ['c'], 'c': []}
        expected_deg_in_dict = {'a': 0, 'b': 1, 'c': 2}

        actual_deg_in_dict = initialize_input_degrees(adjacency_lists)

        assert actual_deg_in_dict == expected_deg_in_dict

    def test_initialize_queue(self):
        adjacency_lists = {'a': ['b', 'c'], 'b': ['c'], 'c': []}
        deg_in_list = initialize_input_degrees(adjacency_lists)
        actual_queue = initialize_queue(deg_in_list, adjacency_lists.keys())

        assert actual_queue.qsize() == 1
        assert actual_queue.get() == 'a'

    def test_visit(self):
        adjacency_lists = {'a': ['b', 'c'], 'b': ['c'], 'c': []}
        deg_in_list = initialize_input_degrees(adjacency_lists)
        visited_queue = queue.Queue()
        visit(deg_in_list, 'b', visited_queue)

        assert visited_queue.qsize() == 1
        assert visited_queue.get() == 'b'

    def test_update_distances(self):
        graph = make_graph()
        distances = {'a': 0, 'b': 1, 'c': 4}
        previous = {}

        update_distances(graph, distances, previous, 'b')

        assert distances['c'] == 3
        assert previous['c'] == 'b'

    def test_find_vertex_index(self):
        vertexes = ['b', 'a', 'c']
        vertex = 'a'
        actual_index = find_vertex_index(vertexes, vertex)

        assert actual_index == 1


def make_graph():
    graph = DiGraph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_edge(Edge('a', 'b', 1))
    graph.add_edge(Edge('b', 'c', 2))
    graph.add_edge(Edge('a', 'c', 4))

    return graph
