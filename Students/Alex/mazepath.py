
def isSafe(maze, visited, x, y, n, m):
    return (x >= 0 and x < n and y >= 0 and y < m and maze[x][y] == 0 and not visited[x][y])


def findPaths(maze, visited, x, y, n, m, path):
    # Base case: If we've reached the bottom-right corner, print the path
    if x == n - 1 and y == m - 1:
        print(path)
        return
    

    visited[x][y] = True
    
    # Move Right (x, y+1)
    if isSafe(maze, visited, x, y + 1, n, m):
        findPaths(maze, visited, x, y + 1, n, m, path + "R") 
    
    # Move Down (x+1, y)
    if isSafe(maze, visited, x + 1, y, n, m):
        findPaths(maze, visited, x + 1, y, n, m, path + "D")  
    
    
    visited[x][y] = False


def solveMaze(maze, n, m):
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    # Start from the top-left corner (0,0) with an empty path
    if maze[0][0] == 0:  # Check if the start is not blocked
        findPaths(maze, visited, 0, 0, n, m, "")
    else:
        print("No path exists")

# Example usage
n, m = 3, 3  # Define maze size
maze = [
    [0, 0, 0],  # 0 means open path
    [0, 1, 0],  # 1 means blocked cell
    [0, 0, 0]
]

solveMaze(maze, n, m)