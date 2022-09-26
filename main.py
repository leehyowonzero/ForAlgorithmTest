n1, n2 = map(int,input().split())
left = list(input())
right = list(input())
t = int(input())
arr = left[::-1] + right
n = n1 + n2
# left 그룹에 있는 애는 다 오른쪽 방향을 가지고있고
# 돌면서 내가 left에 포함되어있는데 내 오른쪽 놈이 right에 포함된 놈이면 swap을 이루어주고 그 포문안에서 다음 인덱스를 보는게 아니라 2칸 뒤 인덱스를 볼 것이다.
for _ in range(t):
    i = 0
    while i < n-1:
        if(arr[i] in left):
            if(arr[i+1] in right):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                i += 2
                continue
        i += 1
print("".join(arr))