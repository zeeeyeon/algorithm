def dfs(S, G):
    visited = [0] * (V+1)
    visited[S] = 1
    stack = []

    v = S

    while True:
        for w in data[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                visited[v] = 1
                break
        else:
            if stack: v = stack.pop()
            else : break

        if v == G: return 1

    return 0


T = int(input())
for case in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    data = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = arr[i][0], arr[i][1]
        data[v1].append(v2)

    result = dfs(S, G)

    print(f'#{case} {result}')