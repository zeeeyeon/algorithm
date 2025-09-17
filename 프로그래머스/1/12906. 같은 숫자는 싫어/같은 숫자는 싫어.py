def solution(arr):
    
    # 새로운 배열에 넣기
    # 다음에 넣을 수와 배열 pop 의 숫자가 같다면 안넣고 넘어가기
    array = []
    array.append(arr[0])
    
    for i in range(1, len(arr)):
        if arr[i] == array[-1]:continue
        array.append(arr[i])
    
    return array
            
        