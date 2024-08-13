def solution(priorities, location):
    # 주어진 프로세스의 길이
    length = len(priorities)
    # [index, 중요도가 적힌 프로세스]의 형식으로 배열 구성 ex. [0번 index, 중요도 2]
    arr = []
    for index, value in enumerate(priorities):
        arr.append([index, value])

    # print(arr)
    # 실행 횟수를 담을 변수
    # count = 0
    # while arr:
    #     print(arr)
    #     # 배열의 첫번째 요소를 제거, 변수에 담음
    #     current = arr.pop(0)
    #     print(current)
    #     # current의 중요도를 arr 요소들의 중요도와 하나씩 비교, current의 중요도보다 큰 값(더 중요도가 큰 값)이 존재한다면 뒤로 보내기(append)
    #     for i in range(len(arr)):
    #         #current = [0, 1] => 1이 중요도를 나타냄 => current[1] , arr[i][1]
    #         if current[1] < arr[i][1]:
    #             #
    #             arr.append(current)
    #             print(arr)
    #             count -= 1
    #
    #     count += 1
    #     print(count)
    #     if current[1] == location:
    #         return count
    count = 0
    while arr:
        for i in range(1, length):
            if arr[0][1] < arr[i][0]:
                temp = arr.pop(0)
                arr.append(temp)






# print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))