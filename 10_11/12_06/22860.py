def check(target):
	global have
	if(target not in filesystem):
		return 
	for el in filesystem[target]:
		if(el[1] == '1'):
			check(el[0])
		else:
			have.append(el[0])
		

n, m = map(int,input().split())
filesystem = dict()
for _ in range(n+m):
	p, f, c = input().split()
	if(p not in filesystem):
		filesystem[p] = []
		filesystem[p].append((f,c))
	else:
		filesystem[p].append((f,c))
q = int(input())
for _ in range(q):
	global have
	have = []
	query = input()
	target = query.split('/')[-1]
	check(target)
	print(len(set(have)), len(have))
