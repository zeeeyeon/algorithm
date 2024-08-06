# 2
# ()(((()())(())()))(())
# (((()(()()))(())()))(()())

T = int(input())

for case in range(1, T+1):
    bracket = input()

    count = 0
    result = 0
    for i in bracket:
        if i == '(': count += 1
        else :
            count -= 1
            result += count

    print(f'#{case} {result}')
# def counting_check(stack):
#     matching_dict = {')': '('}
#
#     for i in stack[::-1]:
#         print(i)
#
#
# for case in range(1, T+1):
#     bracket = list(map(str, input())) + ['1']
#     # ['(', '(', '(', '1', '(', '1', '1', ')', ')', '(', '1', ')', '1', ')', ')', '(', '1', '1', ')', '1']
#     stack = []
#     for i in range(len(bracket)):
#         if bracket[i] == '(' and bracket[i+1] == ')': continue
#         if bracket[i-1] == '(' and bracket[i] == ')':
#             stack.append('1')
#             continue
#         stack.append(bracket[i])
#     #['(', '(', '(', '1', '(', '1', '1', ')', ')', '(', '1', ')', '1', ')', ')', '(', '1', '1', ')', '1']
#     if stack[-1] == '1':stack.pop()
#     if stack[0] == '1': stack.pop(0)
#
#     counting_check(stack)





