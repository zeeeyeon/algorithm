from collections import deque

def bfs(start):
    queue = deque([(start, 0)])

    visited = set([start])

    while queue:
        current_v, current_count = queue.popleft()

        if current_v == M:
            return current_count


        for op in op_list:
            if op == '+1':
                next_v = current_v + 1
            if op == '-1':
                next_v = current_v - 1
            if op == '*2':
                next_v = current_v * 2
            if op == '-10':
                next_v = current_v - 10

            if next_v not in visited:
                if next_v > 1000000: continue
                if next_v <= 0: continue
                visited.add(next_v)
                queue.append((next_v, current_count + 1))

for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    op_list = ['+1', '-1', '*2', '-10']

    count = bfs(N)
    print(f'#{T} {count}')