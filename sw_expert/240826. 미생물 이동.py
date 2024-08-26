T = int(input())

for case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [99] + list(map(int, input().split()))

    visited = [0] + [99] + [0] * (N-1)
    result = N

    for i in range(1, N+1):
        if arr[i]:
            visited.clear()
            visited = [0] + [99] + [0] * (N - 1)
            if (i+K) < (N+1): visited[i+K] = 99

        if not arr[i] and visited[i] == 99:
            result = i
            break

    print(f'#{case} {result}')