T = int(input())
for case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    print(f'{case} {arr[M%N]}')
'''
    flag = True
    result = 0

    while flag:
        for i in range(N):
            if M <= 0:
                break
            arr.append(arr[0])
            del arr[0]
            M -= 1
        if M <= 0: flag = False

    print(f'#{case} {arr[0]}')
'''
