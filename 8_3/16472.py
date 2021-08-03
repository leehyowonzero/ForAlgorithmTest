from collections import deque
n = int(input())
s = input()
alpha = dict()
q = deque()
havealpha = 0
ans = 0 
for el in s:
	if el in alpha:

		alpha[el] += 1
		q.append(el)
	else:
		if(havealpha == n):
			alpha[el] = 1
			havealpha += 1
			q.append(el)
			while(havealpha > n):
				abandonalpha = q.popleft()
				alpha[abandonalpha] -= 1
				if(alpha[abandonalpha] == 0 ):
					havealpha -= 1
					del alpha[abandonalpha]	
		else:
			alpha[el] = 1
			havealpha += 1
			q.append(el)
	# print(q)
	# print(havealpha)
	# print(alpha)
	ans = max(ans, len(q))
print(ans)