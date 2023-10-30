from Dijkstra import *
from AStar import *
from Bfs import *
from Display import *
# Define the maze as a 2D grid where 0 represents open paths, and 1 represents walls.
maze = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)
while (True):
    choice1 = int(input("Using which algorithm you want to excel :\nPress : 1 - Dijkstra\n\t2 - A Star\n\t3 - Best First Search\nChoice : "))
    if (choice1==1):
        path, steps_counter = dijkstra(maze, start, goal)
        display(maze,start,goal,path)
        print(f"Dijkstra's Algorithm took {steps_counter} steps to find the path.")
    elif (choice1==2):
        path, steps_counter = astar(maze, start, goal)
        display(maze,start,goal,path)
        print(f"A Star Algorithm took {steps_counter} steps to find the path.")
    elif(choice1==3):
        path, steps_counter = bfs(maze, start, goal)
        display(maze,start,goal,path)
        print(f"BFS Algorithm took {steps_counter} steps to find the path.")
    else:
        print("Invalid Choice")

    choice2 = int(input("Do you want to continue :\nPress : 1 - Yes\n\t0 - No\nChoice : "))
    if(choice2==1):
        pass
    else:
        print("Thank You")
        quit()