import sys
sys.stdin = open('input.txt')

T = 10
for case in range(1, T+1):
    length = int(input())
    arr = [list(map(int, input().split())) for _ in range(length)]
    count = 0

    new_arr = list(zip(*arr))
    for col in new_arr:
        prev = 0
        for i in col:
            if i:
                if i == 2 and prev == 1:
                    count += 1
                prev = i
    print(f'#{case} {count}')