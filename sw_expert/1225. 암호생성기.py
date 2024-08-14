for case in range(1, 11):
    test_case = int(input())
    numbers = list(map(int, input().split()))

    count = 1
    while numbers[-1] > 0:
        for i in range(len(numbers)):
            if count > 6: count = 1
            numbers[0] -= count
            count += 1

            numbers.append(numbers[0])
            del numbers[0]

            if numbers[-1] <= 0:
                flag = False
                numbers[-1] = 0
                break

    print(f'#{case}', end=' ')
    print(*numbers)

