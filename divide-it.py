q = int(input())

for i in range (q):
    n = int(input())

    let = 0
    moves = 0
    while (n != 1):
        if (n%2 == 0):
            n = n//2
        elif (n%3 == 0):
            n = (2*n)//3
        elif (n%5 == 0):
            n = (4*n)//5
        else:
            let = 1
            break
        moves += 1
    if let == 0:
        print(moves)
    else:
        print(-1)