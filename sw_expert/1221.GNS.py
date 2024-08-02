T = int(input())


# 선택 정렬
def selection_sort(arr, length):
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[j], arr[min_index] = arr[min_index], arr[j]

# 버블 정렬
def bubble_sort(arr, length):
    for i in range(length - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 카운팅 정렬 - 정수형으로 치환이 가능한 경우 사용가능(인덱스를 사용하기 때문)
# 구현하기

for case in range(1, T + 1):
    test_case, arr_length = input().split()
    # split()을 사용, 공백 기준으로 잘라 문자열 -> 리스트 변환
    arr = list(map(str, input().split()))

    # 딕셔너리 형태로 {텍스트 : 숫자} 형태로 저장
    letter_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    number_dict = {0 : "ZRO", 1 : "ONE", 2 : "TWO", 3 : "THR", 4 : "FOR", 5 : "FIV", 6 : "SIX", 7 : "SVN", 8 : "EGT", 9 : "NIN"}

    number_list = []
    for i in arr:
        # 원소를 뽑아서 letter_dict의 키값으로 사용, 나온 값을 다시 리스트에 저장
        number_list.append(letter_dict[i])

    # 정렬을 사용하여 정렬(배열, 길이)
    # selection_sort(number_list, int(arr_length))
    bubble_sort(number_list, int(arr_length))

    result = []
    for i in number_list:
        result.append(number_dict[i])

    a = ' '.join(result)
    print(f'#{test_case} {a}')





