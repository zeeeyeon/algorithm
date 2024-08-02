T = int(input())

for case in range(1, T+1):
    total_page, A, B = map(int, input().split())
    flag = True

    while flag:

        low = 0
        high = total_page
        mid = (low + high) // 2


