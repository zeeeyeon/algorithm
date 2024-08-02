T = int(input())

for case in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    length1 = len(str1)
    length2 = len(str2)

    result = 0
    str_list = []
    for i in range(length2):
        if str2[i] == str1[0]: str_list.append(str2[i:i+length1])
    print(str_list)

    for i in str_list:
        print()
        if i == str1: result = 1

    print(f'#{case} {result}')
