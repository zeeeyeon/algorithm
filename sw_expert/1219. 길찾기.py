T = 10


def dfs(START, END):
    visited = [0] * (V+1)
    visited[START] = 1

    stack = []

    v = START

    while True:
        for w in graph[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                visited[v] = 1
                break
        else:
            if stack: v = stack.pop()
            else : break

        if v == END: return 1
    return 0

for case in range(1, T+1):
    test_case, E = map(int, input().split())
    arr = list(map(int, input().split()))
    V = 100

    graph = [[] for _ in range(V+1)]

    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        graph[v1].append(v2)

    START = 0
    END = 99

    result = dfs(START, END)

    print(f'#{case} {result}')