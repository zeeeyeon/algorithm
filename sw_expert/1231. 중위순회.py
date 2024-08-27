for case in range(1, 11):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]

    # word = []
    # for i in range(len(arr)):
    #     word.append(arr[i][1])

    #isdecimal 안쓰는거 추천~
    a = list(map(list, zip(*arr)))
    print(a)