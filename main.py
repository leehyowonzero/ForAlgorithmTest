s = list(input())
q = []
ans = ""

for el in s:
	if(el.isalpha()):
		ans += el
	else:
		if el == '(': q.append(el)
		
		elif el == '*' or el == '/': 
			while q and (q[-1] == '*' or q[-1] =='/'): 
				ans += q.pop() 	
			q.append(el)
		elif el == '+' or el == '-': 
			while q and q[-1] != '(': 
				ans+= q.pop() 
			q.append(el)
		elif el == ')': 
			while q and q[-1] != '(': 
				ans += q.pop() 
			q.pop()

while q : 
	ans+=q.pop() 

print(ans)
