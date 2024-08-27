def search_node(node):
    if node != 0:
        search_node(tree[node][0])
        search_node(tree[node][1])

for case in range(1, int(input()) + 1):
    # 간선, 시작 노드
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    tree = [[0, 0] for _ in range(E)]

    for i in range(len(arr)//2):
        parent = arr[i*2]
        child = arr[i*2+1]

        if not tree[parent][0]:
            tree[parent][0] = child
        else :
            tree[parent][1] = child

    search_node(N)