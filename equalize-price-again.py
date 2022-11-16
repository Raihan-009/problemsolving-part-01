q = int(input())

for i in range (q):
    n = int(input())
    prices = list(map(int, input().split()))[:n]
    total = sum(prices)
    print((total//n) + (total%n>0))