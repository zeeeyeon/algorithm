# 7 명의 난쟁이 합: 100
# (9 명의 난쟁이의 합  - 100) 의 합에 부합하는 두명의 난쟁이를 찾고 리스트에서 빼주면 됨

def find(height):
    nine_total = sum(height)
    weight = nine_total - 100
    for i in range(N-1):
        for j in range(i+1, N):
            if height[i] + height[j] == weight:
                return height[i], height[j]

N = 9
height = [int(input()) for _ in range(N)]
two = find(height)
height.remove(two[0]), height.remove(two[-1])
print(height)

one, two = find(height)
# 오름차순
for i in sorted(height):
    if i != one and i != two:
        print(i)