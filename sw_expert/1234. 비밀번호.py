def check_stack(data):

    stack = []
    for char in data:
        if len(stack) == 0:
            stack.append(char)
        else :
            if stack[-1] != char: stack.append(char)
            else : stack.pop()

    return ''.join(stack)

T = 10

for case in range(1, T+1):
    N, data = map(str, input().split())

    print(f'#{case} {check_stack(data)}')