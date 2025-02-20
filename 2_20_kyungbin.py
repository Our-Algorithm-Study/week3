# -*- coding: utf-8 -*-
"""2.20_kyungbin.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xjvMOllA-7OgAicmjuGyhsEhUsPkR-pM
"""

# 스택 연습

stack = []

stack.append(0)
stack.append(8)
stack.append(2)
stack.append(5)
stack.pop()
stack.append(9)
stack.append(7)
stack.pop()

#최상단부터 출력
print(stack[::-1])
#최하단부터 출력
print(stack)

# 큐 연습

from collections import deque

queue = deque()

queue.append(0)
queue.append(8)
queue.append(2)
queue.append(5)
queue.popleft()
queue.append(9)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# 재귀함수 연습

# def recursive_function():
#   print("재귀함수를 호출합니다.")
#   recursive_function()

# recursive_function()

def recursive_function(i):
  if i == 5:
    return

  print(i, '번째 재귀함수에서',i+1, '번째 재귀함수를 호출합니다.' )
  recursive_function(i+1)
  print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)

#콜 스택 개념

#DFS 연습
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

def dfs(graph, v, visted):
  visted[v] = True
  print(v, end = ' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)



dfs(graph, 1, visited)

# BFS 연습
from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True

  while queue:

    v = queue.popleft()
    print(v, end = ' ')

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

bfs(graph, 1, visited)

# 1012번 유기농배추



from collections import deque
# 배추밭이 몇 개의 그룹으로 묶이는 지 알아내기


#움직일 수 있는 경우의 수

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

test_case = int(input())


# 좌표를 돌다가 '1'이 표시된 좌표가 있으면 bfs 알고리즘 사용

def bfs(graph, a, b, n, m):
    queue = deque([(a, b)])
    graph[a][b] = 0 #해당 좌표를 0으로 만들어줌.

    while queue:
        x, y = queue.popleft() #큐에서 빼준다.
        for i in range(4): # 네 방향 모두 움직인다.
            nx, ny = x + dx[i], y + dy[i]
            # 좌표를 더했을 때 우리가 설정한 좌표보다 커지면 안됨, 1이 표시된걸 발견
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

for _ in range(test_case):
    count = 0
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)] # 좌표에 0을 채워넣기

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1 #배추가 있는 좌표는 1로 채워주기

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1: # 1이 있는 좌표를 발견하면 bfs알고리즘
                bfs(graph, a, b, n, m)
                count += 1 #한 번 돌릴 때마다 하나의 그룹 -> 지렁이 하나 추가

    print(count)