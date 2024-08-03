T = int(input())

# 중간, 오른쪽, 아래, 왼쪽, 위
dxy = [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]

for case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for x in range(N):
        for y in range(M):
            sum_v = 0
            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy

                if 0 > nx or nx >= N or 0 > ny or ny >= M: continue
                sum_v += arr[nx][ny]

            if max_v < sum_v: max_v = sum_v

    print(max_v)