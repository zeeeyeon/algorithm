students = int(input())
waiting = list(map(int, input().split()))

order = []
for i in range(students):
    seat = len(order)
    if seat == 0: order.append(i+1)
    else :order.insert(seat - waiting[i], i+1)

for i in order:
    print(i, end=' ')