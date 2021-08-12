def check(number):
	candi = number + 1
	while(True):
		cnt = 0
		x = number ^ candi
		print(number)
		print(candi)
		print(x)
		for i in range(len(bin(x))-2):
			if(x & 1 == 1):
				cnt += 1
			x = x >> 1
		print(cnt)
		if(cnt == 1 or cnt == 2):
			break
		candi += 1
	return candi

def solution(numbers):
    answer = []
    for el in numbers:
        answer.append(check(el))
    return answer

print(solution([2,7]))