import heapq

def dijkstra(start):
    heap = []

    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now  ] < dist: continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost

            if new_cost >= distance[next_node]: continue

            distance[next_node] = new_cost
            heapq.heappush(heap, (new_cost, next_node))


for T in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    INF = int(1e9)
    graph = [[] for i in range(N + 1)]
    distance = [INF] * (N + 1)

    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start].append([end, weight])

    dijkstra(0)

    print(f'#{T} {distance[N]}')