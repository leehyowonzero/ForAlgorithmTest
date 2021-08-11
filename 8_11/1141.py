def check(i, prefix):
	for j in range(i+1,len(arr)):
		if(prefix == arr[j][0:len(prefix)]):
			return False
	return True

n = int(input())
arr = []
for _ in range(n):
	arr.append(input())
arr.sort(key = lambda x: len(x))
ans = 0
for i, candi in enumerate(arr):
	if(check(i, candi)):
		ans +=1
print(ans)