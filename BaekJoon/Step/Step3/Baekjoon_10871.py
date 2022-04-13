N,X= map(int,input().split())
result= list(map(int,input().split()))

for i in range(N):
    if result[i] < X:
     print(result[i],end=" ")
