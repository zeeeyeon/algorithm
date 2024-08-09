'''
1. 열린 괄호가 나오면 스택에 추가
2. 숫자가 나오면 결과에 추가
3. 닫힌 괄호, 열린 괄호가 나올때까지 결과에 추가
4. 연산자, 스택 top 연산자와 비교
4-1. 스택에 현재 연산자와 비교하여 우선순위가 같거나 높으면 꺼내서 결과에 추가
4-2. 4-1이 아니라면 현재 연산자를 스택에 추가
5. 남은 연산자 모두 결과에 추가
'''


def infix(formula):
    op_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []
    result = []

    for i in formula:
        if i.isdigit():
            result.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            top = stack.pop()
            while top != '(':
                result.append(top)
                top = stack.pop()
        else:
            while stack and op_dict[stack[-1]] >= op_dict[i]:
                result.append(stack.pop())
            stack.append(i)

    while stack:
        result.append(stack.pop())

    return ''.join(result)


T = int(input())
for case in range(1, T + 1):
    formula = list(map(str, input().strip()))

    numbers = infix(formula)
    print(f'#{case} {numbers}')
