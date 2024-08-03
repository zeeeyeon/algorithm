numbers = int(input())

three = [3, 6, 9]

result = []
for number in range(1, numbers + 1):
     count = 0
     split_number = [*map(int, str(number))]
     for i in range(len(three)):
          count += split_number.count(three[i])

     if count == 0: result.append(number)
     else : result.append('-'*count)
print(result)

# 참고
# for n in range(1, int(input()) + 1): print( '-'*(str(n).count('3') + str(n).count('6') + str(n).count('9')) or n, end = ' ')