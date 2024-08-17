# 1을 만나면 count += 1, 0을 만나면 count, k 같은지 확인
# 같다면 total += 1, 다르면 count = 0 초기화
def check_one(arr, N, K):
    total = 0
    for i in range(N+1):
        count = 0
        for j in range(N+1):
            if arr[i][j] == 1: count += 1
            else:
                if count == K:
                    total += 1
                count = 0
    return total

for case in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]
    #  zip을 사용하여 반대로 돌리기
    arr_reverse = list(map(list, zip(*arr)))

    result = check_one(arr, N, K)
    result_reverse = check_one(arr_reverse, N, K)

    print(f'#{case} {result + result_reverse}')