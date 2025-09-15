def solution(left, right):
    # 제곱근이 자연수인지 확인
    # 1 ~ 제곱근까지 돌려서 나머지 0인지 확인
    # 전체 카운트 + 1

    total = 0
    
    for factor in range(left, right + 1):
        count = 0
        for i in range(1, int(factor**0.5) + 1):
            if factor % i == 0:
                count += 2
            if i * i == factor:
                count -= 1
        
        if count % 2 == 0:
            total += factor
        else:
            total -= factor
    
    return total
            
    
                
            