t = int(input())

for i in range (t):
    n = int(input())
    elements = list(map(int, input().split()))[:n]

    summ = sum(elements)
    odd = 0
    even = 0
    if (summ %2 != 0):
        print("YES")
    else:
        for e in elements:
            if (e%2 == 0):
                even+=1
            else:
                odd +=1
        if (odd >= 1 and even>=1):
            print("YES")
        else:
            print("NO")