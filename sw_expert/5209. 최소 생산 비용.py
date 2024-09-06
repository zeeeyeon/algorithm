import sys
sys.stdin = open('input.txt', 'r')


def dfs(x, current_sum):
    global total

    if total < current_sum: return

    if x == N:
        total = min(total, current_sum)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(x + 1, arr[x][i] + current_sum)
            visited[i] = False


for T in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    total = float('inf')

    dfs(0, 0)
    print(f'#{T} {total}')
