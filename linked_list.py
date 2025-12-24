class Node:
    """Клас для представлення вузла зв'язного списку"""

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """Клас для представлення зв'язного списку"""

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Вставка нового вузла на початок списку"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Вставка нового вузла в кінець списку"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        """Вставка нового вузла після заданого вузла"""
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        """Видалення вузла за заданим ключем"""
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        """Пошук елемента за значенням"""
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse_list(self):
        """Реверсування зв'язного списку"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node
        self.head = prev

    def sort_list(self):
        """сортування вставками зв'язного списку"""
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            if sorted_list is None or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                sorted_current = sorted_list
                while sorted_current.next is not None and sorted_current.next.data < current.data:
                    sorted_current = sorted_current.next
                current.next = sorted_current.next
                sorted_current.next = current
            current = next_node
        self.head = sorted_list

    def merge_sorted(self, other_list):
        """Злиття двох відсортованих зв'язних списків"""
        dummy = Node()
        tail = dummy
        l1 = self.head
        l2 = other_list.head

        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        self.head = dummy.next

    def print_list(self):
        """Виведення всіх елементів списку"""
        current = self.head
        while current:
            print(current.data)
            current = current.next


if __name__ == "__main__":

    linked_list = LinkedList()

    linked_list.insert_at_beginning(5)
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(15)
    print("Зв'язний список після вставки на початок 5, 10, 15:")
    linked_list.print_list()

    linked_list.insert_at_end(20)
    linked_list.insert_at_end(25)
    print("\nЗв'язний список після вставки в кінець 20, 25:")
    linked_list.print_list()

    linked_list.delete_node(10)
    print("\nЗв'язний список після видалення вузла 10:")
    linked_list.print_list()

    linked_list.reverse_list()
    print("\nЗв'язний список після реверсування:")
    linked_list.print_list()

    linked_list.sort_list()
    print("\nВідсортований зв'язний список:")
    linked_list.print_list()

    other_list = LinkedList()
    other_list.insert_at_end(3)
    other_list.insert_at_end(7)
    other_list.insert_at_end(24)
    other_list.insert_at_end(24)
    other_list.insert_at_end(31)
    other_list.sort_list()

    linked_list.merge_sorted(other_list)
    print("\nЗлитий відсортований зв'язний список:")
    linked_list.print_list()
