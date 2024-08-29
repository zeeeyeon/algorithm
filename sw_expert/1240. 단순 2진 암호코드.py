for C in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    dict = {
        '1011000': 0,
        '1000110': 5,
        '1001100': 1,
        '1111010': 6,
        '1100100': 2,
        '1101110': 7,
        '1011110': 3,
        '1110110': 8,
        '1100010': 4,
        '1101000': 9
    }
    start_index = 0
    for i in range(N):
        if sum(arr[i]):
            start_index = i
            break

    new_arr = arr[i][::-1]
    num_list = ''
    index = new_arr.index(1)

    check_code = [0]
    for i in range(index, index+56):
        num_list += str(new_arr[i])
        if len(num_list) == 7:
            check_code.append(dict[num_list])
            num_list = ''

    odd, even = 0, 0
    for i in range(9):
        if i % 2 == 0: odd += check_code[i]
        else: even += check_code[i]

    result = 0
    if ((odd * 3) + even) % 10 == 0: result = odd + even
    else : result = 0

    print(f'#{C} {result}')