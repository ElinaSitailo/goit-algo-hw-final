# Використовуючи код із task_4_heap_visualization_as_tree.py для побудови бінарного дерева,
# необхідно створити програму на Python,
# яка візуалізує обходи дерева: у глибину та в ширину.

# Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0).
# Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу.
# Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.

# Примітка. Використовуйте стек та чергу, НЕ рекурсію для реалізації обходів.

from collections import deque
import colorsys
import heapq
import random
import matplotlib.pyplot as plt
import networkx as nx
import task_4_heap_visualization_as_tree as tree_viz


H_GREEN = 0.33  # відтінок зеленого кольору в HSV
H_RED = 0.0  # відтінок червоного кольору в HSV


def get_shade(i, max_i, h):
    """Отримує відтінок кольору на основі індексу та максимального індексу."""
    
    s = 1.0  # повна насиченість
    v = 0.3 + 0.4 * (i / max_i)  # яскравість змінюється
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"


def bfs_with_colors(root):
    """Обхід дерева в ширину (BFS) з кольоровим відображенням."""

    if root is None:
        return

    graph = nx.DiGraph()
    pos = {root.id: (0, 0)}
    graph = tree_viz.add_edges(graph, root, pos)

    queue = deque([root])
    visited = set()
    order = 0
    total_nodes = sum(1 for _ in nx.nodes(graph))

    while queue:
        current_node = queue.popleft()
        if current_node.id in visited:
            continue

        visited.add(current_node.id)

        # Визначення кольору на основі порядку відвідування
        graph.nodes[current_node.id]["color"] = get_shade(order, total_nodes, H_GREEN)
        order += 1

        if current_node.left and current_node.left.id not in visited:
            queue.append(current_node.left)
        if current_node.right and current_node.right.id not in visited:
            queue.append(current_node.right)

    colors = [node[1]["color"] for node in graph.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title("BFS Tree Traversal Visualization")
    plt.show()


def dfs_with_colors(root):
    """Обхід дерева в глибину (DFS) з кольоровим відображенням."""

    if root is None:
        return

    graph = nx.DiGraph()
    pos = {root.id: (0, 0)}
    graph = tree_viz.add_edges(graph, root, pos)

    stack = [root]
    visited = set()
    order = 0
    total_nodes = sum(1 for _ in nx.nodes(graph))

    while stack:
        current_node = stack.pop()
        if current_node.id in visited:
            continue

        visited.add(current_node.id)

        # Визначення кольору на основі порядку відвідування
        graph.nodes[current_node.id]["color"] = get_shade(order, total_nodes, H_RED)
        order += 1

        if current_node.right and current_node.right.id not in visited:
            stack.append(current_node.right)
        if current_node.left and current_node.left.id not in visited:
            stack.append(current_node.left)

    colors = [node[1]["color"] for node in graph.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title("DFS Tree Traversal Visualization")
    plt.show()


if __name__ == "__main__":
    nums = [random.randint(0, 50) for _ in range(9)]
    print("random array:", nums)

    heapq.heapify(nums)
    print("array after heapify:", nums)

    root = tree_viz.build_tree(nums)

    print("Visualizing BFS Traversal:")
    bfs_with_colors(root)

    print("Visualizing DFS Traversal:")
    dfs_with_colors(root)
