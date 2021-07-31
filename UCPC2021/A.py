def check(start):
	i = 0
	while(True):
		if(i >=len(s)):
			break
		if(s[i:i+len(start)] != start):
			# print(s[i:i+len(start)], start )
			return -1
		i += len(start)
		start = str(int(start) + 1)
	# print(start)
	return int(start) - 1

s= input()
realstart = None
for i in range(1,4):
	start = s[0:i]
	second = int(start) +1
	realsecond = s[i:i+len(str(second))]
	if(str(second) == realsecond):
		realstart = start
		ans = check(realstart)
		if ans != -1:
			print(start, ans)
			break

if(realstart == None):
	print(s, s)