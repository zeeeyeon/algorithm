# import sys, copy
# sys.stdin = open('input.txt', 'r')
#
#
# def crack(x, y, copy_arr):
#
#
#
#
#
# for T in range(1, int(input()) + 1):
#     N, W, H = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(H)]
#
#     copy_arr = copy.deepcopy(arr)
#
#     for i in range(W):
#         for j in range(H):
#             if copy_arr[i][j] != 0:
#                 crack(i, j, copy_arr)