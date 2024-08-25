dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def search_end(x, y, visited):
    global result

    if maze[x][y] == END: result = 1

    visited[x][y] = True

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if maze[nx][ny] == WALL: continue
        if visited[nx][ny]: continue

        search_end(nx, ny, visited)

    return result

for _ in range(1, 11):
    case = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]
    # maze = list(map(list, zip(*arr)))

    LOAD, WALL, START, END = 0, 1, 2, 3
    x, y, result = 0, 0, 0

    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            print(maze[i][j])
            if maze[i][j] == START:
                x, y = i, j
                break
        if maze[i][j] == START: break

    print(f'#{case} {search_end(x, y, visited)}')