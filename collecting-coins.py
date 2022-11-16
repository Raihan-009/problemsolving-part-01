t = int(input())

for i in range (t):
    coins = list(map(int, input().split()))[:4]
    max_coin = max(coins[:3])
    total = sum(coins)
    possibility = total%3
    check = total//3
    if (possibility == 0 and check >= max_coin):
        print("YES")
    else:
        print("NO")