def find_min_sum(x, current_sum):
    global max_sum

    if max_sum >= current_sum: return

    if x == N:
        max_sum = max(max_sum, current_sum)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            find_min_sum(x + 1, current_sum * arr[x][i]/100)
            visited[i] = False

T = int(input())
for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    max_sum = 0

    find_min_sum(0, 1)
    print(f'#{case} {max_sum * 100:.6f}')