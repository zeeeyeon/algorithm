def solution(arr, divisor):
    factors = []
    
    for i in arr:
        if i % divisor == 0:
            factors.append(i)
    
    if not factors:
        return [-1]
    else:
        return sorted(factors)