def solution(n, stations, w):
    answer=0
    i = 0
    locate = 1
    while locate <=n:
        if i < len(stations) and locate >= stations[i]-w:
            locate = stations[i] + w + 1
            i += 1
        else:
            locate += 2 * w + 1
            answer += 1
    return answer