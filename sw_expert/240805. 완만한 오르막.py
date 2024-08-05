T = int(input())

for case in range(1, T + 1):
    # 배열의 길이
    N = int(input())
    # 주어진 정수 배열 + [0] , out of index 나올 경우를 대비
    Ai = list(map(int, input().split())) + [0]

    up_list = []
    # 제일 처음 요소를 미리 넣음
    up = [Ai[0]]
    for i in range(N):
        # 현재 숫자와 비교하여 다음 숫자가 작은 경우, 리스트 안이 초기화 됐기 때문에 현재 요소 값을 넣어줌
        if up == []: up.append(Ai[i])
        # 다음 숫자의 크기가 클 경우 up에 계속 더하기
        if Ai[i] <= Ai[i + 1]:
            up.append(Ai[i + 1])
        else:
            # 다음 숫자의 크기가 작은 경우 up에 모았던 요소를 up_list에 올린 후,  up 초기화
            up_list.append(up)
            up = []

    new_list = []
    for inner in up_list:
        # 리스트 첫번째 요소는 제일 작은 값, 마지막 제일 큰 값.
        min_v = inner[0]
        max_v = inner[-1]
        # inner 에 요소가 없으면 continue
        if len(inner) == 1: continue
        # inner 에 요소가 있으면 길이 넣기
        length = len(inner)
        # 경사 구하기
        avg = (max_v - min_v) // len(inner)
        # 새로운 리스트 [길이, 경사] 넣기(리스트 형식으로 넣기)
        new_list.append([length, avg])

    # x[1]: 경사를 기준으로 오름차순, -x[0]: 경사도가 같은 경우 length가 큰 값으로 출력 (length 내림차순으로 출력)
    sorted_list = sorted(new_list, key=lambda x: (x[1], -x[0]))

    # 오르막이 존재하지 않는 경우 == 리스트 길이가 0인 경우 result = 0
    if len(sorted_list) == 0: result = 0
    # 그 외 오르막이 존재하는 경우 길이 출력
    else : result = sorted_list[0][0]

    print(f'#{case} {result}')
