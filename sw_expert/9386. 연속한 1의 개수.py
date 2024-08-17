for case in range(1, int(input()) + 1):
    length = int(input())
    numbers = list(map(int, input()))

    total, count = 0, 0
    for i in range(length):
        if numbers[i]: count += 1
        else :
            if total < count: total = count
            count = 0
    if total < count: total = count
    print(f'#{case} {total}')

