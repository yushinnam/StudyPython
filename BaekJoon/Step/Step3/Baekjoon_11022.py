n=int(input())

for i in range(n) :
    a,b= map(int,input().split())
    answer = a+b
    print('Case #%s: %s + %s = %s' %(i+1,a,b,answer))