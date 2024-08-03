T = int(input())

for case in range(1, 2):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if N <= M : high, low = b, a
    else : high, low = a, b

    h_length = len(high)
    l_length = len(low)

    total = -1000
    for i in range(h_length - l_length + 1):
        sum_v = 0
        for j in range(l_length):
            sum_v += low[j] * high[i + j]
        print(sum_v)
        if total < sum_v : total = sum_v

    print(sum_v)


