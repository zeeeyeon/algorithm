for case in range(1, 2):
    length = int(input())
    arr = list(map(str, input().strip()))

    op_dict = {'+': 1, '*': 2}
    stack = []
    op = []

    for i in arr:
        if i.isdecimal():
            i = int(i)
            stack.append(i)
        else :
            if not op: op.append(i)
            else :
                if op_dict[op[-1]] < op_dict[i]: op.append(i)
                else:
                    v = op.pop()
                    stack.append(v)
                    op.append(i)
    while op:
        stack.append(op.pop())

    result = []
    total = 0

    for i in stack:
        if isinstance(i, int):
            result.append(i)
        elif i == '+':
            v2 = result.pop()
            v1 = result.pop()
            total = v1 + v2
            result.append(total)
        elif i == '*':
            v2 = result.pop()
            v1 = result.pop()
            total = v1 * v2
            result.append(total)

    print(f'#{case} {result[0]}')