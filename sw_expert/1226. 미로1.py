dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def search_load(x, y):
    visited[x][y] = True



for _ in range(1, 11):
    case = int(input())
    N = 16
    load = [list(map(int, input())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]

    START, END = 2, 3
    LOAD, WALL = 0, 1
    start_x, start_y = 1, 1


    search_load(start_x, start_y)