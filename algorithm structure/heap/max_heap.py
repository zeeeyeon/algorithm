'''
7
20 15 19 4 13 11 17

7
20 15 19 4 13 11 23
'''
'''
 삽입
 1. 마지막에 삽입
 2. 자리 찾아가기
 
 삭제 
 1. 루트에 마지막 노드 값 복사
 2. 마지막 노드 삭제
 3. 자리 찾아가기
 
'''

# 최대힙
def enq(n):
    global last
    last += 1   # 마지막 노드 추가(완전이진트리 유지), len 연산을 피하기 위해
    h[last] = n # 마지막 노드에 데이터 삽입
    c = last    # 부모>자식 비교를 위해
    p = c//2    # 부모 번호 계산 (자식 인덱스를 알기 떄문에 반대로 부모 인덱스 계산 가능)
    while p >= 1 and h[p] < h[c]:   #루트거나, 부모가 있는데 더 작으면
        h[p], h[c] = h[c], h[p]  # 교환
        c = p
        p = c//2


def deq():
    global last
    tmp = h[1]   # 루트의 키값 보관
    # 자리 탐색 구간
    h[1] = h[last]
    last -= 1
    p = 1           # 새로 옮긴 루트
    c = p*2
    # 왼쪽자식 보다 작다면
    while c <= last:  # 자식이 있으면
        # 자식이 존재하고, 오른쪽 자식이 더 크면
        if c+1 <= last and h[c] < h[c+1]: # 오른쪽자식이 있고 더 크면
            # child + 1
            c += 1
        # 부모가 자손보다 더 작으면 swap
        if h[p] < h[c]:
            h[p], h[c] = h[c], h[p]
            p = c
            c = p*2
        # 더 이상 부모가 작은 경우가 없으면 break
        else:
            break
    return tmp


N = int(input())          # 필요한 노드 수
arr = list(map(int, input().split()))

h = [0]*(N+1)   # 최대힙 => 완전 이진 트리 보장 => 일차원 리스트로 구현 => N 노드 자식: N*2, N*2+1
last = 0        # 힙의 마지막 노드 번호

for num in arr:
    enq(num)

print(h)

while last > 0:
    print(deq(), end=' ')