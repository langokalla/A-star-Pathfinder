from queues import PriorityQueue

# TODO: fullfør a*, fungerer ikke. Blir ikke successful.


def heuristic(tile1, tile2):
    (x1, y1) = (tile1.r, tile1.c)
    (x2, y2) = (tile2.r, tile2.c)
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, start, end):
    current = end
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.append(start)  # optional
    path.reverse()  # optional
    return path


def a_star(start, end):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}
    success = False

    while not frontier.empty():
        current = frontier.pop()

        if current == end:
            print("WE MADE IT!! A********!!")
            success = True
            break

        for next_tile in current.neighbours:
            new_cost = cost_so_far[current] + next_tile.weight
            if next_tile not in cost_so_far or new_cost < cost_so_far[next_tile]:
                cost_so_far[next_tile] = new_cost
                priority = new_cost + heuristic(end, next_tile)
                frontier.put(next_tile, priority)
                came_from[next_tile] = current

        return came_from, cost_so_far, success
