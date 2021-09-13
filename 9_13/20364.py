import sys
input = sys.stdin.readline

N, Q = map(int,input().split())
visited = [0 for _ in range(N+1)]

for _ in range(Q):
	want = int(input())
	x = want
	flag = 0
	while want != 1:	
		if visited[want]:
			flag = 1
			first_owned = want
		if want%2:
			want -= 1
		want //= 2
	if flag:
		print(first_owned)
	else:
		visited[x] = True
		print(0)