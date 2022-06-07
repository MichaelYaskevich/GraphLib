import unittest

from GraphLib.profiler.profiler import *
from GraphLib.profiler.statistic import Statistic

times = [170.1, 156.3, 202.2, 196.6, 221.7, 250.3, 187.8, 177.8, 206.4, 233.3, 199.9]


class ProfilerTests(unittest.TestCase):
    def test_calculate_min_func(self):
        assert Statistic(times).minimum == 156.3

    def test_calculate_average(self):
        assert Statistic(times).avg == 200.2181818181818

    def test_standard_deviation(self):
        assert Statistic(times).std_deviation == 27.59002784274848

    def test_confidence_interval(self):
        assert Statistic(times).confidence_interval == 18.534909711580788

