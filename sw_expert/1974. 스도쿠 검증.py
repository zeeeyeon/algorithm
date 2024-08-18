import sys
sys.stdin = open('input.txt')

def check():
    for number in arr:
        if len(set(number)) != N:
            return 0

    arr_reverse = list(zip(*arr))
    for number in arr_reverse:
        if len(set(number)) != N:
            return 0

    for i in range(0, N, 3):
        for j in range(0, N, 3):
            number_list = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
            if len(set(number_list)) != N:
                return 0
    return 1

for case in range(1, int(input())):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = check()

    print(f'#{case} {result}')