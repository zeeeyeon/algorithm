T = int(input())
for case in range(1, T + 1):
    number = int(input())
    carrots = list(map(int, input().split()))

    count = 1
    max_count = 1
    for i in range(number-1):
        if carrots[i] < carrots[i+1]:
            count += 1
            if max_count < count : max_count = count
        else : count = 1

    print(f'{case} {max_count}')

    # count = 0
    # result = [0]
    # for i in range(1, number):
    #     if carrots[i - 1] < carrots[i]: count += 1
    #     else : count = 0
    #     result.append(count)
    #
    # max_equal = []
    # max_v = max(result)
    # for i in range(len(result)):
    #     if max_v <= result[i]: max_equal.append(carrots[i])
    #
    # if max(result) == 0: result_number = 1
    # else : result_number = max(max_equal)
    #
    # print(f'#{case} {result_number}')
