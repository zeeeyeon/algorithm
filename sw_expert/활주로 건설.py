# def find_load(arr):
#
#     height_box = []
#     height_box_2 = ''
#     for number in arr:
#         # 첫번째 무조건 넣기
#         if not height_box:
#             height_box.append(number)
#             continue
#
#         # 붙어있는 지형과 같으면 넣기
#         if height_box[-1] == number:
#             height_box.append(number)
#         else :
#             # 붙어있는 지형과 다를 경우
#             # 차이가 1보다 클 때
#             if (height_box[-1] - number) not in [-1, 1]: break
#             if (height_box[-1] - number) == -1
#
#
#             if (height_box[-1] - number) == -1 and len(height_box) < N: break
#             if (height_box[-1] - number) == 1:
#
#
#         # 같은 숫자의 지형인 경우
#         if len(height_box) == N:
#             return 1


def find_load(arr):
    height_box = []
    height_box_2 = ''
    for i in range(arr):
        # 첫번째 무조건 넣기
        if not height_box:
            height_box.append(arr[i])
            continue

        # 붙어있는 지형과 같으면 넣기
        if height_box[-1] == arr[i]:
            height_box.append(arr[i])
        else:
            # 붙어있는 지형과 다를 경우
            # 차이가 1보다 클 때
            if (height_box[-1] - arr[i]) not in [-1, 1]: break

            if (height_box[-1] - arr[i]) == -1 and len(height_box) < N: break
            if (height_box[-1] - arr[i]) == 1:
                height_box.clear()
                height_box.append(arr[i-1])

        # 같은 숫자의 지형인 경우
        if len(height_box) == N:
            return 1



for case in range(1, int(input()) + 1):
    # X: 경사로의 x길이 값
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    reverse_arr = [list(map(list, zip(*arr)))]
    result = 0
    # step = 1
    # for i in range(N):
    #     for j in range(N-1):
    #         if arr[i][j] == arr[i][j+1]: step += 1
    #         else :
    #             if step < X: break
    #             if abs(arr[i][j] - arr[i][j+1]) > 1: break
    #             if abs(arr[i][j] - arr[i][j+1]) == 1:


    # step = []
    # for i in range(N):
    #     step.append(arr[i][0])
    #     for j in range(N-1):
    #         if arr[i][j] == arr[i][j+1]: step.append(arr[i][j])
    #         else :
    #             if len(step) >= X and (arr[i][j] - arr[i][j+1]) == -1:
    #                 step.clear()
    #                 step.append(arr[i][j+1])
    #                 continue

    '''
     안되는 조건
     1. 붙어있는 지형의 경사로 차이 1 넘는 경우 3 3 1
     2. 경사로 차이가 1인데 그 다음 경사로의 길이가 X보다 작을때 (같거나 크면 됨- 이것도 다른 조건 필요) 3 3 2 2 3 3
     3. 근데 3 3 2 2 1 1 은 가능
     4. 3 2 2 2 3 의 경우 (3 2 2 2 2 3은 가능)
    '''




# 1
# 6 2
# 3 3 3 2 1 1
# 3 3 3 2 2 1
# 3 3 3 3 3 2
# 2 2 3 2 2 2
# 2 2 3 2 2 2
# 2 2 2 2 2 2