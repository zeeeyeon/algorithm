import sys
sys.stdin = open('input.txt')

T = 10
# 위쪽 왼쪽 오른쪽
dxy = [[-1, 0], [0, -1], [0, 1]]

def search_block(x, y):

    while x != 0:
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            # 범위를 벗어 나는 경우
            if nx < 0 or nx >= BLOCK_SIZE or ny < 0 or ny >= BLOCK_SIZE: continue
            # 1이 아닐 경우
            if not arr[nx][ny]: continue
            # 좌표 대입
            x, y = nx, ny
            # !!!!! 지나온 길을 0으로 변경
            arr[x][y] = 0

    return y

for case in range(1, T + 1):
    tc = int(input())
    BLOCK_SIZE = 100

    arr = [list(map(int, input().split())) for _ in range(BLOCK_SIZE)]

    # 도착지점, arr[99][y] y의 값을 먼저 찾기
    for y in range(BLOCK_SIZE):
        # 2일 경우 탈출
        if arr[99][y] == 2:
            result = search_block(99, y)

    print(result)