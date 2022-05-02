n = nbr = int(input())
cnt = 0

while True :
    sum = n // 10 + n % 10 ## 26이면 2+6 = 8
    new_nbr = n % 10 * 10 + sum % 10 ## 새로운수 84
    cnt += 1 ## 사이클 카운트

    n = new_nbr

    if new_nbr == nbr :
        break

print (cnt)