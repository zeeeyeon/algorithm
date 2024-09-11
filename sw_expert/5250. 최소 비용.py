import heapq

def dijkstra(x, y):
    heap = []
    heapq.heappush(heap, (0, x, y))
    distance[x][y] = 0

    while heap:
        dist, x, y = heapq.heappop(heap)

        if distance[x][y] < dist: continue

        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue

            cost = max(0, arr[nx][ny] - arr[x][y])
            new_cost = dist + cost + 1

            if new_cost < distance[nx][ny]:
                distance[nx][ny] = new_cost
                heapq.heappush(heap, (new_cost, nx, ny))


for T in range(1, int(input()) + 1):
    N = int(input())
    INF = int(1e9)
    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * (N) for _ in range(N)]

    dijkstra(0, 0)
    print(f"#{T} {distance[N - 1][N - 1]}")