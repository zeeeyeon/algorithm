def solution(n):
    result = 0
    while n:
        result += n % 10
        n //= 10
    return result
