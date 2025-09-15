def solution(price, money, count):
#     (첫 이용금액 + 마지막 이용금액) * (횟수 // 2)
    
#     근데 이 횟수가 짝수면 그냥 계산
#     홀수면 금액^횟수 더하기
    
    # // 3 6 9 12 -> (3 + 12) * (총개수 / 2)
    # // 3 6 9 12 15 -> (3 + 15) * (int(총개수 / 2) + (9가 계산이안됐네?) -> + price * (count // 2 + 1)
    # // 3 6 9 12 15 -> (price + price * count) * (count // 2) + price * (count//2 + 1)
    
                      
#     if count % 2 == 0 :
#         total_price = (price + price*count) * count // 2
#         result = total_price - money
#         if result >= 0 :
#             return result
#         return 0
    
#     total_price = (price + price*count) * count // 2 + price * (count//2 + 1)
    
#     result = total_price - money
    
#     if result >= 0 :
#         return result
#     return 0

#     케이스 나누기
#     짝수 : 3, 6, 9, 12 -> (3 + 12) * (count // 2)
#     홀수 : 3, 6, 9, 12, 15 -> (3 + 15) * (count // 2) + price * (count // 2 + 1)
    
#     그리고 금액 계산하기
#     케이스 나눈 것 > money : 케이스 - money
#     반대일 경우 0
    
    total_price = (price + price * count) * (count // 2)
    
    if count % 2 != 0:
        total_price += price * (count // 2 + 1)
        
    if total_price > money:
        return total_price - money
    else:
        return 0