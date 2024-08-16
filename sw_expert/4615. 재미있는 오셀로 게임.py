dxy = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
def check(x, y, arr, dx, dy, color):
    points = []
    for i in range(1, N):
        nx = x + dx * i
        ny = y + dy * i

        if 0 > nx or nx >= N or 0 > ny or ny >= N: break
        if arr[nx][ny] == 0: break
        if arr[nx][ny] == color:
            for px, py in points:
                arr[px][py] = color
            break
        points.append((nx, ny))


for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]

    arr[N//2 - 1][N//2 - 1] = arr[N//2][N//2] = 2
    arr[N//2 - 1][N//2] = arr[N//2][N//2 - 1] = 1

    for _ in range(M):
        x, y, color = map(int, input().split())
        x, y = x-1, y-1

        arr[x][y] = color
        for dx, dy in dxy: check(x, y, arr, dx, dy, color)

    black, white = 0, 0
    for i in arr:
        black += i.count(1)
        white += i.count(2)

    print(f'#{case} {black} {white}')