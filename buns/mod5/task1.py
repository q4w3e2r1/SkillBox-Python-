class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.current_Node = Node(None)
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        val = self.current_Node.data
        self.current_Node = self.current_Node.pref
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        if self.current_Node.data is None:
            self.current_Node.data = val
        else:
            new_Node = Node(val)
            new_Node.pref = self.current_Node
            self.current_Node = new_Node

    def print(self):
        """
        вывод на печать содержимого стека
        """
        current_node = self.current_Node
        values = []
        while current_node.pref is not None:
            values.append(current_node.data)
            current_node = current_node.pref
        values.append(current_node.data)
        print(values[::-1])

