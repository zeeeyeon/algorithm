def dfs(x, y, visited):
    global result

    # 도착지점에 닿으면 끝
    if maze[11][11] == END:
        result = 1
        return

    # 도착한 길 표시하기
    visited[x][y] = False

    # 0으로 되어있는 길로만 갈 수 있음
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy

        # 이동하려는 좌표가 범위를 벗어난 경우
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        # 이동하려는 좌표가 벽일 경우
        if maze[nx][ny] == WALL: continue
        # 방문했던 곳인지 확인
        if not visited[nx][ny]: continue

        dfs(nx, ny, visited)

    return result

T = 10
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for case in range(1, T+1):
    N = 16
    case = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    visited = [[True] * N for _ in range(N)]

    WALL, START, END = 1, 2, 3
    x, y, result = 1, 1, 0

    # 출발지에서 갈 수 있는 길 검색
    visited[x][y] = False
    a = dfs(x, y, visited)

    print(f'#{case} {a}')