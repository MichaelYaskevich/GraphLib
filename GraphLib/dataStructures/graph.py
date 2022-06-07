from GraphLib.dataStructures.edge import Edge


class Graph:
    def __init__(self):
        self.adjacency_lists = {}
        self.nodes_to_edge_dict = {}

    def get_nodes(self) -> list:
        return list(self.adjacency_lists.keys())

    def get_edges(self) -> list:
        return list(self.nodes_to_edge_dict.values())

    def get_adjacent_nodes(self, node) -> list:
        return self.adjacency_lists[node]

    def add_node(self, node) -> None:
        if node in self.adjacency_lists:
            raise ValueError("Graph already contains this node")
        self.adjacency_lists[node] = []

    def add_edge(self, edge: Edge) -> None:
        first_node, second_node = edge
        if (first_node not in self.adjacency_lists
                or second_node not in self.adjacency_lists):
            raise ValueError(
                "First_node or second_node aren't present in graph")

        if (first_node in self.adjacency_lists[second_node]
                or second_node in self.adjacency_lists[first_node]):
            raise ValueError("Graph already contains such edge")

        self.adjacency_lists[first_node].append(second_node)
        self.adjacency_lists[second_node].append(first_node)
        self.nodes_to_edge_dict[(first_node, second_node)] = edge
        self.nodes_to_edge_dict[(second_node, first_node)] = edge

    def delete_edge(self, edge: Edge) -> None:
        first_node, second_node = edge
        self.adjacency_lists[first_node].remove(second_node)
        self.adjacency_lists[first_node].remove(second_node)
        self.nodes_to_edge_dict.pop((first_node, second_node))
        self.nodes_to_edge_dict.pop((second_node, first_node))

    def get_incident_edge(self, first_node, second_node) -> Edge:
        return self.nodes_to_edge_dict[(first_node, second_node)]
