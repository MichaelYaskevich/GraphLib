from GraphLib.dataStructures.di_graph import DiGraph
from GraphLib.dataStructures.edge import Edge

'''
4
a b 25 c 4
b 0
c a 0 b 7
d 0
1
4
'''


def read_adjacency_lists(get_line):
    graph = DiGraph()
    n = int(get_line())
    for i in range(n):
        input_vertexes = get_line().split()
        current_node = input_vertexes[0]
        next_vertexes = []
        if current_node not in graph.get_nodes():
            graph.add_node(current_node)
        for j in range(2, len(input_vertexes), 2):
            node, weight = input_vertexes[j - 1], int(input_vertexes[j])
            next_vertexes.append(node)
            if node not in graph.get_nodes():
                graph.add_node(node)
            graph.add_edge(Edge(current_node, node, weight))
    source = get_line().strip()
    target = get_line().strip()

    return graph, source, target


if __name__ == '__main__':
    read_adjacency_lists(input)
