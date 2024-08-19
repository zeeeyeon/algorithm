for T in range(1, int(input()) + 1):
    LENGTH = int(input())
    arr = list(map(int, input().split()))

    copy_arr = [0] * LENGTH

    count = 0
    for i in range(LENGTH):
        if arr[i] == copy_arr[i]: continue
        else :
            if i == 0:
                for j in range(0, LENGTH, 1):
                    copy_arr[j] = 1 - copy_arr[j]
            else:
                for j in range(i, LENGTH, i+1):

                    copy_arr[j] = 1 - copy_arr[j]
            count += 1
            if arr == copy_arr: break

    print(f'#{T} {count}')