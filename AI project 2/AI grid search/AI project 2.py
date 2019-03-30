from heapq import *
import math
import collections
import numpy as np
def bfs(grid,rows,columns,rstart,cstart,rend,cend):
    queue = collections.deque([[(rstart,cstart)]])
    closedset = set([(rstart,cstart)])

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if x==rend and y==cend:
            return path
        for x2, y2 in ((x,y+1), (x-1,y), (x+1,y), (x,y-1)):
            if 0 <= x2 < rows and 0 <= y2 < columns and grid[x2][y2] != 0 and (x2, y2) not in closedset:
                queue.append(path + [(x2, y2)])
                closedset.add((x2, y2))


def dfs(grid,rows,columns,rstart,cstart,rend,cend):
    stack = [[(rstart,cstart)]]
    closedset = set([(rstart,cstart)])
    while stack:
        path = stack.pop()
        x, y = path[-1]
        if x==rend and y==cend:
            return path
        for x2, y2 in ((x,y-1), (x,y+1), (x-1,y), (x+1,y)):
            if 0 <= x2 < rows and 0 <= y2 < columns and grid[x2][y2] != 0 and (x2, y2) not in closedset:
                stack.append(path + [(x2, y2)])
                closedset.add((x2, y2))

def euclideanheuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
def manhattanheuristic(a,b):
    return abs(b[0] - a[0])+abs(b[1] - a[1])
def zeroheuristic(a,b):
    return 0
def astar(grid,rows,columns,rstart,cstart,rend,cend):
    close_set = set()
    came_from = {}
    gscore = {(rstart,cstart): 0}
    fscore = {(rstart,cstart): euclideanheuristic((rstart,cstart), (rend,cend))}
    openset = []
    heappush(openset, (fscore[(rstart,cstart)], (rstart,cstart)))
    while len(openset)!=0:
        current = heappop(openset)[1]
        if current == (rend,cend):
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        close_set.add(current)
        x=current[0]
        y=current[1]
        for x2, y2 in ((x,y-1), (x,y+1), (x-1,y), (x+1,y)):
            if 0 <= x2 < rows and 0 <= y2 < columns and grid[x2][y2] != 0:
               tentative_gscore = gscore[current] + 1 /(grid[x][y]*grid[x2][y2])
            else:
                continue
            if (x2,y2) in close_set and tentative_gscore >= gscore.get((x2,y2), 0):
                continue
            if tentative_gscore < gscore.get((x2,y2), 0) or (x2,y2) not in [i[1] for i in openset]:
                came_from[(x2,y2)] = current
                gscore[(x2,y2)] = tentative_gscore
                fscore[(x2,y2)] = tentative_gscore + euclideanheuristic((x2,y2), (rend,cend))
                heappush(openset, (fscore[(x2,y2)], (x2,y2)))
    return False
class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
       return self.position == other.position
def fringesearch(grid,rows,columns,rstart,cstart,rend,cend):
    F = []
    start_node = Node(None, (rstart, cstart))
    end_node = Node(None, (rend, cend))
    start_node.g=0
    flimit= abs(start_node.position[0] - end_node.position[0])+abs(start_node.position[1] - end_node.position[1])
    found = False
    closedset = set([(rstart, cstart)])
    F.append(start_node)
    while (found== False) and len(F)>0:
        fmin = math.inf
        for node in F:
            g = node.g
            node.h=abs(node.position[0] - end_node.position[0])+abs(node.position[1] - end_node.position[1])
            f= g + node.h

            if f > flimit:
                fmin = min(f,fmin)
                continue
            if node.position[0]==rend and node.position[1]==cend:
                found = True
                break
            x = node.position[0]
            y = node.position[1]
            children = []
            for x2, y2 in ((x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)):
                if 0 <= x2 < rows and 0 <= y2 < columns and grid[x2][y2] != 0 and (x2, y2) not in closedset:
                    new_node = Node(node, (x2, y2))
                    children.append(new_node)
                    closedset.add((x2, y2))
            for child in children:
                g_child = g + 1/(grid[x][y]*grid[child.position[0]][child.position[1]])
                if (Node(node,(child.position[0], child.position[1])) != Node(None,(child.position[0], child.position[1]))):
                    g_cache = child.g
                    if g_child >= g_cache:
                        continue
                if child in F:
                    F.remove(child)

                F.append(child)
                child.g= g_child
            F.remove(node)
        flimit = fmin
    if found == True:
        path = []
        current = node
        while current is not None:
            path.append(current.position)
            current = current.parent
        return  path[::-1]  # Return reversed path
def main():
    grid = np.loadtxt("grid.txt", skiprows=1)
    np.seterr(divide='ignore', invalid='ignore')



    #np.seterr(divide='ignore', invalid='ignore')
    path1=bfs(grid,102,119,0,0,100,100)
    print(path1)
    np.savetxt('path of bfs method.txt', path1,fmt='%d')  # x,y,z equal sized 1D arrays
    path2=dfs(grid,102,119,0,0,100,100)
    print(path2)
    np.savetxt('path of dfs method.txt', path2, fmt='%d')  # x,y,z equal siz
    path3 = astar(1/grid, 102, 119, 0, 0, 100, 100)
    print(path3)
    #np.savetxt('path of astar method with manhattan heuristic.txt', path3, fmt='%d')
    np.savetxt('path of astar method with euclidean heuristic.txt', path3, fmt='%d')
    #np.savetxt('path of astar method with zero heuristic.txt', path3, fmt='%d')
    path4 = fringesearch(grid, 102, 119, 0, 0, 100, 100)
    print(path4)
    np.savetxt('path of fringe search method with Manhattan heuristic.txt', path4, fmt='%d')
if __name__ == '__main__':
    main()
