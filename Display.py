# Visualize the path in the maze.
def display(maze,start,goal,path):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (row, col) == start:
                print("S", end=" ")
            elif (row, col) == goal:
                print("G", end=" ")
            elif (row, col) in path:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()