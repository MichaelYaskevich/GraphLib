from GraphLib.dataStructures.di_graph import DiGraph
from GraphLib.dataStructures.edge import Edge


def read_weight_matrix(lines):
    graph = DiGraph()
    source = lines[-2].strip()
    destination = lines[-1].strip()
    matrix_lines = lines[1:-2]

    for i, line in enumerate(matrix_lines):
        graph.add_node(str(i))
    for i, line in enumerate(matrix_lines):
        for j, value in enumerate(line.split()):
            if value == '-':
                continue
            val = int(value)
            if val != 0:
                graph.add_edge(Edge(str(i), str(j), val))

    return graph, source, destination
