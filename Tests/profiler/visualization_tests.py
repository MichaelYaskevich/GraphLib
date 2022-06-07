import unittest
from pathlib import Path
from PIL import Image
from PIL import ImageChops

from GraphLib.profiler.approximation import approximate
from GraphLib.profiler.visualization import visualize_time, visualize_memory


class VisualizationTests(unittest.TestCase):
    def test_visualize_time(self):
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

        visualize_time(dictionaries, labels,
                       point_dictionaries, confidence_intervals, ['black', 'blue'], path)

        actual_image = Image.open(path)

        assert ImageChops.difference(expected_image, actual_image).getbbox() is None

    # def test_visualize_memory(self):
    #     ROOT_DIR = Path(__file__).parent.parent.parent
    #     path = Path(ROOT_DIR, 'Tests\\resources\\actual_memory_plot.png')
    #
    #     expected_image = Image.open(
    #         Path(ROOT_DIR, 'Tests\\resources\\expected_memory_plot.png'))
    #
    #     colors = ['black', 'blue']
    #     labels = ['1', '2']
    #     points_dictionaries = []
    #     points_dictionaries.append({1: 2, 2: 3})
    #     points_dictionaries.append({1: 1, 2: 5})
    #
    #     x = [1, 2, 3, 4]
    #     y = [1, 4, 9, 16]
    #     approximate(x, y)
    #     data_dictionaries = []
    #
    #
    #
    #     visualize_memory(data_dictionaries, labels, colors, path)
    #
    #     actual_image = Image.open(path)
    #
    #     assert ImageChops.difference(expected_image, actual_image).getbbox() is None
