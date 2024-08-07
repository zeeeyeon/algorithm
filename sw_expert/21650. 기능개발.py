# def solution(progresses, speeds):
#     time = []
#     for i in range(len(progresses)):
#         if progresses[i] % speeds[i] == 0:
#             time.append((100 - progresses[i]) // speeds[i])
#         else:
#             time.append(((100 - progresses[i]) // speeds[i]) + 1)
#
#     answer = []
#     i = 0
#     count = 1
#     for i in range(len(time) - 1):
#         if time[i] >= time[i+1]: count += 1
#         else:
#             answer.append(count)
#             count = 1
#     answer.append(count)
#
#     return answer

