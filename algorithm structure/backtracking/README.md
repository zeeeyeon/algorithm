# 백트래킹(Backtracking) 🌠

> ## 개념
> - 여러 가지 선택지(옵션)들이 존재하는 상황에서 한가지를 선택
> - 선택이 이루어지면 새로운 선택지들의 집합이 생성
> - 선택을 반복하면서 최종 상태에 도달 (올바른 선택을 계속하면 목표에 도달)

> ### 백트래킹과 깊이 우선 탐색과의 차이
> - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도 횟수를 줄임 (Prunning 가지치기)
> - 깊이 우선 탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
> - 깊이 우선 탐색을 가하기에는 경우의 수가 너무 많음. N! 가지의 경우의 수를 가진 문제는 처리 불가능
> - 백트래킹 알고리즘을 적용하면 경우의 수는 줄지만 최악의 경우에는 지수함수 시간을 요하므로 처리 불가능

> ### 절차
> - 1. 상태 공간 트리의 깊이 우선 검색을 실시
> - 2. 각 노드가 유망한지(설계 단계에서 유망하지 않은 경우를 생각하고 구현)
> - 3. 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속한다.

```
def check(row):
    for col in range(row):
        if visited[row] == visited[col]:
            return False

        # 열과 행의 차이가 같다 == 현재 col 의 좌우 대각선이다
        if abs(visited[row] - visited[col]) == abs(row - col):
            return False

    return True


def dfs(row):
    global cnt

    if row == N:
        cnt += 1
        return

    for col in range(N):
        # visited[row][col] = 1      이렇게 사용 x
        # 이차원 배열을 사용하지않고 해당 행의 몇번 째 열에 배치 했다라고 visited 표시        
        visited[row] = col
        if not check(row):
            continue

        dfs(row + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [0] * N
    cnt = 0

    dfs(0)
    print(f'#{tc} {cnt}')
```