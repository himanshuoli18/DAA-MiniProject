import heapq
def dijkstra(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # Initialize the distance matrix with infinity for all cells.
    distance = [[float('inf')] * cols for _ in range(rows)]
    distance[start[0]][start[1]] = 0

    # Priority queue for selecting cells with the smallest distance.
    priority_queue = [(0, start)]
    
    step_counter = 0  # Initialize step counter
    while priority_queue:
        current_dist, (current_row, current_col) = heapq.heappop(priority_queue)

        if (current_row, current_col) == goal:
            break

        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc

            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 0:
                new_dist = distance[current_row][current_col] + 1
                if new_dist < distance[new_row][new_col]:
                    distance[new_row][new_col] = new_dist
                    heapq.heappush(priority_queue, (new_dist, (new_row, new_col)))
                    step_counter += 1  # Increment the step counter

    # Reconstruct the path from goal to start.
    path = []
    row, col = goal
    while (row, col) != start:
        path.append((row, col))
        for dr, dc in directions:
            new_row, new_col = row - dr, col - dc
            if 0 <= new_row < rows and 0 <= new_col < cols and distance[new_row][new_col] < distance[row][col]:
                row, col = new_row, new_col
                break
    path.append(start)
    path.reverse()
    return path, step_counter

    
