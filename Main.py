from pyamaze import maze
from AStar import *
from Dijkstra import *
from Bfs import *

print("Maze Solver")
while(True):
    choice1 = int(input("Which Algo you want to use :\nPress : 1 - A Star Algorithm\n\t2 - Breadth First Search Algorithm\n\t3 - Dijkstra Algorithm\nChoice : "))
    if(choice1 == 1):
        aStar_fcall()
    elif(choice1 == 2):
        bfs_fcall()
    elif(choice1 == 3):
        dijkstra_fcall()
    else:
        print("Invalid Choice.")
    choice2 = int(input("Do you want to continue?\nPress : 1 - Yes\n\t0 - No\nChoice : "))
    if (choice2 == 1):
        pass
    else:
        print("Thank You")
        quit()
