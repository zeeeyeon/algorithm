import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
str_to_numbers = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

for case in range(1, T + 1):
    tc, words_length = input().split()
    words = input().split()
    length = len(numbers)

    # 카운팅 정렬 사용 (numbers 길이의 배열 생성 - 각 글자 갯수를 카운팅하기 위함)
    arr = [0] * length

    # input 요소들 하나씩 꺼내며 카운팅, arr 배열의 인덱스 번호를 이용 카운팅
    for word in words:
        arr[str_to_numbers[word]] += 1

    # arr = [700, 716, 719, 734, 679, 737, 674, 654, 724, 704]
    # numbers[index] * (벨류값 == 반복 횟수)
    new_list = []
    for index, value in enumerate(arr):
        new_list.extend([numbers[index]] * value)

    result = ' '.join(new_list)
    print(result)








