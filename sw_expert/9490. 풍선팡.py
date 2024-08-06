T = int(input())

for case in range(1, 2):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    max_v = 0
    for x in range(N):
        for y in range(M):
            sum_v = 0
            for i in range(4):
                for j in range(1, arr[x][y]+1):
                    nx = x + dx[i] * j
                    ny = y + dy[i] * j

                    if 0 <= nx < N and 0 <= ny < M:
                        sum_v += arr[nx][ny]
            sum_v += arr[x][y]
            if max_v < sum_v: max_v = sum_v

    print(f'#{case} {max_v}')