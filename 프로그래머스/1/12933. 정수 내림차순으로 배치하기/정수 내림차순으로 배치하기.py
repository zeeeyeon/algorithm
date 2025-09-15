def solution(n):
    numbers = str(n)
    sorted_numbers = ''.join(sorted(numbers, reverse=True))
    
    return int(sorted_numbers)