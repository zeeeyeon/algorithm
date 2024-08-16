dxy = [[0, 1], [1, 0]]

def check_puzzle(x, y, arr, dx, dy):
    count = 0
    for i in range(1, 4):
        nx = x + dx * i
        ny = y + dy * i
        if nx < 0 or nx >= N or ny < 0 or ny >= N: break
        if arr[nx][ny] == 1: count += 1

    return count == 3

for case in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    for dx, dy in dxy:
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 1:
                    if check_puzzle(i, j, arr, dx, dy): total += 1


    print(total)