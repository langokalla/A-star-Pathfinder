import collections
import heapq


class PriorityQueue:

    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __len__(self):
        return len(self.elements)


class Queue:

    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()

    def __len__(self):
        return len(self.elements)


def bfs(start, end):
    frontier = Queue()
    frontier.put(start)
    came_from = {start: None}

    while not frontier.empty():
        current = frontier.get()
        current.visit()
        if current == end:
            print("WE MADE IT!!!")

        for next_tile in current.neighbours:
            if next_tile not in came_from:
                frontier.put(next_tile)
                came_from[next_tile] = current

    return came_from
