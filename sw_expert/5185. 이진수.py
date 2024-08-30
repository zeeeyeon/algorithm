dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
hex_list = ['A', 'B', 'C', 'D', 'E', 'F']

def hex_to_binary(n):
    number = ''

    #  0일 경우 0000으로 넣어줘야 함 !
    if n == 0:
        return '0000'

    while n > 0:
        remainder = n % 2
        number += str(remainder)
        n = n // 2

    if len(number) < 4:
        while len(number) != 4:
            number += '0'

    return number[::-1]

for case in range(1, int(input()) + 1):
    N, HEX = map(str, input().split())
    result = ''

    for item in HEX:
        if item in hex_list:
            item = dict[item]
        result += hex_to_binary(int(item))

    print(f'#{case} {result}')