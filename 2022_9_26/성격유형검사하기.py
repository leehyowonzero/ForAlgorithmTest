answerdict = dict()
def check(a, b):
    if(answerdict[a] > answerdict[b]):
        return a
    elif(answerdict[a] < answerdict[b]):
        return b
    else:
        if(a > b):
            return b
        else:
            return a
def solution(survey, choices):
    answer = ''
    for el in ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']:
        answerdict[el] = 0
    for i, el in enumerate(survey):
        if(choices[i] <= 3):
            answerdict[el[0]] += 4 - choices[i]
        elif(choices[i] == 4):
            continue
        else:
            answerdict[el[1]] += choices[i] - 4
    answer += check('R','T')
    answer += check('C','F')
    answer += check('J','M')
    answer += check('A','N')
    return answer