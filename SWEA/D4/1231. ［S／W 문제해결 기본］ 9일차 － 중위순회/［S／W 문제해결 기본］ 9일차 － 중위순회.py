def str_to_int(number):
    try:
        return int(number)
    except ValueError:
        return number

def search(node):
    global word

    if node:
        search(arr[node][2])
        word += arr[node][1]
        search(arr[node][3])

for case in range(1, 11):
    N = int(input())
    arr = [[0, 0, 0, 0]] + [list(map(str, input().split())) for _ in range(N)]
    word = ''

    for node_arr in arr:
        for index, value in enumerate(node_arr):
            node_arr[index] = str_to_int(value)

            while len(node_arr) != 4:
                node_arr.append(0)
    search(1)
    
    print(f'#{case} {word}')