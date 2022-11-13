q = int(input())

for each in range (q):
    a, b = map(int, input().split())
    if (a == b):
        print(0)
    else:
        if (a%2 == 0 and b%2 == 0 and a<b):
            print(2)
        if (a%2 == 0 and b%2 == 0 and a>b):
            print(1)
        if (a%2 == 1 and b%2 == 1 and a<b):
            print(2)
        if (a%2 == 1 and b%2 == 1 and a>b):
            print(1)
        if (a%2 == 0 and b%2 == 1 and a<b):
            print(1)
        if (a%2 == 0 and b%2 == 1 and a>b):
            print(2)
        if (a%2 == 1 and b%2 == 0 and a<b):
            print(1)
        if (a%2 == 1 and b%2 == 0 and a>b):
            print(2)