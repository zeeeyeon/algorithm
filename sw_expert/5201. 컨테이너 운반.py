for case in range(1, int(input()) + 1):
    # N = container, M = truck
    N, M = map(int, input().split())
    # 화물 무게
    arr = list(map(int, input().split()))
    # 트럭의 적재용량
    weight = list(map(int, input().split()))

    arr.sort(reverse=True), weight.sort(reverse=True)

    result = []
    arr_index, weight_arr = 0, 0
    while True:
        if arr_index == N or weight_arr == M: break
        if arr[arr_index] > weight[weight_arr]: arr_index += 1
        else:
            result.append(arr[arr_index])
            arr_index += 1
            weight_arr += 1

    print(f'#{case} {sum(result)}')