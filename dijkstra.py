from queues import PriorityQueue


def dijkstra(start, end):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}
    success = False

    while not frontier.empty():
        current = frontier.pop()
        if current == end:
            print("WE MADE IT!!!1!1! DICKSTRA FTW")
            success = True
            break

        for next_tile in current.neighbours:
            new_cost = cost_so_far[current] + next_tile.weight
            if next_tile not in cost_so_far or new_cost < cost_so_far[next_tile]:
                cost_so_far[next_tile] = new_cost
                priority = new_cost
                frontier.put(next_tile, priority)
                came_from[next_tile] = current
    return came_from, cost_so_far, success
