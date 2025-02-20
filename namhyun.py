### 1012 유기농 배추 DFS

def sol(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    if field[x][y] == 1:
        field[x][y] = 2
        
        sol(x, y+1)
        sol(x, y-1)
        sol(x-1, y)
        sol(x+1, y)
        
        return True
    
    return False

t = int(input())

for tt in range(t):
    m, n, k = map(int, input().split())

    field = [[0] * m for _ in range(n)]

    for i in range(k):
        y, x = map(int, input().split())
        field[x][y] = 1


    count = 0
    for i in range(n):
        for j in range(m):
            if sol(i, j):
                count += 1

    print(count)


from collections import deque


def sol(x, y):
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                
            if field[nx][ny] == 1:
                field[nx][ny] = 2
                queue.append((nx, ny))


# 유기농 배추 BFS
                
t = int(input())

for tt in range(t):
    m, n, k = map(int, input().split())

    field = [[0] * m for _ in range(n)]

    for i in range(k):
        y, x = map(int, input().split())
        field[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    count = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                sol(i,j)
                count += 1

    print(count)


# 2178 미로 탐색

from collections import deque


n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input().rstrip())))
    
queue = deque([(0, 0)])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
            
        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            queue.append((nx, ny))
            
print(maze[n-1][m-1])
