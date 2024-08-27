def search_node(node):
    global count

    if node:
        search_node(tree[node][0])
        result[node-1] = count
        count += 1
        search_node(tree[node][1])


for case in range(1, int(input()) + 1):
    N = int(input())
    # 루트에 저장된 값, N/2의 부모 노드 찾기
    arr = [i for i in range(1, N+1)]
    tree = [[0, 0] for i in range(N+1)]

    count = 1

    for i in range(1, len(arr)//2+1):
        tree[i][0] = i*2
        if i*2+1 <= N:
            tree[i][1] = i*2+1

    result = [0] * N
    search_node(1)

    print(f'{result[0]}, {result[N // 2 - 1]}')