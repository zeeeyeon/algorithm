# def solution(x, n):
#     array = []
#     for i in range(n):
#         array.append(x * (i+1))
        
#     return array


def solution(x, n):
    array = [x]
    for i in range(1, n):
        array.append(array[i-1] + x)
        
    return array