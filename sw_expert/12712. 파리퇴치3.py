for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    da = [-1, 1, 1, -1]
    db = [1, 1, -1,-1]

    total = 0
    for i in range(N):
        for j in range(N):
            sum_x = arr[i][j]
            sum_a = arr[i][j]
            for k in range(len(dx)):
                for c in range(1, M):
                    nx = i + dx[k] * c
                    ny = j + dy[k] * c
                    na = i + da[k] * c
                    nb = j + db[k] * c

                    # 계산하는 범위는 한번에 하지 않기
                    # if 0 > nx or nx >= N or 0 > ny or ny >= N or 0 > na or na >= N or 0 > nb or nb >= N: continue
                    # sum_x += arr[nx][ny]
                    # sum_a += arr[na][nb]
                    if 0 <= nx < N and 0 <= ny < N:
                        sum_x += arr[nx][ny]
                    if 0 <= na < N and 0 <= nb < N:
                        sum_a += arr[na][nb]
            total = max(sum_x, sum_a, total)
    print(f'#{case} {total}')