t = int(input())

for i in range (t):
    n = int(input())
    students = list(map(int, input().split()))[:n]
    students.sort()
    check = 0

    for i in range (n-1):
        if students[i+1] - students[i] <= 1:
            check = 1
            break
    if check == 1:
        print(2)
    else:
        print(1)
