from collections import deque

def bfs(x, y):
    global count

    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if not arr[nx][ny]: continue
            if visited[nx][ny]: continue
            queue.append([nx, ny])
            visited[nx][ny] = True
            count += 1

    return count

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[False] * (N) for _ in range(N)]
result_arr = []
count = 1

for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j]:
            visited[i][j] = True
            result = bfs(i, j)
            result_arr.append(result)
            count = 1

print(len(result_arr))
result_arr.sort()
for size in result_arr:
    print(size)