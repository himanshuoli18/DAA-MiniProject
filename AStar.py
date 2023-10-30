import heapq
def heuristic(node, goal):
    # Manhattan distance heuristic
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def astar(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # Initialize the cost matrix and priority queue for A*.
    cost = [[float('inf')] * cols for _ in range(rows)]
    cost[start[0]][start[1]] = 0
    priority_queue = [(heuristic(start, goal), 0, start)]

    step_counter = 0  # Initialize step counter
    while priority_queue:
        _, current_cost, (current_row, current_col) = heapq.heappop(priority_queue)

        if (current_row, current_col) == goal:
            break

        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc

            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 0:
                new_cost = current_cost + 1
                if new_cost < cost[new_row][new_col]:
                    cost[new_row][new_col] = new_cost
                    heapq.heappush(priority_queue, (new_cost + heuristic((new_row, new_col), goal), new_cost, (new_row, new_col)))
                    step_counter += 1  # Increment the step counter

    # Reconstruct the path from goal to start.
    path = []
    row, col = goal
    while (row, col) != start:
        path.append((row, col))
        for dr, dc in directions:
            new_row, new_col = row - dr, col - dc
            if 0 <= new_row < rows and 0 <= new_col < cols and cost[new_row][new_col] < cost[row][col]:
                row, col = new_row, new_col
                break
    path.append(start)
    path.reverse()
    return path, step_counter

