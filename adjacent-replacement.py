n = int(input())
  
values = list(map(int,input().strip().split()))[:n]
# print(values)

for count, each in enumerate(values):
    if values[count] %2 == 0:
        values[count] = values[count]-1

print(*(each for each in values))