def number_swap(digits):

    min_num, max_num = min(digits), max(digits)

    min_idx, max_idx = 0, 0
    for i in range(len(digits)):
        if digits[i] == max_num:
            max_idx = i

    for i in digits:
        if i == digits[i]: continue
        else: swap(i, digits[max_idx])

for C in range(1, int(input()) + 1):
    score, swap = map(int, input().split())

    score_str = str(score)
    digits = [int(digits) for digits in score_str]

    print(digits)

    number_swap(digits)




