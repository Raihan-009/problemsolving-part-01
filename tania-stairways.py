n = int(input())

sequences = list(map(int,input().strip().split()))[:n]
 
steps = []

for count, each in enumerate(sequences):
    if each == 1 and count > 0:
        steps.append(sequences[count - 1])

steps.append(sequences[-1])

print(len(steps))
print(*(each for each in steps))