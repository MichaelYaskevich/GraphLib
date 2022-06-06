import unittest

from GraphLib.profiler.profiler import *

times = [170.1, 156.3, 202.2, 196.6, 221.7, 250.3, 187.8, 177.8, 206.4, 233.3, 199.9]


class ProfilerTests(unittest.TestCase):
    def test_calculate_min_func(self):
        assert calculate_min_time(times) == 156.3

    def test_calculate_average(self):
        assert calculate_average_time(times) == 200.2181818181818

    def test_standard_deviation(self):
        avg_time = calculate_average_time(times)
        assert calculate_standard_deviation(times, avg_time) == 27.59002784274848

    def test_confidence_interval(self):
        avg_time = calculate_average_time(times)
        std_deviation = calculate_standard_deviation(times, avg_time)
        assert calculate_confidence_interval(times, std_deviation) == 18.534909711580788

