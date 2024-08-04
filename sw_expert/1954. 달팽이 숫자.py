T = int(input())
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for case in range(1, T+1):
    N = int(input())
    data = [[0] * N for _ in range(N)]
    copy_data = [[True] * N for _ in range(N)]

    x, y = 0, 0
    data[x][y] = 1
    number = 1

    while number != N**2:
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if not copy_data[nx][ny]: continue

            number += 1
            data[nx][ny] = number
            copy_data[nx][ny] = False
            x, y = nx, ny
            break


    print(f'#{case}')
    for i in range(N):
        print(*data[i])