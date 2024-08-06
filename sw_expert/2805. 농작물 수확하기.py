T = int(input())

for case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    '''
        5x5인 경우,
        mid = 2, i == 2까지는 i행에 대한 j의 값은 [mid - i : mid + i + 1]으로 계산하고
        i행의 인덱스가 mid(2)를 넘는 순간 j의 계산이 [mid - i : mid + i + 1] 가능해지려면
        i에 i % mid 나머지 값을 넣어서 계산해줘야 한다고 생각 ^.^&
    '''
    mid = N // 2
    total = 0

    for i in range(N):
        if i <= mid:
            total += sum(data[i][mid - i: mid + i + 1])
        else:
            k = i - mid
            total += sum(data[i][k: N-k])

    print(f'#{case} {total}')

