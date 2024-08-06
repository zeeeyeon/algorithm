T = int(input())
matching_dict = {'}':'{', ')':'('}

def check(text):
    stack = []
    result = 0

    for char in text:
        if char in matching_dict.values():
            stack.append(char)
            continue
        if char in matching_dict.keys():
            if not stack or stack[-1] != matching_dict[char]:
                return result

            stack.pop()

    if len(stack) == 0: result = 1

    return result

for case in range(1, T+1):
    text = map(str, input())

    print(f'#{case}', check(text))

