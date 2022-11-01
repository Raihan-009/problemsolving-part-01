four= list(map(int,input().strip().split()))[:4]
four.sort()
four.pop(-1)

m,n,p = four

a = int((m+n-p)/2)
b = int((m-n+p)/2)
c = int((n-m+p)/2)

print(a,b, c)