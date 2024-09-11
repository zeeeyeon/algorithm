from heapq import heappop, heappush


def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y: return

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y


for T in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    edge = []
    count, total = 0, 0

    for _ in range(E):
        u, v, w = map(int, input().split())
        edge.append([u, v, w])

    edge.sort(key=lambda x : x[2])
    parents = [i for i in range(V + 1)]

    for u, v, w in edge:
        if find_set(u) != find_set(v):
            count += 1
            union(u, v)
            total += w
            if count == V: break

    print(f'#{T} {total}')