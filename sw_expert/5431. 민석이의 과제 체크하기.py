for case in range(1, int(input()) + 1):
    length, submit = map(int, input().split())
    data = list(map(int, input().split()))

    result = []
    for i in range(1, length + 1):
        if i not in data: result.append(str(i))

    print(f'#{case} {" ".join(result)}')

