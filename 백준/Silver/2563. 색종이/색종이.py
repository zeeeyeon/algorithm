N = 100
M = 10
arr = [[0] * N for _ in range(N)]

for _ in range(int(input())):
    left, right = map(int, input().split())
    for i in range(M):
        for j in range(M):
            arr[left + i][right + j] = 1

count = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            count += 1

print(count)