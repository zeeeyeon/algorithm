def binary_search(total, page):
    count = 1
    start = 1
    end = total

    while page != int((start + end) / 2):

        if int((start + end) / 2) < page :
            start = int((start + end) / 2)
        else :
            end = int((start + end) / 2)

        count += 1

    return count

T = int(input())
for case in range(1, T+1):
    # page, a가 도달할 값, b가 도달할 값
    # 1000 299 578
    P, A, B = map(int, input().split())

    a = binary_search(P, A)
    b = binary_search(P, B)

    if a < b: print('A')
    if a > b: print('B')
    if a == b: print('0')