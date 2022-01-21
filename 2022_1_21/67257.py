import re
import copy
from itertools import permutations
from collections import deque
def solution(expression):
    answer = 0
    permutationcase = list(permutations(['-','+','*']))
    SplitedExpression = re.split(r'(\D)',expression)
    
    for case in permutationcase:
        leastExpression = deque(SplitedExpression)
        for operator in case:
            q = deque()
            while leastExpression:
                if(leastExpression[0] == operator):
                    q.append(str(eval(q.pop() + leastExpression.popleft() + leastExpression.popleft())))
                else:
                    q.append(leastExpression.popleft())
            leastExpression = q.copy()
        answer = max(answer, abs(int(q[0])))
    return answer