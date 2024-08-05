T = int(input())
for case in range(1, T+1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    sorted_score = sorted(score, reverse=True)

    total = 0
    for i in range(K):
        total += sorted_score[i]

    print(f'#{case} {total}')



