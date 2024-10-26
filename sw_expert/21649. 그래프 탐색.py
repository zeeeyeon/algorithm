T = 1

# s: 시작정점, V:1번부터 마지막까지의 정점 개수
def dfs(s, V):
    # 방문한 정점을 표시
    visited = [0] * (V+1)
    # 스택 생성
    stack = []
    # 시작 정점 방문했다는 표시
    visited[s] = 1

    # v 정점 할당
    v = s

    # [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
    while True:
        # [2, 3] 1번의 정점에서
        for w in data[v]:
            # 방문 하지않은 w가 존재하면
            if visited[w] == 0:
                # 현재 정점을 stack push 하고
                stack.append(v)
                # 정점을 w로 바꿔줌
                v = w
                # 방문했다는 표시 남겨줌
                visited[w] = 1
                break
        # 남은 정점이 없어서 break가 걸리지 않으면
        else:
            # 이전 갈림길을 스택에서 꺼내서 (if Top > -1)
            if stack: v = stack.pop()
            # 되돌아갈 곳이 없고, 남은 갈림길이 없으면 탐색 종료
            else: break


for case in range(1, T+1):
    # V 정점, E 간선
    V, E = map(int, input().split())
    # 간선의 개수만큼 연결된 두 정점
    arr = list(map(int, input().split()))

    # index = 0 (0번의 정점이 없음 => []), index = 1 (1번과 연결된 정점 리스트 => [2, 3])

    # 리스트 안에 각 인덱스 리스트 공간을 준비 (1부터 시작하기 때문에 V+1로 설정)
    data = [[] for _ in range(V+1)]

    # 각 정점의 간선을 나누는 과정
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        # 양방향, 교차하여 넣어주기
        data[v1].append(v2)
        data[v2].append(v1)

    # dfs 사용하여(s: 시작 정점, V:1번부터 마지막까지의 정점 개수)
    dfs(1, V)
