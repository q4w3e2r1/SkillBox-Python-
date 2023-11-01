class DoubleElement:
    def __init__(self, *lst):
        self.list = list(lst)
        self.current = 0

    def __next__(self):
        while self.current < len(self.list) - 1:
            result = (self.list[self.current], self.list[self.current+1])
            self.current += 2
            return result
        if self.current == len(self.list) - 1:
            result = (self.list[self.current], None)
            self.current += 2
            return result
        raise StopIteration

    def __iter__(self):
        return self
