def counting_check(bracket):

    count = 0
    stack = []
    for i in bracket:
        if i == '(':
            stack.append(i)
            continue
        if i == ')':
            stack.pop()
            count += 1
            continue
        if i == '1':
            count += len(stack)

    return count

T = int(input())

for case in range(1, T+1):
    bracket = list(map(str, input())) + ['1']
    # ['(', '(', '(', '1', '(', '1', '1', ')', ')', '(', '1', ')', '1', ')', ')', '(', '1', '1', ')', '1']
    stack = []
    for i in range(len(bracket)):
        if bracket[i] == '(' and bracket[i+1] == ')': continue
        if bracket[i-1] == '(' and bracket[i] == ')':
            stack.append('1')
            continue
        stack.append(bracket[i])
    #['(', '(', '(', '1', '(', '1', '1', ')', ')', '(', '1', ')', '1', ')', ')', '(', '1', '1', ')', '1']
    if stack[-1] == '1':stack.pop()
    if stack[0] == '1': stack.pop(0)

    count = counting_check(stack)

    print(f'#{case} {count}')