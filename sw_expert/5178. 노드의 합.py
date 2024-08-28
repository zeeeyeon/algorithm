for case in range(1, int(input()) + 1):
    # 노드 수, 리프 노드 수, 값 출력할 노드 번호
    N, M, L = map(int, input().split())
    # 리프 노드 번호, 벨류 값
    arr = [list(map(int, input().split())) for _ in range(M)]

    tree = [0] * (N+1)
    for item in arr:
        tree[item[0]//2].append([item[1]])
        # print(tree[item[0]//2])
    print(tree)