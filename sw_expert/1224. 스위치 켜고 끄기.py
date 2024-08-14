import sys
sys.stdin = open('input.txt')

# 3을 받으면 3, 6번의 스위치 반대 => 남학생 (배수로 바꿈)
# 3을 받으면 2, 4번의 스위치 동일한지, 1, 5번 동일한지 체크 동일하다면 12345의 스위치를 반대
# 만약 동일하지 않다면 4번의 스위치만 바꿈

# 스위치 개수 (100개 이하의 양의 정수)
length = int(input())
# 스위치 상태
states = list(map(int, input().split()))
# 학생 수
students = int(input())

def male(states, number):
    for i in range(number-1,length, number):
        if states[i] == 1: states[i] = 0
        else: states[i] = 1
    return states

# 문제 자체를 잘못 이해함, 스위치를 모두 비교하여 다른 부분이 존재하면 중간값만 바꾸는 줄 알았음.....
def female(states, number):
    # count를 왜 1로 설정한지 모르겠음,,,
    count = 1
    flag = True
    while flag:
        if number - count - 1 == -1 or number + count == length+1:
            for i in range(number - count, number + count + 1):
                if states[i] == 1:
                    states[i] = 0
                else:
                    states[i] = 1
            break
        # 슬라이스 해서 0번 인덱스, 마지막 인덱스 같은지 비교
        slice_state = states[number - count - 1:number + count]
        if slice_state[0] == slice_state[-1]:
            count += 1
            continue
        else:
            if states[number - 1] == 1:
                states[number - 1] = 0
            else:
                states[number - 1] = 1
            flag = False
    return states

for _ in range(students):
    # 성별(남:1, 여:2), 받은 수
    gender, number = map(int, input().split())

    # 남자일 경우
    if gender == 1:
        states = male(states, number)
        print('male', states)

    # 여자일 경우
    if gender == 2:
        states = female(states, number)


# 만약 스위치의 수가 20이 넘어가면 다음 줄에 출력
for i in range(length):
    print(states[i], end=" ")
