# def search_node(node):
#     global count
#
#     if node != 0:
#         count += 1
#         search_node(tree[node][0])
#         search_node(tree[node][1])
#
# for case in range(1, int(input()) + 1):
#     # 간선, 시작 노드
#     E, N = map(int, input().split())
#     arr = list(map(int, input().split()))
#     count = 0
#
#     tree = [[0, 0] for _ in range(E + 2)]
#
#     for i in range(len(arr)//2):
#         parent = arr[i*2]
#         child = arr[i*2+1]
#
#         if not tree[parent][0]:
#             tree[parent][0] = child
#         else :
#             tree[parent][1] = child
#     search_node(N)
#
#     print(f'#{case} {count}')


def move():
    N, K = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    now = 1
    while True:
        if arr[now] == 1:
            now += K
            if now >= N:
                return N
        elif arr[now] == 0:
            for step in range(1, K):
                if arr[now-step] == 1:
                    now -= step
                    break
            else:
                return now


for tc in range(1, int(input())+1): print(f'#{tc} {move()}')