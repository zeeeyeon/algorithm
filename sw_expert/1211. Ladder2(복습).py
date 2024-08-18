import sys
sys.stdin = open('input.txt')

dxy = [[1, 0], [0, 1], [0, -1]]
def search_ladder(x, y):
    visited = [[False] * LENGTH for _ in range(LENGTH)]
    visited[x][y] = True

    count = 0
    while x != LENGTH-1:
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= LENGTH or ny < 0 or ny >= LENGTH: continue
            if visited[nx][ny]: continue
            if arr[nx][ny]:
                visited[nx][ny] = True
                x, y = nx, ny
                count += 1

    return count

for case in range(1, 11):
    test_case = int(input())
    LENGTH, START_X = 100, 0
    arr = [list(map(int, input().split())) for _ in range(LENGTH)]

    count_list = []
    for i in range(LENGTH):
        if not arr[START_X][i]: continue
        count = search_ladder(START_X, i)
        count_list.append([i, count])

    result = sorted(count_list, key=lambda x:(-x[1], x[0]))
    print(f'#{case} {result[-1][0]}')