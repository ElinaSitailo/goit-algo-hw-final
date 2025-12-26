# Наступний код виконує побудову бінарних дерев. Виконайте аналіз коду, щоб зрозуміти, як він працює.
# Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.
# Суть завдання полягає у створенні дерева із купи.


import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
import random


class Node:
    """Клас для представлення вузла бінарного дерева."""

    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Рекурсивно додає ребра до графа та позиції для візуалізації дерева."""

    if node is not None:

        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла

        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_node_x = x - 1 / 2**layer
            pos[node.left.id] = (left_node_x, y - 1)
            left_node_x = add_edges(graph, node.left, pos, x=left_node_x, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_node_x = x + 1 / 2**layer
            pos[node.right.id] = (right_node_x, y - 1)
            right_node_x = add_edges(graph, node.right, pos, x=right_node_x, y=y - 1, layer=layer + 1)

    return graph


def draw_tree(tree_root):
    """Візуалізує бінарне дерево за допомогою networkx та matplotlib."""

    graph = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}  # Початкова позиція кореня дерева

    graph = add_edges(graph, tree_root, pos)

    colors = [node[1]["color"] for node in graph.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in graph.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_tree(min_heap):
    """Будує бінарне дерево з бінарної купи."""

    if not min_heap:
        return None

    nodes = [Node(key) for key in min_heap]  # Створюємо вузли для кожного елемента купи
    nodes_count = len(nodes)

    for i, node in enumerate(nodes):

        # Визначаємо індекси лівого та правого дітей в масиві nodes
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index >= nodes_count and right_index >= nodes_count:
            break  # Якщо немає дітей, припиняємо цикл

        if left_index < nodes_count:
            node.left = nodes[left_index]
        if right_index < nodes_count:
            node.right = nodes[right_index]

    return nodes[0]  # Повертаємо корінь дерева


if __name__ == "__main__":

    nums = [random.randint(0, 50) for _ in range(9)]
    print("random array:", nums)

    heapq.heapify(nums)
    print("array after heapify:", nums)

    root = build_tree(nums)

    draw_tree(root)
