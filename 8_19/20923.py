from collections import deque
n, m = map(int,input().split())
do = deque()
su = deque()
turn = 0  
for _ in range(n):
	fordo, forsu = map(int,input().split())
	do.appendleft(fordo)
	su.appendleft(forsu)
doground = deque()
suground = deque()


for i in range(m):
	if(i%2 == 0): # 도도턴
		doground.append(do.popleft())
		if(len(do) == 0):
			print("su")
			exit()
		if(doground[-1] == 5 and len(suground) == 0):
			do.extend(doground)
			doground = deque()
			continue
		if(len(suground) != 0):
			if(doground[-1] + suground[-1] == 5):
				# print("수연이 윈")
				su.extend(doground)
				su.extend(suground)
				doground = deque()
				suground = deque()
				continue
			elif(doground[-1] == 5 or suground[-1] == 5):
				# print("도도 윈")
				do.extend(suground)
				do.extend(doground)
				doground = deque()
				suground = deque()
				continue
	else:
		suground.append(su.popleft())
		if(len(su) == 0):
			print("do")
			exit()
		if(suground[-1] == 5 and len(doground) == 0):
			do.extend(suground)
			suground = deque()
			continue
		if(len(doground) != 0):
			if(doground[-1] + suground[-1] == 5):
				# print("수연이 윈")
				su.extend(doground)
				su.extend(suground)
				doground = deque()
				suground = deque()
				continue
			elif(doground[-1] == 5 or suground[-1] == 5):
				# print("도도 윈")
				do.extend(suground)
				do.extend(doground)
				doground = deque()
				suground = deque()
				continue
	
if(len(do) == len(su)):
	print("dosu")
elif(len(do)> len(su)):
	print("do")
else:
	print("su")