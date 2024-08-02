T = int(input())

for case in range(1, T+1):
    input_str = str(input())
    palindrome = input_str[::-1]
    result = 0

    if input_str == palindrome: result = 1
    else: result = 0

    print(f'#{case} {result}')