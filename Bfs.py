from collections import deque
def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # Initialize other variables
    visited = set()
    queue = deque([(start, [])])
    
    step_counter = 0  # Initialize step counter

    while queue:
        current_pos, path = queue.popleft()
        current_row, current_col = current_pos

        if current_pos == goal:
            return path + [current_pos], step_counter

        if current_pos not in visited:
            visited.add(current_pos)
            for dr, dc in directions:
                new_row, new_col = current_row + dr, current_col + dc

                if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 0:
                    new_pos = (new_row, new_col)
                    queue.append((new_pos, path + [current_pos]))
                    step_counter += 1  # Increment the step counter

    return [], step_counter
