import bisect

def solution(citations):
    answer = 0
    citations.sort()
    for i in range(citations[-1], -1,-1):
        if(i >= bisect.bisect_left(citations, i) and len(citations) - bisect.bisect_left(citations, i) + 1 > i):
            answer = i
            break
            

    return answer