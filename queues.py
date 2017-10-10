import collections
import heapq


class Queue:

    """
    Last in first out queue. Implemented as a collections.deque (deck / stack).
    Used for BFS.
    """

    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def add(self, x):
        self.elements.append(x)

    def pop(self):
        return self.elements.popleft()

    def __len__(self):
        return len(self.elements)


class PriorityQueue:

    """
    Priority queue. Implemented as a heapq from collections.
    Used in Dijkstra and A*.
    """

    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        return heapq.heappop(self.elements)[1]

    def __len__(self):
        return len(self.elements)
