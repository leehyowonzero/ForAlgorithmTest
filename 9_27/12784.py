import sys
import math
from queue import PriorityQueue
input = sys.stdin.readline
inf=math.inf

def dfs(x,y):
    global uy,ry
    uy[x]=1
    if st[x]==1 and x!=1:return inf
    k=0
    for next in graph[x]:
        if next[0]!=y:
            if uy[next[0]]==0:
                zv=dfs(next[0],x)
                k+=min(zv,next[1])
    ry[x]=k
    return k


t=int(input())
for _ in range(t):
    a, b=map(int,input().split())
    st=[0]*(a+1)
    uy=[0]*(a+1)
    ry=[-inf]*(a+1)
    graph=[[]for i in range(a+1)]
    for i in range(b):
        y = list(map(int,input().split()))
        st[y[0]]+=1
        st[y[1]]+=1
        graph[y[0]].append([y[1],y[2]])
        graph[y[1]].append([y[0],y[2]])
    print(dfs(1,1))