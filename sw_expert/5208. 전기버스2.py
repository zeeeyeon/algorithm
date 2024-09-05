def dfs(index, current_count):
    global total_count

    if current_count >= total_count: return

    if index == index + 1:
        total_count = min(total_count, current_count)
        return

    for i in range(index, length):
        charge


for T in range(1, int(input()) + 1):
    charge_arr = list(map(int, input().split()))

    charge = []
    for i in range(len(charge_arr)):
        if i == 0: length = charge_arr[0]
        else: charge.append(charge_arr[i])

    total_count = 0
    dfs(0, 0)
