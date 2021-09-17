from itertools import permutations
import copy

n = int(input())
line = []
for _ in range(n):
	fm, to = map(int,input().split())
	line.append((fm, to))
	

