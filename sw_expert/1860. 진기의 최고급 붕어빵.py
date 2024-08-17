for case in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    arr_ = map(int, input().split())
    arr = sorted(arr_)

    count, arrived = 0, 11111
    result = 'Impossible'
    for i in range(arrived + 1):
        # 매 K초 마다 붕어빵 만들어서 count 더하기
        if i % M == 0 and i != 0: count += K
        # 손님 오는 시간 정렬 후 제일 처음 오는 손님이 굽는 시간보다 전에 도착하면 break
        if arr[0] < M: break
        # 같은 시간에 오는 손님이 있을 경우 카운팅 해서 빼기
        if i in arr:
            number = arr.count(i)
            count -= number
        # 붕어빵 재고가 마이너스, break
        if count < 0: break
    # 그 외의 경우 붕어빵 나눠주기 가능
    else : result = 'Possible'

    print(f'#{case} {result}')
