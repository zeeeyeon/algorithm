N = 9
height = [int(input()) for _ in range(N)]
two_person = sum(height) - 100

def find_person(height, weight):
    for i in range(N-1):
        for j in range(i+1, N):
            if height[i] + height[j] == weight:
                return height[i], height[j]

one, two = find_person(height, two_person)
for i in sorted(height):
    if i != one and i != two:
        print(i)