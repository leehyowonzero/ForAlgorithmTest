from itertools import product
n = int(input())
m = int(input())
wronglist = list(map(int,input().split()))
wrongkey = [False for _ in range(10)]
for el in wronglist:
    wrongkey[el] = True

canusekey = []
for i in range(10):
    if(wrongkey[i] == False):
        canusekey.append(str(i))
strn = str(n)
strlen = len(strn)
answer = abs(100 - n)
dp = [-1 for _ in range(1000001)]
dp[100] = 0
for i in range(1, strlen + 1):
    for perm in product(canusekey, repeat = i):
        number = int(''.join(perm))
        if(dp[number] == -1):
            dp[number] = i
if(dp[n] != -1):
    print(dp[n])
else:
    for i in range(1, 500000):
        candi = []
        if(n-i >= 0):
            if(dp[n-i] != -1):
                candi.append(dp[n-i] + i)
        if(n+i <= 1000000):
            if(dp[n+i] != -1):
                candi.append(dp[n+i] + i)
        if candi:
            print(min(answer, min(candi)))
            break
        