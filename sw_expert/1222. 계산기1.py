T = 10
for case in range(1,T+1):
    length = int(input())
    arr = list(map(str, input().strip()))

    stack = []
    total = 0
    for i in arr:
        if i.isdecimal():
            i = int(i)
            stack.append(i)

        if len(stack) == 2:
            total = stack[0] + stack[-1]
            stack.clear()
            stack.append(total)

    print(f'#{case} {total}')
