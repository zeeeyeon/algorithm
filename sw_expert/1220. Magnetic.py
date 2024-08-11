T = int(input())

for case in range(1, T+1):
    length = int(input())
    arr = [list(map(int, input().split())) for _ in range(length)]

    # 1 = N, 2 = S
    # 열에서 원소가 하나면 넘기기
    #