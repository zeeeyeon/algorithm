T = int(input())

for case in range(1, T+1):
    number = int(input())
    carrots = list(map(int, input().split()))

    result = []
    count = 0
    for i in range(1, number):
        if carrots[i-1] < carrots[i]:
            count += 1
        else :
            count = 0
        result.append(count)

    # 횟수가 같은 경우 큰 값 체크
    max_v = max(result)
    index = [index for index, value in enumerate(result) if max_v == value]

    big_carrot = 0
    for i in index:
        if big_carrot < carrots[result.index(big_carrot) + 1]:
            big_carrot = carrots[result.index(big_carrot) + 1]

    if max(result) == 0: big_carrot = 1
    print(big_carrot)
