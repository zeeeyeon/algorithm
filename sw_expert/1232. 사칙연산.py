def search(num):
    if not tree[num][0] and not tree[num][1]:
        return int(node[num])

    left = search(tree[num][0])
    right = search(tree[num][1])

    if node[num] == '+':
        return left + right
    if node[num] == '-':
        return left - right
    if node[num] == '*':
        return left * right
    if node[num] == '/':
        return left / right

for case in range(1, 11):
    N = int(input())

    # 각 노드에 값 넣기
    node = [''] * (N+1)
    # 자손 가지고 있는 노드들 넣기
    tree = [[0, 0] for _ in range(N+1)]

    for i in range(1, N+1):
        arr = list(input().split())
        node[i] = arr[1]
        if len(arr) == 4:
            tree[i][0] = int(arr[2])
            tree[i][1] = int(arr[3])

    print(f'#{case} {int(search(1))}')