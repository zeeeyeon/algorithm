T = int(input())
for case in range(1, T+1):
    arr = list(map(int, input().split()))
    length = 1
    number = 2

    total = 0
    for i in range(number):
        for j in range(length):
            if i & (1 << j):
                total += arr[j]

    print(total)