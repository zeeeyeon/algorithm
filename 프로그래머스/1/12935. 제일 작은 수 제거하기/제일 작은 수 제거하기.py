def solution(arr):
    if len(arr) == 1:
        return [-1]
    
    reverse_arr = sorted(arr, reverse = True)
    min = reverse_arr[-1]
    factors_arr = []
    
    for i in arr:
        if i != min:factors_arr.append(i)
    
    return factors_arr
            