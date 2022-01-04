import sys

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
diff = 4000000001

for i in range(n-3):
    for j in range(i+3, n):
        fix = arr[i] + arr[j]
        left, right = i+1, j-1
 
        while left < right:
            s = arr[left] + arr[right]
            if abs(s - fix) < diff:
                diff = abs(s - fix)
            
            if s < fix:
                left += 1
            elif s > fix:
                right -= 1
            else:
                print(0)
                sys.exit(0)
 
print(diff)
