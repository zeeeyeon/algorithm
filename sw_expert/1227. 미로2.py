from collections import deque

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs(x, y):
    visited = [[False] * N for _ in range(N)]
    queue = deque([[x, y]])

    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        if maze[x][y] == END:
            return 1

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if maze[nx][ny] == WALL: continue
            if visited[nx][ny]: continue
            queue.append([nx, ny])
            visited[nx][ny] = True
    return 0

for _ in range(1, 11):
    N = 100
    case = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    LOAD, WALL, START, END = 0, 1, 2, 3
    x, y= 0, 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == START:
                x, y = i, j
                break
        if maze[i][j] == START: break

    print(f'#{case} {bfs(x, y)}')