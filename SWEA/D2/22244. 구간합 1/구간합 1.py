for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_len = max(len(i) for i in arr)

    for i in range(N):
        while max_len - len(arr[i]):
            arr[i].append(0)

    reverse_arr = list(map(list, zip(*arr)))

    for arr in reverse_arr:
        while 0 in arr:
            arr.remove(0)

    max_sum, min_sum = -float('inf'), float('inf')
    for row in reverse_arr:
        if len(row) < M: continue
        for i in range(len(row) - M + 1):
            current_sum = sum(row[i:i+M])
            max_sum = max(max_sum, current_sum)
            min_sum = min(min_sum, current_sum)

    if max_sum == -float('inf') or min_sum == float('inf'):
        print(f'#{T} -1')
    else:
        print(f'#{T} {max_sum - min_sum}')