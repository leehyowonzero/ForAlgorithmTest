from collections import deque

N, K = map(int,input().split())
LEN = len(N) #전체 자릿수
answer = -1

visited =[[False for i in range(11)] for i in range(1000001)]

q = deque()
q.append((N,0))
visited[N][0]=True

def swap(N, idx1, idx2):
	N = list(str(N))
    N[idx1], N[idx2] = N[idx2], N[idx1]

	return int(''.join(N))

while q:
    n, depth = q.popleft()

    if depth == K: #깊이가 K면 비교해서 최대값
        answer = max(answer, n)
        continue
       
    for i in range(LEN): 
        for j in range(i+1,LEN):
            if i ==0 and n[j] =='0': 
                continue

            next_n = swap(n, i, j) #자리를 바꾸고
            if not visited[next_n][depth+1]: #해당 값과 깊이를 방문하지 않았으면
                visited[next_n][depth+1] = True #방문하고
                q.append([next_n, depth+1]) # q에 집어넣어준다.

print(answer)