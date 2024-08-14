for case in range(1, int(input()) + 1):
    text = input()

    ball = ['(|', '|)', '()']

    ball_count = 0
    for i in range(len(text)-1):
         if text[i : i+2] in ball: ball_count += 1

    print(f'#{case} {ball_count}')