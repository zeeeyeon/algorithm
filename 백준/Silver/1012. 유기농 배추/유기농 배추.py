from collections import deque

def bfs(ground, x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if ground[nx][ny]: queue.append([nx, ny])
            # 같은 좌표를 여러번 넣는 것을 방지, 미리 0으로 변경 후 큐에서 뽑기 (메모리 초과남 !!!!!)
            ground[nx][ny] = 0

    return 1

for case in range(1, int(input()) + 1):
    N, M, B = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    count = 0

    for _ in range(B):
        x, y = map(int, input().split())
        ground[x][y] = 1

    for x in range(N):
        for y in range(M):
            if ground[x][y]:
                count += bfs(ground, x, y)

    print(count)