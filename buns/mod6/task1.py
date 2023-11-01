class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел


class LinkedList:
    """
    Основной класс
    """

    def __init__(self):
        self.head = None  # ссылка на начало очереди
        self.end = None
        self.current = None  # для next

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        if self.head is None:
            self.head = Node(val)

        else:
            new_Node = Node(val)
            if self.end is None:
                self.end = new_Node
                self.head.nref = self.end
            self.end.nref = new_Node
            self.end = new_Node

    def get(self, index):
        if index < 0: raise IndexError
        counter = 0
        current_node = self.head
        while counter != index:
            counter += 1
            if current_node.nref is None:
                raise IndexError
            current_node = current_node.nref

        return current_node.data

    def remove(self, index):
        if index < 0:
            raise IndexError
        if index == 0:
            self.head = self.head.nref
        counter = 0
        current_node = self.head
        previous_current = self.head
        while counter != index:
            counter += 1
            if current_node.nref is None:
                raise IndexError
            previous_current = current_node
            current_node = current_node.nref
        previous_current.nref = current_node.nref

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        current_node = self.head
        counter = 0
        if n - 1 < 0: raise IndexError
        while counter != n - 1:
            counter += 1
            current_node = current_node.nref
        new_node = Node(val)
        new_node.nref = current_node.nref
        current_node.nref = new_node

    def __next__(self):
        if self.current == -1:
            raise StopIteration
        if self.current is None:
            self.current = self.head
        while not (self.current.nref is None):
            result = self.current.data
            self.current = self.current.nref
            return result
        self.current = -1
        return self.end.data

    def __iter__(self):
        return self

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        current_node = self.head
        if current_node is None:
            print(None)
        else:
            values = []
            while current_node.nref is not None:
                values.append(current_node.data)
                current_node = current_node.nref
            values.append(current_node.data)
            print(values)


