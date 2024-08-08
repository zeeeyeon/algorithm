def dfs(graph, current, visited, goal):
    # graph : [[], [5], [6, 9], [9], [7, 8], [7, 3], [], [8], [], []]
    visited.add(current) # v = (1, 5, 7, 8)

    if current == goal: return 1

    for neighbor in graph[current]:
        if neighbor not in visited:
            current = neighbor
            dfs(graph, current, visited, goal)
    return 0

T = int(input())
for case in range(1, T+1):
    # V 정점, E 간선
    V, E = map(int, input().split())
    # 연결 된 간선을 리스트로 순회
    arr = [list(map(int, input().split())) for _ in range(E)]
    # S 시작, G 마지막 정점
    S, G = map(int, input().split())

    # 각 정점의 간선을 나누는 과정 (단방향!)
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = arr[i][0], arr[i][1]
        graph[v1].append(v2)

    # 방문한 정점을 저장할 집합
    visited = set()

    result = dfs(graph, S, visited, G)

    print(f'#{case} {result}')