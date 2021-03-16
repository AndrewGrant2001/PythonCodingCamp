# Andrew Grant
# 105226219

def empty(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] != 0:
                return False
    return True


def find(grid, x):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == x:
                return [i, j]
    return [-1, -1]


grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
x = 67

print(empty(grid))
print(find(grid, x))