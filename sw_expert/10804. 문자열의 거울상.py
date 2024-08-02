T = int(input())
for case in range(1, T+1):
    letter_dict = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}

    input_str = str(input())
    new_str = ''

    for i in input_str[::-1]:
        new_str += letter_dict[i]

    print(f'#{case} {new_str}')
