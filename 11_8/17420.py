n = int(input())
left = list(map(int,input().split()))
useday = list(map(int,input().split()))
gifticon = [[useday[i], left[i]] for i in range(n)]
answer = 0
for i in range(n):
	share = 0
	if(gifticon[i][0] > gifticon[i][1]):
		share = (gifticon[i][0] - gifticon[i][1] +29)//30
	gifticon[i][1] += 30*share
	answer += share
gifticon.sort(key = lambda x :(x[0], x[1]))
# print(gifticon)
mx = 0 
savemx = 0
for i in range(n):
	# print(answer)
	share = 0
	if(gifticon[i][0] == gifticon[i-1][0] and i != 0):
		if(savemx <= gifticon[i][1]):
			mx = max(mx, gifticon[i][1])
			continue
		else:
			share = (savemx - gifticon[i][1] + 29)//30
			answer += share
			gifticon[i][1] += 30*share
			mx = max(mx, gifticon[i][1])
	else:		
		if(mx <= gifticon[i][1]):
			savemx = mx
			mx = max(mx, gifticon[i][1])
			continue
		else:
			share = (mx - gifticon[i][1] + 29)//30
			answer += share
			gifticon[i][1] += 30*share
			savemx = mx
			mx = max(mx, gifticon[i][1])
print(answer)