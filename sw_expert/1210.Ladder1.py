import sys
sys.stdin = open('input.txt')

T = 10
dxy = [[1, 0], [0, -1], [0, 1]]

def search_block(x, y):
    # 갔던 길 체크를 위한 복사본 만들기
    visited = [[False] * BLOCK_SIZE for _ in range(BLOCK_SIZE)]
    # 방문 한 곳은 True 표시
    visited[x][y] = True

    # x가 마지막 줄에 도달하는 순간 끝
    while x != BLOCK_SIZE - 1:

        # 3방향 체크, 아래 -> 왼쪽 -> 오른쪽 순서로 1, 0 체크
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            # 좌표를 벗어나면 continue
            if 0 > nx or ny < 0 or nx >= BLOCK_SIZE or ny >= BLOCK_SIZE: continue

            # arr = 0 -> not 0 -> not False -> True
            if not arr[nx][ny]: continue

            # 복사본으로 방문했던 곳인지 체크, 1 -> True
            if visited[nx][ny]: continue

            # 위의 예외를 다 통과하면 True, 복사본 표기
            visited[nx][ny] = True

            # 이동하는 곳으로 좌표 변경
            x, y = nx, ny

    if arr[x][y] == 2: return True
    return False

for case in range(1, T + 1):
    tc = int(input())
    BLOCK_SIZE = 100

    arr = [list(map(int, input().split())) for _ in range(BLOCK_SIZE)]

    result = -1

    # [0][y]의 시작점 : 0, 1 체크
    for y in range(BLOCK_SIZE):
        if arr[0][y] == 0: continue

        # 1인 경우, 아래 -> 왼쪽 -> 오른쪽 순서로 1, 0 체크 (메서드 만들기)
        if search_block(0, y):
            result = y
            break

    print(result)