t = int(input())

for i in range (t):
    h, m = map(int, input().split(" "))

    minutes = h*60 + m

    remaning = 1440 - minutes
    print(remaning)