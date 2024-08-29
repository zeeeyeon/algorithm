# def hex_to_binary(n):
#     number = ''
#
#     # 숫자가 아닌 16진수의 문자가 들어왔을 경우도 처리
#
#     if n == 0:
#         return 0
#
#     while n > 0:
#         remainder = n % 2
#         number += str(remainder)
#         n = n // 2
#
#     return number
#
#
# for case in range(1, int(input()) + 1):
#     N, HEX = map(int, input().split())

    # for item in HEX:
    #     hex_to_binary(item)

print(bin(int('47FE', 16)))