t=int(input())
for i in range(0,t):
    x,n=map(int,input().split())
    y=x//10
    res=y*n
    print(res)
