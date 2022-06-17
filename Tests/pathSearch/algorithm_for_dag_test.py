import unittest

from GraphLib.algorithms.pathSearch.algorithm_for_DAG import *
from GraphLib.algorithms.pathSearch.algorithm_for_DAG_help_methods import *
from Tests.dataStructures.graph_making_functions_test import *


class AlgorithmForDagTests(unittest.TestCase):
    def test_topological_sort_no_cycle(self):
        adjacency_lists = {'a': ['b', 'c'], 'b': ['c'], 'c': []}

        sorted_vertexes = topological_sort(adjacency_lists)

        assert sorted_vertexes == ['a', 'b', 'c']

    def test_topological_sort_with_cycle(self):
        adjacency_lists = {'a': ['b'], 'b': ['c'], 'c': ['a']}
        try:
            topological_sort(adjacency_lists)
        except CycleError as e:
            assert e.args[0] == "There is a cycle a-b-c-a"

        adjacency_lists = {'a': ['b'], 'b': ['c'], 'c': ['d'], 'd': ['b']}
        try:
            topological_sort(adjacency_lists)
        except CycleError as e:
            assert e.args[0] == "There is a cycle b-c-d-b"

    def test_get_cycle(self):
        expected = ['a', 'b', 'c', 'a']

        actual = get_cycle({'a': ['b'], 'b': ['c'], 'c': ['a']})

        assert actual == expected

    def test_shortest_paths_for_dag(self):
        find_paths_test(make_graph(), 'a',
                        {'a': 0, 'b': 1, 'c': 3},
                        {'a': None, 'b': 'a', 'c': 'b'})
        find_paths_test(make_graph1(), 1,
                        {1: 0, 2: 4, 3: 4, 4: 11},
                        {1: None, 2: 3, 3: 1, 4: 3})
        find_paths_test(make_graph2(), 1,
                        {1: 0, 2: 10, 3: 50, 4: 30, 5: 60},
                        {1: None, 2: 1, 3: 4, 4: 1, 5: 3})
        find_paths_test(make_graph3(), 1,
                        {1: 0, 2: 12, 3: 24, 4: 36, 5: 12, 6: 30, 7: 56},
                        {1: None, 2: 1, 3: 2, 4: 3, 5: 1, 6: 1, 7: 4})
        find_paths_test(make_graph4(), 1,
                        {1: 0, 2: 4, 3: 2, 4: 9, 5: 5, 6: 20},
                        {1: None, 2: 1, 3: 1, 4: 5, 5: 3, 6: 4})

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


def find_paths_test(graph, source, expected_dist, expected_previous):
    actual_previous, actual_dist = get_prev_and_dist(graph, source)

    assert actual_dist == expected_dist
    assert actual_previous == expected_previous


def make_graph():
    graph = DiGraph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_edge(Edge('a', 'b', 1))
    graph.add_edge(Edge('b', 'c', 2))
    graph.add_edge(Edge('a', 'c', 4))

    return graph
