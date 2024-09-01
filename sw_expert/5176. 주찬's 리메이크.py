def inorder(node):
    global count

    if node != 0:
        inorder(tree[node][0])
        count += 1
        data[node] = password[count - 1]
        inorder(tree[node][1])

for case in range(1, int(input()) + 1):
    length = 8
    arr = input()
    password = [0] * length
    data = [0] * (length + 1)
    tree = [[0, 0] for _ in range(length + 1)]

    n, arr = int(arr[0]), arr[1:]
    for i in range(length):
        password[i] = '0x' + arr[2 * i:2 * (i + 1)]
        password[i] = int(password[i], 16)
        password[i] -= (n * (i + 1))

    for i in range(1, length + 1):
        if (i * 2) <= length:
            tree[i][0] = i * 2
        if (i * 2 + 1) <= length:
            tree[i][1] = i * 2 + 1

    count = 0
    inorder(1)

    result = ""
    for i in range(1, length + 1):
        result += str(data[i] % 10)

    print(f'#{case} {result}')