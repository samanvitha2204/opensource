n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
    print(l[n-i-1],end=" ")
