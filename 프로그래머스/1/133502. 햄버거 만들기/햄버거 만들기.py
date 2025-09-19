def solution(ingredient):
    # 스택으로 풀기
    # 4개의 재료가 [1, 2, 3, 1]로 쌓였다면 삭제
    
    stack = []
    count = 0
    
    for i in ingredient:
        stack.append(i)
        
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            count += 1
            for j in range(4):
                stack.pop()
            
    return count