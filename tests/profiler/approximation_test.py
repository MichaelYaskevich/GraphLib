import unittest

from graphLib.profiler.approximation import approximate


class ApproximationTests(unittest.TestCase):
    def test_approximation_when_smallest_size_is_1(self):
        graph_size_array = [1, 2, 3, 4]
        time_results_array = [1, 4, 9, 16]

        expected_sizes = []
        for i in range(10, graph_size_array[-1]*10 + 1):
            expected_sizes.append(i * 0.1)

        expected_results = []
        for i in range(len(expected_sizes)):
            expected_results.append(expected_sizes[i] ** 2)

        actual_sizes, actual_results = approximate(
            graph_size_array, time_results_array)

        assert expected_sizes == actual_sizes
        for i in range(len(expected_results)):
            assert abs(expected_results[i] - actual_results[i]) < 0.001

    def test_approximation_when_smallest_size_is_10(self):
        graph_size_array = [10, 12, 13, 14]
        time_results_array = [100, 144, 169, 196]

        expected_sizes = []
        for i in range(graph_size_array[0]*10, graph_size_array[-1]*10 + 1):
            expected_sizes.append(i * 0.1)

        expected_results = []
        for i in range(len(expected_sizes)):
            expected_results.append(expected_sizes[i] ** 2)

        actual_sizes, actual_results = approximate(
            graph_size_array, time_results_array)

        assert expected_sizes == actual_sizes
        for i in range(len(expected_results)):
            assert abs(expected_results[i] - actual_results[i]) < 0.001
