a,d,k = map(int,input().split())
ans = 0
up = (d*k/100)/100
tmp1 =d/100
n = 1
res = 1
while True:
    if n == 1:
        ans += n*a*tmp1
        res2 = tmp1
    else:
        res *= (1-res2)
        res2 += up
        if res2 > 1:
            res2 = 1
        ans += n*a*res*(res2)
        up = (res2*k)/100
    n += 1
    if 1-res2 <= 0.000001:
        print(ans)
        break