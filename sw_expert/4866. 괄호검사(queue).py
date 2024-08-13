T = int(input())
pair = {'}':'{', ')':'('}

def check(text):
    stack = []
    result = 0
    for char in text:
        if char in pair.values():
            stack.append(char)
            continue

        if char in pair.keys():
            if not stack and stack[-1] != pair[char]:
                return result

            stack.pop()

    if len(stack) == 0: result = 1
    return result

for case in range(1, T+1):
    text = map(str, input())

    print(f'#{case}', check(text))