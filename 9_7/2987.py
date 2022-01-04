x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())
x3, y3 = map(int,input().split())
d = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2
cnt = 0
n = int(input())
for _ in range(n):
	ans = 0
	nx, ny = map(int,input().split())
	ans += abs(nx*(y2-y3) + x2*(y3-ny) + x3*(ny-y2))/2
	ans += abs(x1*(ny-y3) + nx*(y3-y1) + x3*(y1-ny))/2
	ans += abs(x1*(y2-ny) + x2*(ny-y1) + nx*(y1-y2))/2
	if(ans == d):
		cnt += 1
print(d)
print(cnt)	
