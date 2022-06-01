import argparse

from GraphLib.algorithms.pathSearch \
    import dijkstra, bellman_ford, algorithm_for_DAG, floyd
from GraphLib.interface.read_adjacency_lists import read_adjacency_lists
from GraphLib.interface.read_weight_matrix import read_weight_matrix

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
Txt file must look like this:\n
4\n
0 1 0 1\n
1 0 2 5\n
1 3 0 -4\n
0 0 5 0\n
1\n
4
Nodes count
{Nodes count} lines which represent graph as weight matrix
    where '-' means that path doesn't exist
Source node
Destination node
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=f'Use algorithms from console.\n'
                    f'You can provide algorithm '
                    f'with graph in txt file in any of the next '
                    f'formats: \n{graph_adjacency_list_file_format} \n '
                    f'or \n {graph_weight_matrix_file_format}',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('path', type=str, nargs=1,
                        help=f'full path for graph file')
    parser.add_argument('format', type=str, nargs=1, choices=['al', 'wm'],
                        help='Choose format of graph representation:'
                             '"al" for adjacency list and "wm" for '
                             'weight matrix')
    parser.add_argument('algorithm', type=str, nargs=1,
                        choices=['dijkstra', 'bellman_ford',
                                 'algorithm_for_dag', 'floyd'],
                        help=f'algorithm you want to use there are: '
                             f'dijkstra, bellman_ford, '
                             f'algorithm_for_dag, floyd')

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
