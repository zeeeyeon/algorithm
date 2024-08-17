import sys
sys.stdin = open("input.txt")

def check_arr(length, arr):
    for arr_ in arr:
        # 최대한 들어 갈 수 있는 시작 지점
        for i in range(N-length+1):
            # 반 나눠서 대칭에 맞는 부분이 일치한지 체크
            for j in range(length // 2):
                if arr_[i+j] != arr_[i+length-1-j]: break
            else : return True
    return False

for _ in range(1, 11):
    case = int(input())
    N = 100
    arr = [input() for _ in range(N)]
    arr_reverse = [''.join(i) for i in zip(*arr)]

    # 제일 큰 회문의 길이 출력
    for i in range(N, 1, -1):
        if check_arr(i, arr) or check_arr(i, arr_reverse):
            print(f'#{case} {i}')
            break