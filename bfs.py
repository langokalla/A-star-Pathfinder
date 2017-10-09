from queues import Queue


def bfs(start, end):
    frontier = Queue()
    frontier.add(start)
    came_from = {start: None}
    success = False

    while not frontier.empty():
        current = frontier.pop()
        current.visit()
        if current == end:
            print("WE MADE IT!!!")
            success = True
            break

        for next_tile in current.neighbours:
            if next_tile not in came_from:
                frontier.add(next_tile)
                came_from[next_tile] = current

    return came_from, success
