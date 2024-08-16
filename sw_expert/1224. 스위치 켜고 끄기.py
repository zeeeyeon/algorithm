length = int(input())
states = list(map(int, input().split()))
students = int(input())

def male(states, number):
    for i in range(number-1,length, number):
        if states[i] == 1: states[i] = 0
        else: states[i] = 1
    return states


def female(states, number):
    number -= 1
    states[number] = 1 - states[number]

    count = 1
    for _ in range(length):
        if number - count < 0 or number + count >= length: break

        if states[number - count] == states[number + count]:
            states[number - count] = 1 - states[number - count]
            states[number + count] = 1 - states[number + count]
            count += 1
        else: break

    return states

for _ in range(students):
    gender, number = map(int, input().split())

    if gender == 1:
        states = male(states, number)

    if gender == 2:
        states = female(states, number)

for i in range(1, length + 1):
    print(states[i - 1], end= " ")
    if i % 20 == 0:
        print()