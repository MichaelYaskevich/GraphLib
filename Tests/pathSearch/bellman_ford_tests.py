import unittest

from GraphLib.algorithms.pathSearch.bellman_ford_help_functions import *


class Bellman_Ford(unittest.TestCase):
    def test_find_negative_cycle(self):
        pass
        # wait for graph
        # find_negative_cycle()

    def test_update_distances(self):
        pass
        # update_distances()
        # wait for graph

    def test_get_better_edges(self):
        pass
        # get_better_edges()
        # wait for graph

    def test_update_dist(self):
        current = 1
        neighbor = 2
        weight = 2
        dist = {neighbor: 4, current: 1}
        previous = {neighbor: 0}
        update_dist(current, neighbor, dist, weight, previous)

        new_dist = dist[current] + weight
        assert new_dist == 3
        assert dist[neighbor] == new_dist
        assert previous[neighbor] == current

    def test_raise_error(self):
        pass
        # raise_error(prev, source, previous)

    def test_build_cycle_with_empty_previous_list(self):
        try:
            build_cycle(3, 1, [])
        except Exception as e:
            assert e.args[0] == "There isn't enough information to build a cycle"

    def test_build_cycle(self):
        prev = 3
        source = 1
        previous = {prev: 2, 2: source}
        cycle = build_cycle(prev, source, previous)

        assert cycle == [1, 2, 3, 1]

    def test_build_cycle_without_some_nodes(self):
        cycle = build_cycle(3, 1, {2: 1, 3: 1})

        assert cycle == [1, 3, 1]

    def test_initialise_distances(self):
        nodes = [1, 3, 5]
        source = 3
        actual_distances = initialise_distances(nodes, source)

        expected_distances = {1: math.inf, 3: 0, 5: math.inf}

        assert actual_distances == expected_distances
