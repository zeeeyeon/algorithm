T = int(input())
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for case in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    for x in range(N):
        for y in range(N):
            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy

                if 0 > nx or nx >= N or 0 > ny or ny >= N: continue
                total += abs(data[nx][ny] - data[x][y])
    print(f'#{case} {total}')