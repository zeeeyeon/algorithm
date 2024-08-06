def check(data):
    stack = []
    matching_dict = {')': '('}
    result = -1

    for char in data:
        if char in matching_dict.values():
            stack.append(char)
            continue
        if char in matching_dict.keys():
            if not stack or stack[-1] != matching_dict[char]:
                return result

            stack.pop()

    if len(stack) == 0:
        result = 1

    return result

T = int(input())

for case in range(1, T + 1):
    data = input()

    print(f'#{case}', check(data))
