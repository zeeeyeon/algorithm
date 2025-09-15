def solution(n):
    word100 = "수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박수박"
    word10 = "수박수박수박수박수박"
    word4 = "수박수박"
    word2 = "수박"
    odd_word = "수"
    result = ""
    
    if n > 100 :
        temp = n // 100
        n = n % 100
        result = result + (word100 * temp)
    if n > 10 :
        temp = n // 10
        n = n % 10
        result = result + (word10 * temp)
        
    if n > 4 :
        temp = n // 4
        n = n % 4
        result = result + (word4 * temp)
        
    if n >= 2 :
        temp = n // 2
        n = n % 2
        result = result + (word2 * temp)
        
    if n == 1 :
        result = result + odd_word
        
    return result
    