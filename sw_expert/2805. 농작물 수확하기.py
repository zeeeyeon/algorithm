T = int(input())
for case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    total = 0
    for i in range(N):
       for j in range(N):
           if i > N // 2:
               k = i % (N // 2)

               if N // 2 - k <= j <= N // 2 + k:
                   total += data[i][j]

           else:
               if N // 2 - i <= j <= N // 2 + i:
                   total += data[i][j]

    print(total)

    M = N // 2
    total = 0
    for i in range(N):
        total += sum(data[i][M-(i % M): M+(i % M)+1])
    print(total)
