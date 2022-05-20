from GraphLib.dataStructures.di_graph import DiGraph
from GraphLib.dataStructures.edge import Edge
from GraphLib.dataStructures.graph import Graph


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
    for i in range(0, 8):
        graph.add_node(i)
    graph.add_edge(Edge(0, 1, 1))
    graph.add_edge(Edge(0, 2, 2))
    graph.add_edge(Edge(0, 3, 5))
    graph.add_edge(Edge(2, 5, 5))
    graph.add_edge(Edge(3, 6, 2))
    graph.add_edge(Edge(1, 5, 11))
    graph.add_edge(Edge(2, 4, 9))
    graph.add_edge(Edge(2, 6, 16))
    graph.add_edge(Edge(4, 7, 18))
    graph.add_edge(Edge(5, 7, 13))
    graph.add_edge(Edge(6, 7, 2))

    return graph
    # source = 0
    # path 0-1: {0, 1}, length = 1
    # path 0-2: {0, 2}, length = 2
    # path 0-3: {0, 3}, length = 5
    # path 0-4: {0, 1, 4}, length = 5
    # path 0-5: {0, 2, 5}, length = 7
    # path 0-6: {0, 3, 6}, length = 7
    # path 0-7: {0, 3, 6, 7}, length = 9


def make_graph4():
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


def make_graph5():
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
