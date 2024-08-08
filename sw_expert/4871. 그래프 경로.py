# s: 시작정점, V:1번부터 마지막까지의 정점 개수
def dfs(S, G):
    # 방문한 정점을 표시
    visited = [0] * (V+1)
    # 시작 정점 방문했다는 표시
    visited[S] = 1
    # 스택 생성
    stack = []

    # v 정점 할당
    v = S

    while True:
        # 1번의 정점에서
        for w in data[v]:
            # 방문 하지않은 w가 존재하면
            if visited[w] == 0:
                # 현재 정점을 stack push 하고
                stack.append(v)
                # 정점을 w로 바꿔줌
                v = w
                # 방문했다는 표시 남겨줌
                visited[v] = 1
                break
        else:
            if stack: v = stack.pop()
            else: break

        # 문제에서 제시한 정점에 도착하면 1 리턴
        if v == G: return 1

    # 문제에서 제시한 정점에 도착하지 못하면 0 리턴
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
    data = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = arr[i][0], arr[i][1]
        data[v1].append(v2)

    result = dfs(S, G)

    print(f'#{case} {result}')