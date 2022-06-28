import unittest
from pathlib import Path
from PIL import Image
from PIL import ImageChops

from profiler import VisualizationData
from profiler.approximation import approximate
from profiler import visualize_time


class VisualizationTests(unittest.TestCase):
    def test_visualize_time(self):
        ROOT_DIR = Path(__file__).parent.parent.parent
        path = Path(ROOT_DIR, 'tests\\resources\\actual_plot.png')

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
            Path(ROOT_DIR, 'tests\\resources\\expected_plot.png'))

        data = VisualizationData(
            dictionaries, point_dictionaries, confidence_intervals)

        visualize_time(data, labels, ['black', 'blue'], path)

        actual_image = Image.open(path)

        assert ImageChops.difference(
            expected_image, actual_image).getbbox() is None
