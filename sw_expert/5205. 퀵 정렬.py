def quick_sort(div_arr):
    if len(div_arr) <= 1:
        return div_arr
    else:
        pivot = div_arr[0]  # 왼쪽을 피봇으로 잡음.
        left, right = [], []
        for i in range(1, len(div_arr)):
            if div_arr[i] < pivot:
                left.append(div_arr)
            else:
                right.append(div_arr[i])
        return [*quick_sort(left), pivot, *quick_sort(right)]

for T in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{T} {quick_sort(arr)}')
    # print(f'#{T} {sorted(arr)[N//2]}')