import unittest

from src.generator.generator import generate_random_graph


class GeneratorTests(unittest.TestCase):
    def test_fails_generating_graph_with_zero_nodes(self):
        try:
            generate_random_graph(0, 0, 1000)
            assert False
        except ValueError:
            assert True

    def test_fails_when_min_weight_bigger_than_max_weight(self):
        try:
            generate_random_graph(1, 1111, 0)
            assert False
        except ValueError:
            assert True

    def test_generator_generates_correct_graph(self):
        nodes_count = 10
        min_weight = 0
        max_weight = 1000
        graph = generate_random_graph(nodes_count, min_weight, max_weight)
        assert len(graph.get_nodes()) == nodes_count
        for edge in graph.get_edges():
            assert min_weight <= edge.weight <= max_weight
