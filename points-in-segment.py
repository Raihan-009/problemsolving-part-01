n, m = map(int, input().split())

coordinates = []
for each in range (1, m+1):
    coordinates.append(each)

for i in range (n):
    l ,r = map(int, input().split())
    for j in range(l, r+1):
        if j in coordinates:
            coordinates.remove(j)

print(len(coordinates))
for each in coordinates:
    print(each, end=" ")
