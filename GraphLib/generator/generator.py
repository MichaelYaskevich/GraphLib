from random import shuffle, uniform
from GraphLib.dataStructures.di_graph import DiGraph, is_cyclic
from GraphLib.dataStructures.edge import Edge


def generate_random_graph(nodes_count, min_weight, max_weight):
    if nodes_count <= 0:
        raise ValueError(f"Inappropriate value for nodes_count: {nodes_count}, nodes_count can't be zero or less")
    if min_weight > max_weight:
        raise ValueError(f'Min_weight parameter ({min_weight}) is bigger than max_weight ({max_weight})')

    graph = DiGraph()

    nodes = [str(x) for x in range(nodes_count)]
    for node in nodes:
        graph.add_node(node)

    edges = []
    for x in nodes:
        for y in nodes:
            if x != y:
                edges.append((x, y))
                if is_cyclic(graph):
                    edges.pop()

    shuffle(edges)

    for i in range(len(edges)):
        graph.add_edge(Edge(edges[i][0], edges[i][1], uniform(min_weight, max_weight)))

    return graph


