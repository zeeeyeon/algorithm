arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]

# left : 왼쪽 정렬 대상 시작 지점
# right : 오른쪽 정렬 대상 시작 지점

# hoare 방식의 배열 쪼개기
def hoare_partition(left, right):       # 개념적으로 배운 quick sort
    pivot = arr[left]
    left += 1



def quick_sort(left, right):
    # 조사 대상이 하나 이하가 된다면, 더 이상 조사 할 수 없음
    if left >= right: return

    # 호어 방식의 정렬을 위해서는, 정렬을 위한 배열을
    # 영역별로 구분 지을 수 있어야 하고,
    # 호어 방식의 파티션 구분 결과로 얻은 index 지점을 pivot으로 보겠다.
    pivot_index = hoare_partition(left, right)
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]

    quick_sort(left, pivot_index - 1)
    quick_sort(pivot_index + 1, right)