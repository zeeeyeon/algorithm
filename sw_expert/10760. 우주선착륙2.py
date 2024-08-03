T = int(input())

dxy = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for case in range(1, T+1):
    N, M = map(int, input().split())
    data = [list((map(int, input().split()))) for _ in range(N)]

    place = 0

    for x in range(N):
        for y in range(M):
            check = 0
            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy

                if 0 > nx or nx >= N or 0 > ny or ny >= M: continue
                if data[nx][ny] < data[x][y]: check += 1
            if check >= 4: place += 1

    print(place)