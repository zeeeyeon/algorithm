dxy = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
def check(x, y, arr, dx, dy):
    count = 0
    for c in range(1, 5):
        nx = x + dx * c
        ny = y + dy * c

        if 0 > nx or nx >= length or 0 > ny or ny >= length: break
        if arr[nx][ny] == '.': break
        count += 1
    return count == 4

for case in range(1, int(input()) + 1):
    length = int(input())
    arr = [input() for _ in range(length)]
    result = 'NO'

    for i in range(length):
        for j in range(length):

            if arr[i][j] == '.': continue
            for dx, dy in dxy:
                if check(i, j, arr, dx, dy):
                    result = 'YES'
                    break
        if result == 'YES': break

    print(f'#{case} {result}')
