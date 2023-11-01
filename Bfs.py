from collections import deque
from pyamaze import maze,agent,COLOR,textLabel

def bfs_fcall():
    row = int(input("Enter number of rows : "))
    column = int(input("Enter number of columns : "))
    m = maze(row,column)
    m.CreateMaze(loopPercent=10)
    bSearch,bfsPath,fwdPath=bfs(m)
    a=agent(m,footprints=True,color=COLOR.blue,shape='square',filled=True)
    b=agent(m,footprints=True,color=COLOR.red,shape='square',filled=False)
    c=agent(m,1,1,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols))
    m.tracePath({a:bSearch},delay=200)
    m.tracePath({c:bfsPath},delay=200)
    m.tracePath({b:fwdPath},delay=200)
    m.run()

def bfs(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    frontier = deque()
    frontier.append(start)
    bfsPath = {}
    explored = [start]
    bSearch=[]

    while len(frontier)>0:
        currCell=frontier.popleft()
        if currCell==m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
                bSearch.append(childCell)
    # print(f'{bfsPath}')
    fwdPath={}
    cell=m._goal
    while cell!=(m.rows,m.cols):
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return bSearch,bfsPath,fwdPath
