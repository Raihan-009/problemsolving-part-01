from operator import mod


n = int(input())
  
members = list(map(int,input().strip().split()))[:n]
members.sort()

min_probs = []
for count, each in enumerate(members):
    if (count %2 == 0):
        min_probs.append(abs(members[count] - members[count+1]))

print(sum(min_probs))
