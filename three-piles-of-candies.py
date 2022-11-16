q = int(input())

for i in range(q):
    a,b,c = map(int, input().split())
    sum = a+b+c
    print(sum//2)