for case in range(1, int(input()) + 1):
    bus = [0] * 5001

    for _ in range(int(input())):
        start, end = map(int, input().split())
        for i in range(start, end+1):
            bus[i] += 1

    result = []
    for _ in range(int(input())):
        number = int(input())
        result.append(bus[number])

    print(f'#{case}', end=' ')
    print(*result)