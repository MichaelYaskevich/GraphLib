from GraphLib.dataStructures.di_graph import DiGraph
from GraphLib.dataStructures.edge import Edge


def read_weight_matrix(lines):
    graph = DiGraph()
    source = int(lines[-2]) - 1
    destination = int(lines[-1]) - 1
    matrix_lines = lines[1:-2]

    for i, line in enumerate(matrix_lines):
        graph.add_node(i)
    for i, line in enumerate(matrix_lines):
        for j, value in enumerate(line.split()):
            if value == '-':
                continue
            val = int(value)
            if val != 0:
                graph.add_edge(Edge(i, j, val))

    return graph, source, destination
