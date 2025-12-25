# Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі,
# використовуючи бінарну купу.
# Завдання включає створення графа,
# використання піраміди для оптимізації вибору вершин
# та обчислення найкоротших шляхів від початкової вершини до всіх інших.

import heapq
from typing import Dict, List, Tuple
import networkx as nx
import matplotlib.pyplot as plt

Graph = Dict[str, List[Tuple[str, int]]]


def dijkstra(graph: Graph, start: str) -> Dict[str, int]:
    """Find shortest paths from start node to all other nodes in the graph using Dijkstra's algorithm with a binary heap."""

    # Initialize distances with infinity
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # Priority queue/heap to hold nodes to explore
    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the distance is greater than the recorded distance, skip
        distance_to_current = distances[current_node]
        if current_distance > distance_to_current:
            continue

        # check neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def visualize_graph(graph_data: Graph) -> None:
    """Visualize the graph using networkx and matplotlib."""

    graph = nx.DiGraph()
    for node, edges in graph_data.items():
        for neighbor, weight in edges:
            graph.add_edge(node, neighbor, weight=weight)
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color="lightblue", node_size=1000, font_size=16)
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=12)
    plt.title("Graph Visualization")
    plt.show()


if __name__ == "__main__":

    START_NODE = "A"

    sample_graph = {
        START_NODE: [("B", 4), ("C", 1)],  # Edges from node A, where each tuple is (neighbor, edge_weight)
        "B": [("D", 1)],
        "C": [("B", 2), ("D", 5)],
        "D": [],
    }

    shortest_paths = dijkstra(sample_graph, START_NODE)
    print(f"Shortest paths from node {START_NODE}: {shortest_paths}")

    visualize_graph(sample_graph)

# RUN in env to visualize the graph
# python task_3_dijkstra_with_binary_heap.py
