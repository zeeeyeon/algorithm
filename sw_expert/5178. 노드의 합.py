for case in range(1, int(input()) + 1):
    # 노드 수, 리프 노드 수, 값 출력할 노드 번호
    N, M, L = map(int, input().split())
    # 리프 노드 번호, 벨류 값
    arr = [list(map(int, input().split())) for _ in range(M)]
    result = 0
    tree = [0] * (N+1)

    for item in arr:
        tree[item[0]] = item[1]


    while N != L*2-1:
        child = N
        parent = N // 2
        tree[parent] += tree[child]
        N -= 1

    print(f'#{case} {tree[L]}')