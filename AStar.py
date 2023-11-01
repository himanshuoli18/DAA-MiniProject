from queue import PriorityQueue
from pyamaze import maze, agent, textLabel, COLOR
def aStar_fcall():
    row = int(input("Enter number of rows : "))
    column = int(input("Enter number of columns : "))
    m = maze(row,column)
    m.CreateMaze()

    searchPath,aPath,fwdPath=aStar(m)
    a=agent(m,footprints=True,color=COLOR.blue,filled=True)
    b=agent(m,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(m.rows,m.cols))
    c=agent(m,footprints=True,color=COLOR.red)

    m.tracePath({a:searchPath},delay=200)
    m.tracePath({b:aPath},delay=200)
    m.tracePath({c:fwdPath},delay=200)

    l=textLabel(m,'A Star Path Length',len(fwdPath)+1)
    l=textLabel(m,'A Star Search Length',len(searchPath))
    m.run()

def heuristic(cell1, cell2):
    # Manhattan distance heuristic
    return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

def aStar(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    open = PriorityQueue()
    open.put((heuristic(start, m._goal), heuristic(start, m._goal), start))
    aPath = {}
    g_score = {row: float("inf") for row in m.grid}
    g_score[start] = 0
    f_score = {row: float("inf") for row in m.grid}
    f_score[start] = heuristic(start, m._goal)
    searchPath=[start]
    while not open.empty():
        currCell = open.get()[2]
        searchPath.append(currCell)
        if currCell == m._goal:
            break        
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + heuristic(childCell, m._goal)


                if temp_f_score < f_score[childCell]:   
                    aPath[childCell] = currCell
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_g_score + heuristic(childCell, m._goal)
                    open.put((f_score[childCell], heuristic(childCell, m._goal), childCell))
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return searchPath,aPath,fwdPath
