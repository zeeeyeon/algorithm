T = int(input())

for case in range(1, 2):

    N = int(input())
    arr = list(map(int, input().split()))

    # 선택 정렬(121ms)
    for i in range(N-1):
       min_index = i
       for j in range(i+1, N):
           if arr[min_index] > arr[j]:
              min_index = j

       arr[i], arr[min_index] = arr[min_index], arr[i]

    # 버블 정렬(126ms)
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # 카운팅 정렬 (108ms)
    # 1. 최대값보다 1크게 만들기
    max_v = max(arr)
    data = [0] * (max_v + 1)

    # 2. 순회하면서 순서대로 넣어주기
    for i in range(N):
        data[arr[i]] += 1

    # 3. 길이만큼의 배열 만들어 주기
    new_arr = [0] * len(arr)

    # 4. 순회하면서 넣어주기
    index = 0
    for i in range(len(data)):
        for _ in range(data[i]):
            new_arr[index] = i
            index += 1

    print(f'#{case}', end=' ')
    print(*arr)