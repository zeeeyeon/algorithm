import sys
sys.stdin = open('input.txt')
dxy = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]

def check():
    for i in arr:
        if len(set(i)) != N: return 0

    arr_reverse = list(zip(*arr))
    for i in arr_reverse:
        if len(set(i)) != N: return 0

    rotate_list = [1, 4, 7]

    for i in rotate_list:
        for j in rotate_list:
            numbers = set()
            for dx, dy in dxy:
                nx, ny = i + dx, j + dy
                numbers.add(arr[nx][ny])

            if len(numbers) != N: return 0
    return 1


for case in range(1, int(input()) + 1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = check()

    print(f'#{case} {result}')