from collections import deque
import sys
sys.stdin = open('a.txt')

def search():
    queue = deque()
    for i in range(N):
        if in_degree[i] == 0:
            queue.append(i)

    # 최종 목표는 최소 학기
    # 모든 과목을 완료 했는지 알기 위해서는
    completed = 0   # 완료된 과목이 몇개냐 비교용
    semester = 0    # 총 소요된 학기는?

    while queue:    # 조사 대상이 남아 있는 동안
        semester += 1
        #현재 학기에 삽입된 모든 진입차수가 0인 과목들 제거
        for _ in range(len(queue)):
            current = queue.popleft()
            completed += 1      # 과목완료

            # 나를 진입차수로 보고 있는 다음번 노드 번호 투입
            for next in graph[current]:
                # 진입차수 하나 제거
                in_degree[next] -= 1
                if in_degree[next] == 0:
                    queue.append(next)

    if completed == N:
        return semester
    else :
        return -1

T = int(input())
for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))[1:] for _ in range(N)]

    graph = [[] for _ in range(N)]
    # 나에게 들어 올 수 있는 진입 차수
    in_degree = [0] * N

    for i in range(N):
        pre = arr[i]
        for p in pre:
            # 선수 과목 -> 현재 과목으로 갈 수 있음을 인접 리스트에 표기
            graph[p-1].append(i)
            # 해당 현재 과목의 진입차수 += 1
            in_degree[i] += 1

    result = search()

    print(f'#{case} {result}')