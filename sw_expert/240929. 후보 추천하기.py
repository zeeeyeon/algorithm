N = int(input())
M = int(input())
students = list(map(int, input().split()))

# 3
# 9
# 2 1 4 3 5 6 2 7 2
rank = []


#  왜 안되는지 모루겠,,
for student in students:
    # 랭킹에 존재하는지 확인
    if student not in [x[0] for x in rank]:
        # 정해진 사진틀 개수보다 적으면 추가
        if len(rank) < M:
            rank.append([student, 1])
        else:
            # 랭킹에 존재하는 학생 중 추천이 가장 적은 학생 삭제
            min_student = min(rank, key=lambda x: x[1])
            rank.remove(min_student)
            rank.append([student, 1])
    else:
        # 랭킹에 존재
        for j in range(len(rank)):
            if rank[j][0] == student:
                # 추천수 1 추가
                rank[j][1] += 1
                break
