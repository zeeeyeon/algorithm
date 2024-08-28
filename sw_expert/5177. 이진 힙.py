def enqueue(target):

    while target // 2:
        parent = target // 2
        if tree[target] <= tree[parent]:
            tree[target], tree[parent] = tree[parent], tree[target]
        target = parent

for case in range(1, int(input()) + 1):
    N = int(input())
    arr = map(int, input().split())

    tree = [0]
    last = 0
    for item in arr:
        tree.append(item)
        last += 1
        enqueue(last)

    result = 0
    while last:
        parent = last // 2
        result += tree[parent]
        last = parent

    print(f'{case} {result}')