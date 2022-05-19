from GraphLib.dataStructures.edge import Edge


class DiGraph:
    def __init__(self):
        self.adjacency_lists = {}
        self.nodes_to_edge_dict = {}

    def get_nodes(self):
        return list(self.adjacency_lists.keys())

    def get_edges(self):
        return list(self.nodes_to_edge_dict.values())

    def get_adjacent_nodes(self, node):
        return self.adjacency_lists[node]

    def add_node(self, node):
        if node in self.adjacency_lists:
            raise ValueError("Graph already contains this node")
        self.adjacency_lists[node] = []

    def add_edge(self, edge: Edge):
        start, end = edge
        if start not in self.adjacency_lists or end not in self.adjacency_lists:
            raise ValueError("Start node or end node aren't present in adjacency list")

        if (start, end) in self.nodes_to_edge_dict:
            raise ValueError("Such edge already exists")

        self.adjacency_lists[start].append(end)
        self.nodes_to_edge_dict[(start, end)] = edge

    def get_incident_edge(self, start, end):
        return self.nodes_to_edge_dict[(start, end)]
