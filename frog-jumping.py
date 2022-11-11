queries = int(input())

for each in range (queries):

    a,b,k = map(int, input().split())

    if (k %2 == 0):
        print((a-b)*(k//2))
        
    else:
        print((a*((k+1)//2)) - (b*((k-1)//2)))
