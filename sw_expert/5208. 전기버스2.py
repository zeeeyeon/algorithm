def dfs(index, count, battery):
    global total

    if total <= count: return

    if index == length:
        total = min(total, count)
        return

    if battery > 0:
        dfs(index + 1, count, battery - 1)

    dfs(index + 1, count + 1, charge[index] - 1)


for T in range(1, int(input()) + 1):
    charge = list(map(int, input().split()))
    length = charge[0]
    total = length

    # 2번째 정류장부터 시작, 교체 횟수, 배터리 잔량
    dfs(2, 0, charge[1] - 1)

    print(f'#{T} {total}')
