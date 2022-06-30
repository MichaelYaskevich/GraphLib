import matplotlib.pyplot as plt
import networkx as nx

from graph_library.data_structures import Graph


class GraphVisualization:

    def __init__(self):
        self.visual = []

    def add_edge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self):
        graph = nx.DiGraph()
        graph.add_edges_from(self.visual)
        nx.draw_networkx(graph)
        plt.show()


def visualize_graph(graph: Graph, result):
    edges = graph.get_edges()
    source, destination = result[0]
    full_path = result[1]
    path = set()
    nodes_in_path = set(full_path)
    labels = {}

    # if is_ok:
    #     for i in range(len(full_path) - 1):
    #         path.add((full_path[i], full_path[i + 1]))

    visualization = nx.DiGraph()

    for edge in edges:
        labels[(edge.first_node, edge.second_node)] = edge.weight
        if (edge.first_node, edge.second_node) in path:
            visualization.add_edge(edge.first_node,
                                   edge.second_node,
                                   weight=3,
                                   color='g')
        else:
            visualization.add_edge(edge.first_node,
                                   edge.second_node,
                                   weight=1,
                                   color='black')

    color_map = [
        'green' if node in nodes_in_path
        else 'orange'
        for node in visualization]

    colors = nx.get_edge_attributes(visualization, 'color').values()
    weights = nx.get_edge_attributes(visualization, 'weight').values()
    pos = nx.spring_layout(visualization)
    nx.draw_networkx(visualization,
                     pos=pos,
                     edge_color=colors,
                     width=list(weights),
                     node_color=color_map)
    nx.draw_networkx_edge_labels(visualization,
                                 pos=pos,
                                 edge_labels=labels,
                                 font_size=12)
    plt.show()


def main():
    from src.generator.generator import generate_random_graph
    graph = generate_random_graph(20, 0, 1000)
    visualize_graph()


if __name__ == '__main__':
    main()
