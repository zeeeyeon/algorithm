from collections import deque

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs(x, y):
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1

    queue = deque([[x, y]])

    while queue:
        x, y = queue.popleft()
        if maze[x][y] == END:
            return visited[x][y] - 2

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if maze[nx][ny] == WALL: continue
            if visited[nx][ny]: continue

            queue.append([nx, ny])
            visited[nx][ny] = visited[x][y] + 1

    return 0

T = int(input())
for case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    LOAD, WALL, START, END = 0, 1, 2, 3
    x, y = 0, 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == START:
                x, y = i, j
                break
        if maze[i][j] == START : break

    print(f"#{case} {bfs(x, y)}")