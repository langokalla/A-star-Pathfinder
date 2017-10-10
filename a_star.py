from queues import PriorityQueue


def heuristic(tile1, tile2):
    """
    Manhattan distance between two tiles.
    :param tile1: Tile
    :param tile2: Tile
    :return: int distance
    """
    (x1, y1) = (tile1.r, tile1.c)
    (x2, y2) = (tile2.r, tile2.c)
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, start, end):
    """
    Reconstructs the came_from dictionary to be a list of tiles
    we can traverse and draw later.
    :param came_from: dictionary
    :param start: Tile
    :param end: Tile
    :return: List path
    """
    current = end
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.append(start)  # optional
    path.reverse()      # optional
    return path


def a_star(start, end):
    """
    A* Pathfinding algorithm. Takes a start tile and end tile, and uses
    their neighbour list to traverse.
    Uses the heapq queue in queues.py.
    :param start: Tile
    :param end: Tile
    :return: came_from, dictionary with all tiles as key, and where we came from (parent tile) as value.
             cost_so_far, dictionary with tiles as key, and their cost so far as value.
             success, True or False. If the algorithm found the end tile or not.
             has_been_next, list over tiles that has been considered as the next tile.
    """
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}
    has_been_next = []
    success = False

    while not frontier.empty():
        current = frontier.pop()
        current.visit()

        if current == end:
            print("A* Pathfinder, successful.")
            success = True
            break

        for next_tile in current.neighbours:

            if next_tile not in has_been_next:
                has_been_next.append(next_tile)

            new_cost = cost_so_far[current] + next_tile.weight
            if next_tile not in cost_so_far or new_cost < cost_so_far[next_tile]:
                cost_so_far[next_tile] = new_cost
                priority = new_cost + heuristic(end, next_tile)
                frontier.put(next_tile, priority)
                came_from[next_tile] = current

    return came_from, cost_so_far, success, has_been_next
