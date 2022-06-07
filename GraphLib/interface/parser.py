import argparse
import unittest

from GraphLib.algorithms.pathSearch \
    import dijkstra, bellman_ford, algorithm_for_DAG, floyd
from GraphLib.interface.read_adjacency_lists import read_adjacency_lists
from GraphLib.interface.read_weight_matrix import read_weight_matrix
from GraphLib.profiler.profiler import profile_all_algorithms

graph_adjacency_list_file_format = '''
nodes count
record for every node in format:
i j weight(i, j) k weight(i, k) ... n weight(i, n)
where j, k, ..., n are neighbours for node i
source node
target node or - if you want to see all paths from source

example:
4
a b 25 c 4
b 0
c a 0 b 7
d 0
a
-'''

graph_weight_matrix_file_format = '''
Txt file can look like this:
4
0 1 0 1
1 0 2 5
1 3 0 -4
0 0 5 0
1
4
Nodes count
{Nodes count} lines which represent graph as weight matrix
    where '-' means that path doesn't exist
Source node
Destination node
'''


def run():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)

    subparsers = parser.add_subparsers(help='', dest='name')

    test_parser = subparsers.add_parser('test', description='Run all test in project',
                                        formatter_class=argparse.RawDescriptionHelpFormatter)

    reporter_parser = subparsers.add_parser('report',
                                            description='Make a pdf report about algorithms in GraphLib',
                                            formatter_class=argparse.RawDescriptionHelpFormatter)
    reporter_parser.add_argument('path', type=str, nargs=1, help='Path where your report will be saved')

    graph_lib_parser = subparsers.add_parser('find_path',
                                             description=f'Use algorithms from console.\nYou can '
                                                         f'provide algorithm with graph in txt file in '
                                                         f'any of the next '
                                                         f'formats: \n{graph_adjacency_list_file_format}'
                                                         f'\n\n====OR====\n{graph_weight_matrix_file_format}',
                                             formatter_class=argparse.RawDescriptionHelpFormatter)
    graph_lib_parser.add_argument('path', type=str, nargs=1, help=f'full path for graph file')
    graph_lib_parser.add_argument('format', type=str, nargs=1, choices=['al', 'wm'],
                                  help='Choose format of graph representation:'
                                       '"al" for adjacency list and "wm" for '
                                       'weight matrix')
    graph_lib_parser.add_argument('algorithm', type=str, nargs=1,
                                  choices=['dijkstra', 'bellman_ford', 'algorithm_for_dag', 'floyd'],
                                  help=f'algorithm you want to use, choices are: '
                                       f'dijkstra, bellman_ford, algorithm_for_dag, floyd')
    algs_all_paths = {'dijkstra': dijkstra.find_shortest_paths,
                      'bellman_ford': bellman_ford.find_shortest_paths,
                      'algorithm_for_dag':
                          algorithm_for_DAG.find_shortest_paths,
                      'floyd': floyd.find_shortest_paths_from_source}
    algs_single_path = {'dijkstra': dijkstra.find_shortest_path,
                        'bellman_ford': bellman_ford.find_shortest_path,
                        'algorithm_for_dag':
                            algorithm_for_DAG.find_shortest_path,
                        'floyd': floyd.find_shortest_path}

    args = parser.parse_args()
    if args.name == 'report':
        profile_all_algorithms(args.path[0])
        return
    if args.name == 'test':
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
        return
    try:
        with open(args.path[0], 'r') as graph_file:
            if args.format[0] == 'al':
                graph, source, destination = read_adjacency_lists(
                    graph_file.readline)
                if graph_file.read() != '':
                    raise Exception('wrong format of the file given')
            else:
                graph, source, destination = read_weight_matrix(
                    graph_file.readlines())
        if destination == '-':
            alg = algs_all_paths[args.algorithm[0]]
            try:
                for path, distance in alg(graph, source):
                    print('path: ', '-'.join(path), f"weight: {distance}")
            except Exception as e:
                print(e.args[0])
        else:
            alg = algs_single_path[args.algorithm[0]]
            try:
                path, distance = alg(graph, source, destination)
                print('path: ', '-'.join(path), f"weight: {distance}")
            except Exception as e:
                print(e.args[0])
    except Exception:
        print('wrong format of the file given')
