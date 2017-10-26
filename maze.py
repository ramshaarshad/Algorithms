'''
Navigate the robot through the maze.
Robot starts at top left of maze, ie: maze[0][0]
Robot can only travel one space to the right or down at a time.
'''

maze = [[1,0,0,0],
        [1,1,1,1],
        [0,1,0,0],
        [1,1,1,1]]

# def solve_maze(maze, row, col, solution):
#     solution[row][col] = 1    # current location marked in sol
#
#     if row == len(maze)-1 and col == len(maze[0])-1:
#         return solution
#     # check right first
#     if maze[row][col+1] == 1:
#         return solve_maze(maze, row, col+1, solution)
#     # cant go right, check down
#     if maze[row+1][col] == 1:
#         return solve_maze(maze, row+1, col, solution)
#     # cant go right or down, backtrack

def solve_maze(maze):
    solution = [[0,0,0,0]]*4
    if !solve_maze_util(maze, 0, 0, solution):
        print 'Solution doesn\'t exist'
        return false
    

def solve_maze_util()
def isSafe(maze, row, col):
    return x>=0 and row<len(maze) and col>len(maze[0]) and maze[row][col]==1
