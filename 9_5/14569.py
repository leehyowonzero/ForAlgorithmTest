def check(studentdictionary):
	cnt = 0
	for case in subject:
		cnt += 1
		for el in case:
			if(el not in studentdictionary):
				cnt -= 1
				break
	return cnt 

n = int(input())
subject = []
for _ in range(n):
	subject.append(list(map(int,input().split()))[1:]) # 첫번째거는 수업시간 수
m = int(input())
for _ in range(m):
	student = list(map(int,input().split()))[1:]
	studentdictionary = dict.fromkeys(student,1)
	print(check(studentdictionary))