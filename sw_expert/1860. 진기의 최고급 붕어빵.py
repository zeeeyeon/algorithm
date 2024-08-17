for case in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    arr_ = map(int, input().split())
    arr = sorted(arr_)

    count, arrived = 0, 11111
    result = 'Impossible'
    for i in range(arrived + 1):
        if i % M == 0 and i != 0: count += K
        if arr[0] < M: break
        if i in arr:
            number = arr.count(i)
            count -= number

        if count < 0: break
    else : result = 'Possible'

    print(f'#{case} {result}')
