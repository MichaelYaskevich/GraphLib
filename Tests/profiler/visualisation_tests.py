import unittest

from GraphLib.profiler.visualisation import approximate, visualize


class Test(unittest.TestCase):
    def test_approximation(self):
        graph_size_array = [1, 2, 3, 4]
        time_results_array = [1, 4, 9, 16]

        expected_sizes = []
        steps = len(graph_size_array) * 10
        for i in range(1, steps + 1):
            expected_sizes.append(i * 0.1)

        expected_results = []
        for i in range(steps):
            expected_results.append(expected_sizes[i] ** 2)

        actual_sizes, actual_results = approximate(graph_size_array, time_results_array)

        assert expected_sizes == actual_sizes
        for i in range(steps):
            assert abs(expected_results[i] - actual_results[i]) < 0.001

    def test_visualize(self):
        #TODO: сделать путь не абсолютным
        path = 'D:\The_p\prog\python\GraphLib\GraphLib\\resources\\test_plot.pdf'

        sizes, results = approximate([1, 2, 3, 4], [1, 4, 9, 16])
        d = {sizes[i]: results[i] for i in range(len(sizes))}
        dictionaries = [d]
        labels = ['1']

        sizes, results = approximate([1, 2, 3, 4], [1, 8, 27, 64])
        d = {sizes[i]: results[i] for i in range(len(sizes))}
        dictionaries.append(d)
        labels.append('2')

        visualize(dictionaries, labels, path)
