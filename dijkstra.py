from queues import PriorityQueue


def dijkstra(start, end):
    """
    Dijkstra's algorithm. Takes a start tile and end tile, and uses
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
            print("Dijkstra's algorithm, successful.")
            success = True
            break

        for next_tile in current.neighbours:
            if next_tile not in has_been_next:
                has_been_next.append(next_tile)
            new_cost = cost_so_far[current] + next_tile.weight
            if next_tile not in cost_so_far or new_cost < cost_so_far[next_tile]:
                cost_so_far[next_tile] = new_cost
                priority = new_cost
                frontier.put(next_tile, priority)
                came_from[next_tile] = current

    return came_from, cost_so_far, success, has_been_next
