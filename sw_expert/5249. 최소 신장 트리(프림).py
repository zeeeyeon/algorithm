from heapq import heappop, heappush

def prim(start):
    heap = list()
    visited = [0] * (V + 1)

    sum_weight = 0
    heappush(heap, (0, start))

    while heap:
        weight, v = heappop(heap)

        if visited[v]: continue

        visited[v] = 1
        sum_weight += weight

        for next in range(V+1):
            if graph[v][next] == 0: continue
            if visited[next]: continue

            heappush(heap, (graph[v][next], next))

    return sum_weight


for T in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    graph = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w

    result = prim(0)
    print(f'#{T} {result}')
