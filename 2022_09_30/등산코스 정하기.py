import heapq
import sys


def solution(n, paths, gates, summits):
    # 인접 리스트
    answer = [50001, sys.maxsize]
    node = [[] for _ in range(n + 1)]
    for path in paths:
        fm, to, cost = path
        node[fm].append([to, cost])
        node[to].append([fm, cost])

    # set 자료구조 활용
    gate_set = set(gates)
    summit_set = set(summits)
    minsummit = min(summits)
    # 작업을 수행 할 큐
    q = []
    # 출입구 모두 넣기
    for gate in gates:
        heapq.heappush(q, [0, gate])  # [비용, 현재 지점]
    visited = set()
    flag = False
    while q:
        cost, nownode = heapq.heappop(q)
        if (flag == True and cost > answer[1]):
            break
        visited.add(nownode)
        if (nownode in summit_set):
            flag = True
            if (nownode == minsummit):
                return [nownode, cost]
            if (cost <= answer[1]):
                answer = [min(nownode, answer[0]), cost]
            continue
        for nextnodedata in node[nownode]:
            nextnode, nextcost = nextnodedata
            if (nextnode in visited):
                continue
            if (nextnode in gate_set):
                continue
            heapq.heappush(q, [max(nextcost, cost), nextnode])
    return answer
