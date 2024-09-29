N = int(input())
M = int(input())
students = list(map(int, input().split()))

rank = []
student_likes = [0] * 101  # 학생들의 추천 횟수를 저장할 리스트
student_order = {}  # 학생들이 처음 추천된 순서를 저장할 딕셔너리
order = 0  # 추천 순서

for student in students:
    order += 1
    if student in [x[0] for x in rank]:
        # 랭킹에 존재
        for j in range(len(rank)):
            if rank[j][0] == student:
                # 추천수 1 추가
                rank[j][1] += 1
                break
    else:
        # 정해진 사진틀 개수보다 적으면 추가
        if len(rank) < N:
            rank.append([student, 1, order])
            student_order[student] = order
        else:
            # 랭킹에 존재하는 학생 중 추천이 가장 적은 학생 삭제
            rank.sort(key=lambda x: (x[1], x[2]))
            oldest_student = rank[0][0]
            rank.pop(0)
            rank.append([student, 1, order])
            student_order[student] = order

# 최종 후보 리스트를 학생 번호 순으로 정렬하여 출력
rank.sort(key=lambda x: x[0])
print(' '.join(str(x[0]) for x in rank))