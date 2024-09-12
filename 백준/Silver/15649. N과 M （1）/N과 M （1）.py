N, M = map(int, input().split())

path = []
def recur(x):
    if x == M:
        print(*path)
        return

    for i in range(1, N+1):
        if i not in path:
            path.append(i)
            recur(x + 1)
            path.pop()

recur(0)