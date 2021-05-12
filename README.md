# Python Sudoku solver

 The algorithms was made in Python3 and can be executed with followed command:
    
    
    python sudoku bfs|dfs|astar|ac3|back <filename.txt>
    python sudoku bfs|dfs|astar|ac3|back < input.txt
    
 *Just one algorithm at a time:
 
    python sudoku astar input.txt
 
 The text must have the format below:
 
    
    .......2143.......6........2.15..........637...........68...4.....23........7....
    .......241..8.............3...4..5..7.....1......3.......51.6....2....5..3...7...
    
    
 The output will be with the format below (solved, I hope :)):
 
    
    857349621432861597619752843271583964945126378386497215768915432194238756523674189
    867351924143829765295746813318472596724695138956138247489513672672984351531267489
    

__Breadth-first search algorithm__
  - Function _solveBFS(board)_: The BFS algorithm list all options for a specific cell then go to next blank, if the next cell don't have a solution the function return to last recursion instance and try the next possibility.

		For example:
    
    ```
    |0..|...|.21|
    |43.|...|...|
    |6..|...|...|
    |---+---+---|
    |2.1|5..|...|
    |...|..6|37.|
    |...|...|...|
    |---+---+---|
    |.68|...|4..|
    |...|23.|...|
    |...|.7.|...|
    ```  
    
	First cell in the above board is [0,0] (top, left), we have the options [5,6,7] stored in a list of solutions in the current instance, in the next instance we have the board below:

    
    ```
    |50.|...|.21|
    |43.|...|...|
    |6..|...|...|
    |---+---+---|
    |2.1|5..|...|
    |...|..6|37.|
    |...|...|...|
    |---+---+---|
    |.68|...|4..|
    |...|23.|...|
    |...|.7.|...|
    ```
    
	With the cell [0,1] we have the options [7,8,9], if the list of options is empty the function will return to the last recursion instance and will try the next option of the last generated list of options, until find the board solution.


__Depth-first search algorithm__
  - Function _solveDFS(board)_: The DFS algorithm takes the first option for the current cell and moves to the next cell, unlike BFS, DFS does not generate all possibilities before going to the next cell. Follow the example below:

    ```
    |0..|...|.21|
    |43.|...|...|
    |6..|...|...|
    |---+---+---|
    |2.1|5..|...|
    |...|..6|37.|
    |...|...|...|
    |---+---+---|
    |.68|...|4..|
    |...|23.|...|
    |...|.7.|...|
    ```
    
	The first valid option to cell [0,0] is 5, then, we call the recursive function to the next empty cell, with 5 on board.

    
    ```
    |50.|...|.21|
    |43.|...|...|
    |6..|...|...|
    |---+---+---|
    |2.1|5..|...|
    |...|..6|37.|
    |...|...|...|
    |---+---+---|
    |.68|...|4..|
    |...|23.|...|
    |...|.7.|...|
    ```
    
	The next option to cell [0,1] is 7. If doesn't have an option the function will return to last recursion, then the next possibility will be verified, this occurs until the sudoku solution is found.
    
__A* algorithm__
  - Function _solveAStar(board)_: The A* uses a heuristic to always obtain the best choice in each cell to solve the sudoku. In each execution of the function, all the cells are checked to identify which ones have the least possibilities, that is, those that have the lowest cost to reach the sudoku solution. There are often cells with the same costs and then one of these cells is selected to continue the solution. These possibilities are stored in a list and the cell are inserted in an orderly manner, leaving those with the least possibilities at the beginning of the list. Below is an example of the execution:
  

    ```
    |...|...|.21|
    |43.|...|...|
    |6..|...|...|
    |---+---+---|
    |2.1|5..|...|
    |...|..6|37.|
    |...|...|...|
    |---+---+---|
    |.68|...|4..|
    |...|23.|...|
    |...|.7.|...|
    ```
    
    The first execution of the function generates the following possibilities::
    
    ```
    [[3, 1, 4, [4, 7, 8, 9]], [3, 4, 4, [4, 6, 8, 9]], [3, 6, 4, [6, 7, 8, 9]], [4, 0, 4, [1, 5, 8, 9]], [4, 2, 4, [2, 4, 5, 9]], [4, 3, 4, [1, 4, 8, 9]], [6, 3, 4, [1, 3, 7, 9]], [6, 4, 4, [1, 2, 5, 9]], [6, 7, 4, [1, 3, 5, 9]], [0, 0, 5, [3, 5, 7, 8, 9]], [0, 1, 5, [4, 5, 7, 8, 9]], [0, 4, 5, [4, 5, 6, 8, 9]], [0, 6, 5, [5, 6, 7, 8, 9]], [1, 2, 5, [2, 5, 6, 7, 9]], [1, 3, 5, [1, 6, 7, 8, 9]], [1, 7, 5, [1, 5, 6, 8, 9]], [3, 5, 5, [3, 4, 7, 8, 9]], [3, 7, 5, [3, 4, 6, 8, 9]], [4, 8, 5, [2, 4, 5, 8, 9]], [6, 0, 5, [1, 3, 5, 7, 9]], [6, 8, 5, [2, 3, 5, 7, 9]], [7, 0, 5, [1, 5, 7, 8, 9]], [7, 2, 5, [4, 5, 6, 7, 9]], [8, 0, 5, [1, 3, 5, 8, 9]], [0, 2, 6, [3, 4, 5, 6, 7, 9]], [0, 3, 6, [3, 4, 6, 7, 8, 9]], [0, 5, 6, [3, 4, 5, 7, 8, 9]], [1, 4, 6, [1, 2, 5, 6, 8, 9]], [1, 5, 6, [1, 2, 5, 7, 8, 9]], [1, 8, 6, [2, 5, 6, 7, 8, 9]], [2, 2, 6, [2, 3, 4, 5, 7, 9]], [2, 3, 6, [1, 3, 4, 7, 8, 9]], [2, 4, 6, [1, 2, 4, 5, 8, 9]], [2, 6, 6, [1, 2, 5, 7, 8, 9]], [2, 7, 6, [1, 3, 4, 5, 8, 9]], [3, 8, 6, [3, 4, 6, 7, 8, 9]], [4, 1, 6, [1, 2, 4, 5, 8, 9]], [4, 4, 6, [1, 2, 4, 5, 8, 9]], [5, 0, 6, [1, 3, 5, 7, 8, 9]], [6, 5, 6, [1, 2, 3, 5, 7, 9]], [7, 1, 6, [1, 4, 5, 7, 8, 9]], [7, 5, 6, [1, 4, 5, 7, 8, 9]], [7, 6, 6, [1, 5, 6, 7, 8, 9]], [7, 7, 6, [1, 4, 5, 6, 8, 9]], [7, 8, 6, [4, 5, 6, 7, 8, 9]], [8, 1, 6, [1, 2, 4, 5, 8, 9]], [8, 2, 6, [2, 3, 4, 5, 6, 9]], [8, 3, 6, [1, 3, 4, 6, 8, 9]], [8, 6, 6, [1, 2, 5, 6, 8, 9]], [1, 6, 7, [1, 2, 5, 6, 7, 8, 9]], [2, 1, 7, [1, 2, 4, 5, 7, 8, 9]], [2, 8, 7, [2, 3, 4, 5, 7, 8, 9]], [5, 1, 7, [1, 2, 4, 5, 7, 8, 9]], [5, 2, 7, [2, 3, 4, 5, 6, 7, 9]], [5, 3, 7, [1, 3, 4, 6, 7, 8, 9]], [5, 4, 7, [1, 2, 4, 5, 6, 8, 9]], [5, 6, 7, [1, 2, 5, 6, 7, 8, 9]], [5, 7, 7, [1, 3, 4, 5, 6, 8, 9]], [8, 5, 7, [1, 2, 3, 4, 5, 8, 9]], [8, 7, 7, [1, 3, 4, 5, 6, 8, 9]], [8, 8, 7, [2, 3, 4, 5, 6, 8, 9]], [2, 5, 8, [1, 2, 3, 4, 5, 7, 8, 9]], [5, 5, 8, [1, 2, 3, 4, 5, 7, 8, 9]], [5, 8, 8, [2, 3, 4, 5, 6, 7, 8, 9]]]
    ```
    
    Items are stored as follows:
    
    ```
    [[<row>,<col>,<size>,<list of possibilities>],]
    ```
    
	In the case above, the selected cell will be [3,1] with the first possibility being 4. Then the function is called recursively and proceeds to the sudoku solution. In case there are no more possibilities, the function returns to the previous recursion and the next possibility in the list will be considered, in this case it would be 7.
  
# Additional
Function to visualize the board:
- _printRealBoard(board)_
Print the board as follows:

```
---------------------
8 5 7  | 3 4 9  | 6 2 1
4 3 2  | 8 6 1  | 5 9 7
6 1 9  | 7 5 2  | 8 4 3
---------------------
2 7 1  | 5 8 3  | 9 6 4
9 4 5  | 1 2 6  | 3 7 8
3 8 6  | 4 9 7  | 2 1 5
---------------------
7 6 8  | 9 1 5  | 4 3 2
1 9 4  | 2 3 8  | 7 5 6
5 2 3  | 6 7 4  | 1 8 9
---------------------
```

- _printLineBoard(board)_
Print the board as follows:

```
867351924143829765295746813318472596724695138956138247489513672672984351531267489
```

There are some commented lines to log the time used for the sudoku solution in each instance.
The lines are as follows:

```
For the case of using: python sudoku bfs|dfs|astar < input.txt
293.  startTime = time.time()
306.  elapsedTime = time.time() - startTime
307.  print("Elapsed time(s): " + str(elapsedTime))

For the case of using: python sudoku bfs|dfs|astar <filename.txt>
332.  startTime = time.time()
345.  elapsedTime = time.time() - startTime
346.  print("Elapsed time(s): " + str(elapsedTime))
```    

In the repository there is a list with the execution times of each instance in each algorithm, in addition to a graph to visualize the difference in performance of each one.
It is worth mentioning that such result was obtained in any execution, the times may vary from machine to machine, they serve only as a basis for analysis.

