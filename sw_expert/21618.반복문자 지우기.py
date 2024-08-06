T = int(input())

def check(s):
    stack = []

    for char in s:
        if len(stack) == 0:
            stack.append(char)
            continue
        else:
            if stack[-1] != char: stack.append(char)
            else:
                stack.pop()
                continue
    return len(stack)

for case in range(1, T+1):
    s = map(str, input())

    print(f'#{case} {check(s)}')
