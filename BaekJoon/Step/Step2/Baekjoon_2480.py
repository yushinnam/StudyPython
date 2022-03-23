a,b,c = map(int,input().split())

if a==b==c : ## 3개가 같은 경우
    print(10000 + a * 1000)
elif a==b or b==c : ## 2개가 같은 경우 1
    print(1000 + b * 100)
elif a==c : ## 2개 같은 경우 2
    print(1000 + a * 100)
else : ## 모두 다른 경우
    print(max(a,b,c) * 100)