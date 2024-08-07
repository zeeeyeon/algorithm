import math

def solution(progresses, speeds):
    time = []
    for i in range(len(progresses)):
        time.append(math.ceil(100 - progresses[i]) // speeds[i])

    print(time)
    answer = []
    count = 1
    for i in range(1, len(time)):
        if time[i-1] < time[i]:
            answer.append(count)
            count = 1
        else :
            count += 1
    answer.append(count)
    return answer

    print(solution([93, 30, 55], [1, 30, 5]))
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# def solution(progresses, speeds):
#     answer = []
#     COMPLETE = 100
#     count = 0
#
#     while speeds:
#         for i in range(len(speeds)):
#             # 한 사이클 돌았을 때 첫번째 요소가 100이 넘지 않으면 100이상 될때까지 계속 사이클 돌리기
#             if progresses[i] >= COMPLETE: continue
#             progresses[i] += speeds[i]
#
#         while progresses and progresses[0] >= COMPLETE:
#             progresses.pop(0)
#             count += 1
#
#             if progresses and progresses[0] < COMPLETE:
#                 answer.append(count)
#                 count = 0
#
#             elif len(progresses) == 0: answer.append(count)
#             speeds.pop(0)
#
#     return answer