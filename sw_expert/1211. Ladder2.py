import sys
sys.stdin = open('Ladder2_input.txt')

def search_data(x, y):

    # 복사본의 모든 길을 True 설정
    copy_data = [[True] * LADDER_LENGTH for _ in range(LADDER_LENGTH)]

    copy_data[x][y] = False
    total = 1
    while x != LADDER_LENGTH - 1:
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 > nx or nx >= LADDER_LENGTH or 0 > ny or ny >= LADDER_LENGTH: continue
            if not copy_data[nx][ny]: continue
            if data[nx][ny]:
                total += 1
                copy_data[nx][ny] = False
                x, y = nx, ny

    return total

T = 10
# 아래, 오른쪽, 왼쪽
dxy = [[1, 0], [0, 1], [0, -1]]
for case in range(1, T+1):
    N = int(input())
    LADDER_LENGTH = 100
    data = [list(map(int, input().split())) for _ in range(LADDER_LENGTH)]

    total_list = []
    for y in range(LADDER_LENGTH):
        # 0인 경우 continue로 넘기기
        if not data[0][y]: continue

        # 길탐색 시작
        total = search_data(0,y)
        total_list.append([total, y])
        a = sorted(total_list, key=lambda x:(x[0], -x[1]))

    print(f'#{case} {a[0][1]}')
