# def dfs(START, END):
#     visited = [0] * (V+1)
#     visited[START] = 1
#
#     stack = []
#
#     v = START
#
#     while True:
#         for w in graph[v]:
#             if visited[w] == 0:
#                 stack.append(v)
#                 v = w
#                 visited[v] = 1
#                 break
#         else:
#             if stack: v = stack.pop()
#             else : break
#
#         if v == END: return 1
#     return 0
#
# T = 10
# for case in range(1, T+1):
#     test_case, E = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     V = 100
#     START = 0
#     END = 99
#
#     graph = [[] for _ in range(V+1)]
#
#     for i in range(E):
#         v1, v2 = arr[i*2], arr[i*2+1]
#         graph[v1].append(v2)
#
#
#
#     result = dfs(START, END)
#
#     print(f'#{case} {result}')

T = 10
for case in range(1, T+1):
    test_case, E = map(int, input().split())
    edges = list(map(int, input().split()))

    V = 100
    START = 0
    END = 99

    def dfs(START, visited):
        global result

        if result == 1: return

        if START == END:
            result = 1
            return

        visited[START] = True

        for neighbor in graph[START]:
            if visited[neighbor]: continue
            dfs(neighbor, visited)


    graph = [[] for _ in range(V)]

    for i in range(0, len(edges), 2):
        graph[edges[i]].append(edges[i+1])

    visited = [False] * V
    result = 0

    dfs(START, visited)

    print(f'#{case} {result}')

'''
    DFS 파라미터로 뭘 해야하는가? 잘 모르겠으면 위의 변수 다 집어넣기
    1. 재귀 호출을 중단하기 위한 파라미터
    => 시작 지점이 목표지점에 도달했을 떄
    => 목표 지점은 고정되어있고,
    => 시작 지점을 파라미터로 넘기기

    2. 누적해서 가져간다던가, 목표하는 바를 찾기위해 계속 가져가야하는 값
    => 방문여부를 확인하는 변수
'''
# for _ in range(10):  # 10개의 테스트 케이스
#     tc, N = map(int, input().split())
#     edges = list(map(int, input().split()))
#     SIZE, START, END = 100, 0, 99
#
#     # 도착을 못할거라는 가정하에 시작
#     result = 0
#
#     # [1, 2], [4, 3], [9, 5], [7], [8, 3], [6, 7], [10], [99, 9], [], [8, 10], []
#
#     def dfs(vertex, visited):
#         global result
#
#         # 이미 도착지를 찾은 경우에는 아래 로직을 실행하지 않도록 함 ( 이런게 백트래킹 )
#         if result == 1:
#             return
#
#         # 시작지점이 도착지에 도착한 경우에는 결과를 1로 바꾸고 종료
#         if vertex == END:
#             result = 1
#             return
#
#         # 현재 노드를 방문 처리
#         visited[vertex] = True
#
#         # 인접한 노드에 대해서 DFS 실행, 대신 방문한 노드는 DFS를 실행하지 않음
#         for adj_vertex in graph[vertex]:
#             if visited[adj_vertex]:
#                 continue
#             dfs(adj_vertex, visited)
#
#
#     # 그래프 초기화
#     # 인접리스트로 구현
#     # 100개의 정점이 있기 때문에 100개의 2차원 배열을 할당함
#     # 여기서 이전 코드의 V+1을 하지 않는 이유는 정점값이 0부터 주어지기 때문
#     graph = [[] for _ in range(SIZE)]
#
#     for i in range(0, len(edges), 2):
#         graph[edges[i]].append(edges[i + 1])
#
#     # DFS 수행, 주어진 정점의 갯수만큼 False로 초기화
#     visited = [False] * SIZE
#
#     dfs(START, visited)
#
#     print(f'#{tc} {result}')