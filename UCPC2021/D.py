from collections import deque
n = int(input())

arr = [[] for _ in range(n)]
string = input()
for i in range(n):
    arr[i].append(string[i])
score = list(map(int,input().split()))
for i in range(n):
    arr[i].append(score[i])
q = deque()
for el in arr:
    if(len(q) >= 1):
        if(q[-1][0] == el[0]):
            if(q[-1][1] > el[1]):
                continue
            else:
                q.pop()
                q.append(el)
        else:
            q.append(el)
    else:
        q.append(el)
n = len(q)
if(n == 1 ):
    print("0")
    quit(0)
elif(n == 2):
    print("0")
    quit(0)
q.pop()
q.popleft()
t = (len(q))//2 +(len(q))%2
q = sorted(q,key = lambda x :x[1] ,reverse = True)
ans = 0
for i in range(0,t, 1):
    ans += q[i][1]
print(ans)