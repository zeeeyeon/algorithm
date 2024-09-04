# def search_max_percent(level, current_sum):
#     global max_percent
#
#     if max_percent <= current_sum
#
#
# for x in range(1, int(input()) + 1):
#     level = int(input())
#
#     visited = [False] * level
#     max_percent = float('inf')
#
#     search_max_percent(level, current_sum = 0)

def find_min_sum(x, current_sum):
    global min_sum

    if min_sum <= current_sum: return

    if x == N:
        min_sum = min(min_sum, current_sum)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            find_min_sum(x + 1, current_sum + arr[x][i])
            visited[i] = False

T = int(input())
for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    min_sum = float('inf')

    find_min_sum(x = 0, current_sum = 0)
    print(f'#{case} {min_sum}')