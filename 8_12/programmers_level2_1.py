def dfs(cnt, arr, ans, target):
    global answer
    global n
    if(cnt == n and target == ans):
        answer += 1
        return
    nowarr = arr[:]
    for i, el in enumerate(arr):
        for operator in [-1,1]:
            ans += el*operator
            del arr[i]
            dfs(cnt+1,arr,ans, target)
            arr = nowarr[:]
            ans -= el*operator
    return

def solution(numbers, target):
    global answer
    global n
    n = len(numbers)
    answer = 0
    dfs(0, numbers, 0, target)
    
    return answer