from collections import deque

def bfs():
    global ans
    queue = deque()

    # 모든 시작 위치에 대해 BFS 시작
    for i in range(N):
        queue.append((i, 0, 0))  # 시작 위치, 위험도 합계, 더한 줄 수

    while queue:
        n, sm, k = queue.popleft()

        # 3줄이 더해졌다면, ans와 비교하여 최솟값 입력
        if k == 3:
            ans = min(ans, sm)
            continue

        # 방문하지 않은 줄이며, 이전 줄과 같은 줄이 아닐 경우에 방문
        for j in range(N):
            if n != j and not visited[j]:
                visited[j] = True
                queue.append((j, sm + danger[n][j], k + 1))
                visited[j] = False


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    danger = [list(map(int, input().split())) for _ in range(N)]

    # 정답 출력할 최소 위험도 초기 설정
    ans = float('inf')

    # BFS를 위한 방문 배열 초기화
    visited = [False] * N

    bfs()

    print(f'#{test_case} {ans}')