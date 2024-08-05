T = int(input())

for case in range(1, T + 1):
    # 배열의 길이
    N = int(input())
    # 주어진 정수 배열 + [0] , out of index 나올 경우를 대비
    Ai = list(map(int, input().split())) + [0]

    up_list = []
    # 제일 처음 요소를 미리 넣어놓음, 크기가 클 경우, 다음 요소를 넣을 예정
    up = [Ai[0]]
    for i in range(N):
        # 다음 수의 크기가 작은 경우, 리스트 안이 초기화 됐으므로 돌아온 요소의 값을 넣어줌
        if up == []: up.append(Ai[i])
        # 다음 수의 크기가 클 경우 up 리스트에 요소 계속 더하기
        if Ai[i] <= Ai[i + 1]:
            up.append(Ai[i + 1])
        else:
            # 다음 수의 크기가 작은 경우 모았던 리스트를 통으로 올려버린 후, 리스트를 초기화
            up_list.append(up)
            up = []

    new_list = []
    for inner in up_list:
        # 리스트의 첫번째 요소는 제일 작은 값, 마지막은 제일 큰 값.
        min_v = min(inner)
        max_v = max(inner)
        if len(inner) == 1: continue
        length = len(inner)
        avg = (max_v - min_v) // len(inner)
        new_list.append([length, avg])

    sorted_list = sorted(new_list, key=lambda x: (x[1], -x[0]))

    if len(sorted_list) == 0: result = 0
    else : result = sorted_list[0][0]

    print(f'#{case} {result}')
