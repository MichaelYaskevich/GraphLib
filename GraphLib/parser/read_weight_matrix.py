import argparse
import os.path

from GraphLib.algorithms.pathSearch.dijkstra import *
from GraphLib.algorithms.pathSearch.bellman_ford import *
from GraphLib.algorithms.pathSearch.floyd import *
from GraphLib.algorithms.pathSearch.algorithm_for_DAG import *
from GraphLib.dataStructures.di_graph import DiGraph
from GraphLib.dataStructures.edge import Edge


def parse_args():
    parser = argparse.ArgumentParser(description='Find path in graph')
    parser.add_argument('command',
                        metavar='command_name',
                        type=str,
                        nargs=1,
                        help="Commands available:"
                             "'d' - dijkstra's algorithm\n"
                             "'f' - floyd's algorithm\n"
                             "'bf' - bellman-ford's algorithm\n"
                             "'dag' - algorithm for finding shortest path in directed acyclic graph (DAG)")
    parser.add_argument('path',
                        metavar='path_to_file',
                        type=str,
                        nargs=1,
                        help="Path to txt file that contains incidence matrix\n"
                             "Txt file must look like this:\n"
                             "1\n"
                             "0 1 0 1\n"
                             "1 0 2 5\n"
                             "1 3 0 -4\n"
                             "0 0 5 0\n"
                             "Where first line is source node"
                             "And the rest is adjacency matrix where '0' means path doesn't exist"
                             "If you want to use floyd's algorithm then you can skip first line"
                        )
    args = parser.parse_args()
    lines = read(args.path[0])
    return lines, args.command[0]


def read(file_path: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'Such file does not exist, please enter correct path')
    with open(file_path) as f:
        return f.readlines()


def get_graph_and_source(lines: [], command: str) -> tuple[DiGraph, int]:
    graph = DiGraph()
    source = 0
    matrix_lines = lines

    if command != 'f':
        source = int(lines[0])
        matrix_lines = lines[1:]

    for i, line in enumerate(matrix_lines):
        graph.add_node(i)
    for i, line in enumerate(matrix_lines):
        for j, value in enumerate(line.split()):
            if value == '-':
                continue
            val = int(value)
            if val != 0:
                graph.add_edge(Edge(i, j, val))

    return graph, source if command != 'f' else graph


def find_path(command, graph, src=None):
    if command == 'd':
        return dijkstra_shortest_paths(graph, src)
    if command == 'f':
        return floyd_shortest_path(graph)
    if command == 'bf':
        return shortest_paths_bellman_ford(graph, src)
    if command == 'dag':
        return shortest_paths_for_dag(graph, src)
    raise ValueError('Unknown command')


def main():
    lines, command = parse_args()
    graph, src = get_graph_and_source(lines, command)
    print()


if __name__ == "__main__":
    main()
