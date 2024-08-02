T = int(input())

for case in range(1, T + 1):

    N = int(input())
    arr = list(map(int, input().split()))

    # 선택 정렬
    for i in range(N-1):
       min_index = i
       for j in range(i+1, N):
           if arr[min_index] > arr[j]:
              min_index = j

       arr[i], arr[min_index] = arr[min_index], arr[i]

    # 버블 정렬
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(f'#{case}', end=' ')
    print(*arr)