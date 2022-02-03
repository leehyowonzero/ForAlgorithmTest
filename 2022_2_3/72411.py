from itertools import combinations

def solution(orders, course):
    answer = []
    for idx in course: # 각 course 케이스 별로 조합짜기
        candi = dict()
        for order in orders:
            order = list(''.join(order))
            order.sort()
            for ret in list(map(''.join,combinations(order,idx))):
                if(ret not in candi):
                    candi[ret] = 1
                else:
                    candi[ret] += 1
        candi = sorted(candi.items(), key = lambda x : x[1], reverse = True)
        if(len(candi) > 0): # 가장 많은 빈도의 셋트 메뉴들 뽑기
            mx = candi[0][1]
            if(mx  == 1):
                continue
            for el in candi:
                if(el[1] == mx ):
                    answer.append(el[0])
    answer.sort()
    return answer