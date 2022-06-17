from graphLib.dataStructures.di_graph import DiGraph
from graphLib.dataStructures.edge import Edge


def make_graph1():
    graph = DiGraph()
    for i in range(4):
        graph.add_node(i + 1)
    graph.add_edge(Edge(1, 2, 25))
    graph.add_edge(Edge(1, 3, 4))
    graph.add_edge(Edge(3, 2, 0))
    graph.add_edge(Edge(3, 4, 7))

    return graph
    # source = 1
    # path 1-2: {1, 3, 2}, length = 4
    # path 1-3: {1, 3}, length = 4
    # path 1-4: {1, 3, 4}, length = 11


def make_graph2():
    graph = DiGraph()
    for i in range(5):
        graph.add_node(i + 1)
    graph.add_edge(Edge(1, 2, 10))
    graph.add_edge(Edge(1, 4, 30))
    graph.add_edge(Edge(1, 5, 100))
    graph.add_edge(Edge(2, 3, 50))
    graph.add_edge(Edge(3, 5, 10))
    graph.add_edge(Edge(4, 3, 20))
    graph.add_edge(Edge(4, 5, 60))

    return graph
    # source = 1
    # path 1-2: {1, 2}, length = 10
    # path 1-3: {1, 4, 3}, length = 50
    # path 1-4: {1, 4}, length = 30
    # path 1-5: {1, 4, 3, 5}, length = 60


def make_graph3():
    graph = DiGraph()
    for i in range(7):
        graph.add_node(i + 1)
    graph.add_edge(Edge(1, 5, 12))
    graph.add_edge(Edge(1, 2, 12))
    graph.add_edge(Edge(1, 6, 30))
    graph.add_edge(Edge(2, 3, 12))
    graph.add_edge(Edge(3, 4, 12))
    graph.add_edge(Edge(4, 7, 20))

    return graph
    # source = 1
    # path 1-2: {1, 2}, length = 12
    # path 1-3: {1, 2, 3}, length = 24
    # path 1-4: {1, 2, 3, 4}, length = 36
    # path 1-5: {1, 5}, length = 12
    # path 1-6: {1, 6}, length = 30
    # path 1-7: {1, 2, 3, 4, 7}, length = 56


def make_graph4():
    graph = DiGraph()
    for i in range(6):
        graph.add_node(i + 1)
    graph.add_edge(Edge(1, 2, 4))
    graph.add_edge(Edge(1, 3, 2))
    graph.add_edge(Edge(2, 3, 5))
    graph.add_edge(Edge(2, 4, 10))
    graph.add_edge(Edge(3, 5, 3))
    graph.add_edge(Edge(5, 4, 4))
    graph.add_edge(Edge(4, 6, 11))

    return graph
    # source = 1
    # path 1-2: {1, 2}, length = 4
    # path 1-3: {1, 3}, length = 2
    # path 1-4: {1, 3, 5, 4}, length = 9
    # path 1-5: {1, 3, 5}, length = 5
    # path 1-6: {1, 3, 5, 4, 6}, length = 20
