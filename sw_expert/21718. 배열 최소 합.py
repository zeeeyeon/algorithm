def find_min_sum(depth, current_sum):
    global min_sum

    # if depth == N:
    #     min_sum = min(min_sum, current_sum)
    #     return
    #
    # for i in range(N):
    #     if not visited[i]:
    #         visited[i] = True
    #         find_min_sum(depth + 1, current_sum + arr[depth][i])
    #         visited[i] = False

T = int(input())

for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    min_sum = 0

    print(visited)

    # find_min_sum(depth=0, current_sum=0)

    # print(min_sum)