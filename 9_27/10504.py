t = int(input())
for _ in range(t):
	n = int(input())
	if(n == 1 or n == 2):
		print("IMPOSSIBLE")
		break
	flag = True
	for m in range(2, n):
		now = n
		now -= (m*(m+1))//2
		if(now < 0):
			break
		if(now % m == 0):
			flag = False
			print(n, end="")
			print(" = ",end="")
			
			for j in range(1, m+1):
				print(j + now//m, end ="")
				if(j == m):
					continue
				print(" + ", end= "")
			print()
			break
	if(flag == True):
		print("IMPOSSIBLE")
			

