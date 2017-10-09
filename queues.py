import collections
import heapq


class Queue:

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