T = int(input())
for case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    color = ['W’, ‘B’, ‘R']

    total = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            count = 0

            for select in range(i+1): count += arr[select].count('W')
            for select in range(i+1, j+1): count += arr[select].count('B')
            for select in range(j+1, N): count += arr[select].count('R')

            total = max(total, count)
    print(f'{case} {N*M-total}')