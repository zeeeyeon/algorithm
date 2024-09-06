from collections import deque

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    visited = [[-1] * M for _ in range(N)]
    total = 0
    queue = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                queue.append((i, j))
                visited[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                total += visited[nx][ny]

    print(f"#{T} {total}")