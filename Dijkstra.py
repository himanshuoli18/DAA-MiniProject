from pyamaze import maze,agent,COLOR,textLabel

def dijkstra_fcall():
    row = int(input("Enter number of rows : "))
    column = int(input("Enter number of columns : "))
    m = maze(row,column)
    m.CreateMaze(loopPercent=100)

    h1=agent(m,2,3,color=COLOR.red)
    h2=agent(m,1,4,color=COLOR.red)
    h3=agent(m,4,4,color=COLOR.red)
    h4=agent(m,5,1,color=COLOR.red)
    h5=agent(m,3,1,color=COLOR.red)


    h1.cost=100
    h2.cost=100
    h3.cost=100
    h4.cost=100
    h5.cost=100

    path,cost =dijkstra(m,h1,h2,h3,h4,h5)
    textLabel(m,'Total Cost',cost)
    a=agent(m,footprints=True,color=COLOR.blue,filled=True)
    b=agent(m,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(m.rows,m.cols))
    c=agent(m,footprints=True,color=COLOR.red)

    a=agent(m,color=COLOR.cyan,filled=True,footprints=True)
    m.tracePath({a:path})
    m.run()

def dijkstra(m,*h,start=None):
    if start is None:
        start=(m.rows,m.cols)

    hurdles=[(i.position,i.cost) for i in h]

    unvisited={n:float('inf') for n in m.grid}
    unvisited[start]=0
    visited={}
    revPath={}
    while unvisited:
        currCell=min(unvisited,key=unvisited.get)
        visited[currCell]=unvisited[currCell]
        if currCell==m._goal:
            break
        for d in 'EWNS':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in visited:
                    continue
                tempDist= unvisited[currCell]+1
                for hurdle in hurdles:
                    if hurdle[0]==currCell:
                        tempDist+=hurdle[1]

                if tempDist < unvisited[childCell]:
                    unvisited[childCell]=tempDist
                    revPath[childCell]=currCell
        unvisited.pop(currCell)
    
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]
    
    return fwdPath,visited[m._goal]