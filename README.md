# Grid-Search-on-a-Costmap
Given a grid, where certain cells are marked as obstacles, the objective is to find a path from an initial to a
goal cell that avoids collisions with the obstacles. More specifically, each grid cell will have a numeric value
in the range [0,1]. A value of 0 indicates that the cell is an obstacle, which must always be avoided. A value
of 1 indicates that the cell is free. 

![grayscale image note](https://github.com/chinhtranvan/Grid-Search-on-a-Costmap/blob/master/AI%20grid%20search/SupportCode/grayscale%20image.png)

In this way, obstacle cells have a cost of ∞, while free cells have a cost of 1. Note that the cost increases as
the value of the cell gets closer to 0.
The method name is as follows: DFS for depth-first search, BFS for breadth-first search, AStarZero
for A*-search with the zero heuristic, AStarEuclidean for A*-search with the Euclidean heuristic,
AStarManhattan for A*-search with the Manhattan heuristic.
The program should read the file grid.txt and search for a solution from (rstart,cstart) to
(rend,cend). It should then write the solution to the file path.txt. The moves are LEFT, RIGHT,
UP, DOWN (no diagonal moves allowed).
Note that DFS and BFS treat the cells with value (> 0) as free cells since these methods just focus on
computing a path. Essentially, these methods ignore the cost.
A* should take the cell-traversal costs into account so that it can find the shortest path to the goal.
The cost of passing through a cell (i, j) should be computed as
cost(i, j) = 1/val(i, j).


Result
![breadth first search](https://github.com/chinhtranvan/Grid-Search-on-a-Costmap/blob/master/AI%20grid%20search/result/figure%20of%20BFS.PNG)

![Depth first search](https://github.com/chinhtranvan/Grid-Search-on-a-Costmap/blob/master/AI%20grid%20search/result/figure%20of%20DFS.PNG)

