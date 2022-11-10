n = int(input())
abcd = input()[:n]

sum = 0

for i in range(1, n+1):
    sum = sum + i
    if sum <= len(abcd):
        print(abcd[sum-1], end="")
    