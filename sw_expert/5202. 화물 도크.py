for case in range(1, int(input()) + 1):
    N = int(input())
    work_time = [list(map(int, input().split())) for _ in range(N)]

    work = sorted(work_time, key=lambda x:(x[1], x[0]))

    end_time, count, result = work[0][1], 1, []
    for i in range(N):
        if end_time <= work[i][0]:
            end_time = work[i][1]
            count += 1

    print(f'#{case} {count}')