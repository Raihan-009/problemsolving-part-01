def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

n = int(input())

sum = getSum(n)

while (sum %4 != 0):
    n+=1
    sum = getSum(n)
print(n)

