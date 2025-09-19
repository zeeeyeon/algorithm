def solution(park, routes):
    dxy = {"S": [1, 0], "N": [-1, 0], "E": [0, 1], "W": [0, -1]}
    x, y = 0, 0
    
    w = len(park[0])
    h = len(park)
    
    # 스타트 지점 찾기
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":  
                x, y = i, j
                break
                
    for route in routes:
        dx, dy = dxy[route.split()[0]]
        n = int(route.split()[1])
        ix, iy = x, y
        
        for _ in range(n):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                x, y = ix, iy
                break 
            if park[nx][ny] == "X":
                x, y = ix, iy
                break
            x, y = nx, ny
            
    return [x, y]
    
#     for route in routes:
#         direction, distance = route.split()
#         distance = int(distance)
        
#         if direction == "E":
#             dx, dy = dxy[0]
#         elif direction == "W":
#             dx, dy = dxy[1]
#         elif direction == "S":
#             dx, dy = dxy[2]
#         elif direction == "N":
#             dx, dy = dxy[3]
            
#         for _ in range(distance):
#             if 0 <= x + dx < h and 0 <= y + dy < w and park[x + dx][y + dy] != "X":
#                 x += dx
#                 y += dy
#             else:
#                 break
        
#     return [x, y]