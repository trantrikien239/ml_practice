#

def nextMove(n,r,c,grid):
    p_row, p_col = [(x,y) for x in range(n) for y in range(n) if grid[x][y] == 'p'][0]
    move_row = 'UP' if r - p_row > 0 else 'DOWN'
    move_col = 'LEFT' if c - p_col > 0 else 'RIGHT'
    if r - p_row != 0:
        return move_row
    elif c - p_col != 0:
        return move_col


n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))