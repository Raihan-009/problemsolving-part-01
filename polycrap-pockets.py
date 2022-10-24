n = int(input())
  
coins = list(map(int,input().strip().split()))[:n]
  
duplicateFrequencies = {}
for i in set(coins):
    duplicateFrequencies[i] = coins.count(i)

print(max(duplicateFrequencies.values()))