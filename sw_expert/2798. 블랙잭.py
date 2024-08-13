N, M = map(int, input())
arr = list(map(int, input().split()))

total = 0
for i in range(N-1):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if total < arr[i] + arr[j] + arr[k] <= M:
                total = arr[i] + arr[j] + arr[k]

print(total)