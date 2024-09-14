from collections import deque

def dfs(start):
    visited.add(start)
    print(start, end=' ')

    for next in sorted(tree[start]):
        if next not in visited:
            dfs(next)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for next in tree[node]:
            if next not in visited:
                queue.append(next)
                visited.add(next)

N, M, start = map(int, input().split())
tree = [[] for _ in range(N + 1)]
visited = set()

for _ in range(M):
    index, value = map(int, input().split())
    tree[index].append(value)
    tree[value].append(index)

for i in tree:
    i.sort()

dfs(start)
visited = set()
print()
bfs(start)
