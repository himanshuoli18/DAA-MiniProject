# Visualize the path in the maze.
def draw_maze(path):
    canvas.delete("all")
    cell_size = 40
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            x0, y0 = col * cell_size, row * cell_size
            x1, y1 = x0 + cell_size, y0 + cell_size
            if maze[row][col] == 1:
                canvas.create_rectangle(x0, y0, x1, y1, fill="black")
            if (row, col) in path:
                canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill="yellow")