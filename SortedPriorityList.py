from priority_queue_base import PriorityQueueBase
from positional_list import PositionalList


class SortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        if self.is_empty():
            raise Empty('Priority Queue is Empty.')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority Queue is Empty.')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)

if __name__ == '__main__':
    p = SortedPriorityQueue()
    p.add(1, 5)
    p.add(4, 1)
    p.add(2, 7)
    p.add(3, 4)
    print(p.remove_min())
    print(p.remove_min())
    print(p.remove_min())
    print(p.remove_min())