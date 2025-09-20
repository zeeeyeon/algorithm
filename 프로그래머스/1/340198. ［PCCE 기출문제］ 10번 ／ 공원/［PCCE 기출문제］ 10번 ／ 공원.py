def solution(mats, park):
    answer = 0
    m, n = len(park), len(park[0])
    mats.sort(reverse=True)
    max_cnt = 0

    def check(x, y):
        size = 0
        while x + size < m and y + size < n:
            # 사각형 내부에 -1이 아닌 것이 있으면 중단
            for i in range(x, x + size + 1):
                if park[i][y + size] != "-1":
                    return size
            for j in range(y, y + size + 1):
                if park[x + size][j] != "-1":
                    return size
            size += 1
        return size

    # 최대 사각형 변의 길이 찾기
    for i in range(m):
        for j in range(n):
            if park[i][j] == "-1":
                max_cnt = max(max_cnt, check(i, j))

    # mats 중에서 max_cnt 이하인 가장 큰 값 반환
    for mat in mats:
        if mat <= max_cnt:
            return mat

    return -1