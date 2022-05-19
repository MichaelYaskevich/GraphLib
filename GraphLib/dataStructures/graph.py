from GraphLib.dataStructures.edge import Edge


class Graph:
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
        first_node, second_node = edge
        if first_node not in self.adjacency_lists or second_node not in self.adjacency_lists:
            raise ValueError("First_node or second_node aren't present in graph")

        if first_node in self.adjacency_lists[second_node] or second_node in self.adjacency_lists[first_node]:
            raise ValueError("Graph already contains such edge")

        self.adjacency_lists[first_node].append(second_node)
        self.adjacency_lists[second_node].append(first_node)
        self.nodes_to_edge_dict[(first_node, second_node)] = edge
        self.nodes_to_edge_dict[(second_node, first_node)] = edge

    def get_incident_edge(self, start_node, end_node):
        return self.nodes_to_edge_dict[(start_node, end_node)]
