for t in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = input()
    length = len(arr) // 4
    password = set()

    for rotate in range(length):
        for i in range(0, len(arr), length):
            password.add(arr[i:i+length])

        arr = arr[1:] + arr[0]

    result = []
    for i in password:
        result.append(int(i, 16))

    result_arr = sorted(result, reverse=True)

    print(f'#{t} {result_arr[K - 1]}')
