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
