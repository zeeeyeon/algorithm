def solution(n):
    word = "수"
    words = "수박"
    
    if n == 1:
        return word
    
    if n % 2 == 0:
        return (n // 2) * words
    else:
        return (n // 2) * words + word
    