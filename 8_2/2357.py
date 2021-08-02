from math import *
import sys
input = sys.stdin.readline

def Mininit(node, start, end):
	if start == end:
		min_tree[node] = arr[start]
		return min_tree[node]
	else:
		mid = (start + end) // 2
		min_tree[node] = min(Mininit(node*2, start, mid), Mininit(node*2+1, mid+1, end))
		return min_tree[node]

def Maxinit(node, start, end):
	if start == end:
		max_tree[node] = arr[start]
		return max_tree[node]
	else:
		mid = (start + end) // 2
		max_tree[node] = max(Maxinit(node*2, start, mid), Maxinit(node*2+1, mid+1, end))
		return max_tree[node]

def Minquery(node, start, end, left, right):
	if( start > right or end < left):
		return 1000000001
	if(left <= start and right >= end):
		return min_tree[node]
	
	mid = (start + end) // 2
	return min(Minquery(node*2, start, mid, left, right),Minquery(node*2+1, mid+1, end, left, right))

def Maxquery(node, start, end, left, right):
	if( start > right or end < left):
		return 0
	if(left <= start and right >= end):
		return max_tree[node]
	
	mid = (start + end) // 2
	return max(Maxquery(node*2, start, mid, left, right),Maxquery(node*2+1, mid+1, end, left, right))
# 입력 및 배열 생성
n, m = map(int,input().split())
arr = []
for i in range(0,n):
	arr.append(int(input()))
# 구각 최소 최대 값을 가지는 트리 생성
h= int(ceil(log2(n)))
min_tree = [0 for _ in range(1 << (h+1))]
max_tree = [0 for _ in range(1 << (h+1))]
Mininit(1,0,n-1)
Maxinit(1,0,n-1)
for i in range(m):
	a, b = map(int,input().split())
	print(Minquery(1,0,n-1,a-1,b-1), Maxquery(1,0,n-1,a-1,b-1))
	
