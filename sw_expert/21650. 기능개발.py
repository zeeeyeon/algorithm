import math

def solution(progresses, speeds):
    time = [math.ceil((100-progresses[i]) / speeds[i]) for i in range(len(progresses))]

    count = 1
    # 변수에 넣어주기 ! (선형적으로 움직이기때문)
    current_time = time[0]
    result = []

    for i in range(1, len(time)):
        if current_time < time[i]:
            result.append(count)
            count = 1
            current_time = time[i]
        else:
            count += 1
    result.append(count)
    return result

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