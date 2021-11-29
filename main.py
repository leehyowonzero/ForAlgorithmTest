n = int(input())
stack = []
ans = 0
for i in range(n):
	# print(stack)
	# print(ans)
	nowinput = [0,1]
	nowinput[0] = int(input())
	while stack:
		if(stack[-1][0] < nowinput[0]):
			stack.pop()
			ans += 1
		elif(stack[-1][0] == nowinput[0]):
			ans += stack[-1][1]
			nowinput[1] += stack[-1][1]
			break
		else:
			nowinput[1] += 1
			ans += 1
			break
	stack.append(nowinput)
	# print(stack)
	# print("답",ans)
print(ans)