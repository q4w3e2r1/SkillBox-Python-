class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if self.start is None:
            raise Exception
        val = self.start.data
        self.start = self.start.nref
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        if self.start is None:
            self.start = Node(None)
            self.start.data = val

        else:
            new_Node = Node(val)
            if self.end is None:
                self.end = new_Node
                self.end.pref = self.start
                self.start.nref = self.end
            new_Node.pref = self.end
            self.end.nref = new_Node
            self.end = new_Node

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        current_Node = self.start
        counter = 0
        while counter != n-1:
            counter += 1
            current_Node = current_Node.nref
        new_Node = Node(val)
        new_Node.pref = current_Node
        new_Node.nref = current_Node.nref

        current_Node.nref.pref = new_Node
        current_Node.nref = new_Node



    def print(self):
        """
        вывод на печать содержимого очереди
        """
        current_node = self.start
        if current_node is None:
            print(None)
        else:
            values = []
            while current_node.nref is not None:
                values.append(current_node.data)
                current_node = current_node.nref
            values.append(current_node.data)
            print(values)
