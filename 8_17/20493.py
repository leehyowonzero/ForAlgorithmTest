dx = [-1,0,1,0]
dy = [0,1,0,-1]
n, t = map(int,input().split())
command = []
for _ in range(n):
	command.append(list(input().split()))
start = 0
x = 0
y = 0
d = 2
for el in command:
	distance = int(el[0]) - start
	x = x + dx[d]*distance
	y = y + dy[d]*distance
	start = int(el[0])
	if(el[1] == "left"):
		d = (d-1)%4
	else:
		d = (d+1)%4
distance = t - start
x = x + dx[d]*distance
y = y + dy[d]*distance
print(x,y)