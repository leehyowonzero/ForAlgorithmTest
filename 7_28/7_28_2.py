from collections import deque

def transpossible(a, b):
    cnt = 0 
    for i in range(len(a)):
        if(a[i] != b[i]):
            cnt += 1
    if(cnt == 1):
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0
    visited = [0 for _ in range(len(words))]
    q = deque()
    q.append(begin)
    while(q):
        turnlen = len(q)
        for _ in range(turnlen):   
            a = q.popleft()
            if(a == target):
                return answer
            for i in range(len(words)):
                if(visited[i] == 1):
                    continue
                if(transpossible(a, words[i])):
                    q.append(words[i])
                    visited[i] = 1 
        answer += 1
    return 0