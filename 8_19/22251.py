n, k, p, x = map(int,input().split())
ans = 0
convert = [
	[0,4,3,3,4,3,2,3,1,2],
	[4,0,5,3,2,5,6,1,5,4],
	[3,5,0,2,5,4,3,4,2,3],
	[3,3,2,0,3,2,3,2,2,1],
	[4,2,5,3,0,3,4,3,3,2],
	[3,5,4,2,3,0,1,4,2,1],
	[2,6,3,3,4,1,0,5,1,2],
	[3,1,4,2,3,4,5,0,4,3],
	[1,5,2,2,3,2,1,4,0,1],
	[2,4,3,1,2,1,2,3,1,0]
]
strx = str(x)
while(len(strx)< k):
	strx = "0" + strx

for num in range(1,n+1):
	target = str(num)
	while(len(target)< k):
		target = "0" + target
	need = 0
	for i in range(0,k):
		need += convert[int(strx[i])][int(target[i])]
	if(1 <= need <= p):
		# print(target)
		ans += 1
print(ans)