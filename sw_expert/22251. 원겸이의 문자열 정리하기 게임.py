def find_ascii(stack):
    ascii_count = 0
    ascii_stack = set()

    for i in range(1, len(stack)):
        if ord(stack[i-1]) + 1 == ord(stack[i]):
            ascii_stack.add(stack[i-1])
            ascii_stack.add(stack[i])
        else:
            ascii_count += len(ascii_stack)
            ascii_stack = set()

    ascii_count += len(ascii_stack)
    return ascii_count

for case in range(1, int(input()) + 1):
    word = input()

    stack = []
    before_word = ''
    count = 0
    for i in word:
        if not stack:
            if before_word == i:
                count += 1
                continue
            stack.append(i)
        else:
            if stack[-1] == i:
                before_word = stack.pop()
                count += 2
            else :
                if before_word == i: count += 1
                else :stack.append(i)

    if stack:
        count += find_ascii(stack)

    print(f'#{case} {count}')

