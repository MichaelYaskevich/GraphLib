import unittest
from pathlib import Path
from PIL import Image
from PIL import ImageChops

from GraphLib.profiler.visualization import approximate, visualize


class VisualizationTests(unittest.TestCase):
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

        actual_sizes, actual_results = approximate(
            graph_size_array, time_results_array)

        assert expected_sizes == actual_sizes
        for i in range(steps):
            assert abs(expected_results[i] - actual_results[i]) < 0.001

    def test_visualize(self):
        ROOT_DIR = Path(__file__).parent.parent.parent
        path = Path(ROOT_DIR, 'Tests\\resources\\actual_plot.png')

        x = [1, 2, 3, 4]
        y = [1, 4, 9, 16]
        intervals = [3, 6, 3, 9]
        confidence_intervals = [
            {x[i]: intervals[i] for i in range(len(x))}]
        point_dictionaries = [{x[i]: y[i] for i in range(len(x))}]
        sizes, results = approximate(x, y)
        d = {sizes[i]: results[i] for i in range(len(sizes))}
        dictionaries = [d]
        labels = ['1']

        y = [1, 8, 27, 64]
        intervals = [3, 6, 6, 12]
        confidence_intervals.append(
            {x[i]: intervals[i] for i in range(len(x))})
        point_dictionaries.append({x[i]: y[i] for i in range(len(x))})
        sizes, results = approximate(x, y)
        d = {sizes[i]: results[i] for i in range(len(sizes))}
        dictionaries.append(d)
        labels.append('2')

        expected_image = Image.open(
            Path(ROOT_DIR, 'Tests\\resources\\expected_plot.png'))

        visualize(dictionaries, labels,
                  point_dictionaries, confidence_intervals, ['black', 'blue'], path)

        actual_image = Image.open(path)

        assert ImageChops.difference(expected_image, actual_image).getbbox() is None
