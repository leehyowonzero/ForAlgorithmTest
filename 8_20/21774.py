import bisect
import sys
input = sys.stdin.readline

n, q = map(int,input().split())
arr = [[]for _ in range(7)]
for _ in range(n):
	line = input()
	front, back = line.split()
	front = "".join(front.split('-'))
	back, lv = back.split('#')
	back = "".join(back.split(':'))
	day = int(front + back)
	arr[int(lv)].append(day)
for _ in range(q):
	line = input()
	front, middle, back = line.split('#')
	x, y = front.split()
	x = "".join(x.split('-'))
	y = "".join(y.split(':'))
	startday = int(x + y)
	x, y = middle.split()
	x = "".join(x.split('-'))
	y = "".join(y.split(':'))
	endday = int(x + y)
	lv = int(back)
	ans = 0
	for i in range(lv, 7):
		ans += bisect.bisect_right(arr[i], endday) - bisect.bisect_left(arr[i], startday)
	print(ans)
