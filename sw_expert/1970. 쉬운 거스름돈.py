T = int(input())

for case in range(1, T+1):
    money = int(input())

    won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = []

    for i in range(len(won)):
        change.append(money // won[i])
        money %= won[i]

    print(f'#{case}')
    print(*change)