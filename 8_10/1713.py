n = int(input())
m = int(input())
arr = list(map(int,input().split()))
have = dict()

for i, el in enumerate(arr):
	if(len(have) >= n):
		if(el not in have):
			del have[min(have, key = lambda x : have[x])]
			have[el] = [1,i]
		else:
			have[el][0] += 1
	else:
		if(el in have):
			have[el][0] += 1
		
		else:
			have[el] = [1, i]

print(*sorted(have))