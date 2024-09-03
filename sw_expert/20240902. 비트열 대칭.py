# for T in range(1, int(input()) + 1):
#     N = int(input())
#     arr = list(map(int, input()))
#
#     result = 0
#     for i in range(1, N-1):
#         left, right, total = i-1, i+1, 1
#
#         while left >= 0 and right < N:
#             if arr[left] == arr[right]:
#                 total += 2
#                 left -= 1
#                 right += 1
#             else:
#                 result = max(result, total)
#                 break
#         result = max(result, total)
#
#     print(f'#{T} {result}')
#
#
arr = [1, 2, 3, 4, 5, 6]
path = []
n = 3

total = set()

def run(level, start):
    if level == n:
        print(*path)
        return

    for i in range(start, 7):
        path.append(i)
        run(level + 1, i)
        path.pop()

run(0, 1)
