def search(node):
    if tree[node]:
        if node*2<=N:search(node*2)
        if (node*2+1)<=N:search(node*2+1)
        result.append(tree[node])



for case in range(1, 2):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    tree = [0] * (N+1)
    result = []

    for i in range(N):
        if arr[i][1].isdecimal():
            tree[i+1] = int(arr[i][1])
        else :
            tree[i+1] = arr[i][1]

    search(1)