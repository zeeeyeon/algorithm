def solution(a, b):
    total = 0
    
    for i, j in zip(a, b):
        total += i * j
    return total