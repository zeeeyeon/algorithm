T = int(input())
for case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    for i in range(N):
        for j in range(N):
            if i == j: total += data[i][j]
            if N - i == j: total += data[i][j]

    total -= data[N//2][N//2]
    print(total)