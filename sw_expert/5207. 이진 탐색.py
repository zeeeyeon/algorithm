def search_binary(low, high, target, flag):
    global total
    mid = (low + high) // 2

    if target == arr[mid]:
        total += 1
        return

    elif target > arr[mid]:
        direction = 1
        if direction == flag: return
        search_binary(mid + 1, high, target, direction)

    elif target < arr[mid]:
        direction = -1
        if direction == flag: return
        search_binary(low, mid - 1, target, direction)

for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    new_arr = list(map(int, input().split()))
    target_arr = list(map(int, input().split()))

    arr = sorted(new_arr)
    length = len(target_arr)

    low, high = 0, len(arr) - 1
    total = 0

    for i in range(length):
        search_binary(low, high, target_arr[i], flag=0)

    print(f'#{T} {total}')