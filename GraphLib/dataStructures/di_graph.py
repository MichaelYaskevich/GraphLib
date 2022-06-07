import queue

from GraphLib.dataStructures.edge import Edge
from GraphLib.dataStructures.graph import Graph


class DiGraph(Graph):
    def __init__(self):
        super().__init__()

    def add_edge(self, edge: Edge) -> None:
        start, end = edge
        if (start not in self.adjacency_lists
                or end not in self.adjacency_lists):
            raise ValueError(
                "Start node or end node aren't present in adjacency list")

        if (start, end) in self.nodes_to_edge_dict:
            raise ValueError("Such edge already exists")

        self.adjacency_lists[start].append(end)
        self.nodes_to_edge_dict[(start, end)] = edge

    def delete_edge(self, edge: Edge) -> None:
        start, end = edge
        self.adjacency_lists[start].remove(end)
        self.nodes_to_edge_dict.pop((start, end))


def is_cyclic(graph: Graph):
    path = set()
    visited = set()

    def visit(node):
        if node in visited:
            return False
        visited.add(node)
        path.add(node)
        for neighbour in graph.get_adjacent_nodes(node):
            if neighbour in path or visit(neighbour):
                return True
        path.remove(node)
        return False

    return any(visit(v) for v in graph.get_nodes())
