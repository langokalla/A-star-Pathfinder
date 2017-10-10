from queues import Queue


def bfs(start, end):
    """
    Breadth first search. Takes a start tile and end tile, and uses
    their neighbour list to traverse.
    Uses the LIFO queue in queues.py.
    :param start: Tile
    :param end: Tile
    :return: came_from, dictionary with all tiles, and where we came from (parent).
             success, True or False. If the algorithm found the end tile or not.
             has_been_next, list over tiles that has been considered as the next tile.
    """
    frontier = Queue()
    frontier.add(start)
    came_from = {start: None}
    success = False
    has_been_next = []

    while not frontier.empty():
        current = frontier.pop()
        current.visit()
        if current == end:
            print("Breadth First Search, successful.")
            success = True
            break

        for next_tile in current.neighbours:
            if next_tile not in has_been_next:
                has_been_next.append(next_tile)
            if next_tile not in came_from:
                frontier.add(next_tile)
                came_from[next_tile] = current

    return came_from, success, has_been_next
