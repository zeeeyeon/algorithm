T = int(input())
for case in range(1, 2):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    color = ['W’, ‘B’, ‘R']

    total = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            count = 0

            # 흰색의 영역이 끝나는 지점을 i라고 생각하고 계산 => i의 범위는 (0,i+1)
            # 선택된 열의 흰색 타일 수를 카운트에 더해줌
            for select in range(i+1):
                count += arr[select].count('W')
            # 파란색 영역 끝나는 지점을 j라고 생각하고 계산 => j의 범위는 (i+1, j+1)
            for select in range(i+1, j+1):
                count += arr[select].count('B')
            # 빨간색 영역 끝나는 지점은 (j+1, N)
            for select in range(j+1, N):
                count += arr[select].count('R')

            # 범위를 바꿔가면서 칠해진 개수가 최대일 경우 업데이트 하여 가장 큰 값을 넣어줌
            total = max(total, count)
    print(f'{case} {N*M-total}')