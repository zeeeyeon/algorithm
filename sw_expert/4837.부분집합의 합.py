T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())

    arr = []
    for i in range(1, 13):
        arr.append(i)

    n = len(arr)
    subset_count = 2 ** n

    count = 0
    for i in range(subset_count):
        sub = []
        for j in range(n):
            if i & (1 << j):
                sub.append(arr[j])
        if len(sub) == N and sum(sub) == M: count += 1

    print(f'#{case} {count}')