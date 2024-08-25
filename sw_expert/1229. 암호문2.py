


def checked_bingo(arr):
    count, sum_v = 0, 0

    while count != 3:
        for i in arr:
            if i.count(99) == LENGTH: count += 1

        arr_reverse = list(zip(*arr))
        for i in arr_reverse:
            if i.count(99) == LENGTH: count += 1

        number_list = [0, 1, 2, 3, 4]
        for i in number_list:
            if arr[i][i] == 99:
                sum_v += 1
            if sum_v == LENGTH: count += 1

        sum_v = 0

        for i in number_list:
            for j in number_list[::-1]:
                if arr[i][j] == 99:
                    sum_v += 1
            if sum_v == LENGTH: count += 1

    return True

def bingo(arr, checked):

    count = 0
    for i in range(LENGTH):
        for j in range(LENGTH):

            for x in range(LENGTH):
                for y in range(LENGTH):
                    if arr[x][y] == checked[i][j]:
                        arr[x][y] = 99
                        count += 1
                        if checked_bingo(arr):
                            return count


LENGTH = 5
arr = [list(map(int, input().split())) for _ in range(LENGTH)]
checked = [list(map(int, input().split())) for _ in range(LENGTH)]

a = bingo(arr, checked)
print(a)