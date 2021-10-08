string = list(x for x in input())
fm = 0 
to = len(string)
answer = ""
while(1):
	for i in range(fm , to):
		if(fm == i):
			selected = string[i]
			idx = i
		else:
			if(selected > string[i]):
				selected = string[i]
				idx = i
	answer += selected
	fm = idx
	
	print(answer)
