def solution(queue1, queue2):
    answer = 0
    queue = []
    sum_all = 0
    sum_part = 0
    for el in queue1:
        queue.append(el)
        sum_all += el
        sum_part += el
    for el in queue2:
        queue.append(el)
        sum_all += el
    if (sum_all % 2 == 1):
        return -1  # 홀수 예외처리
    half_all = sum_all / 2
    left = 0
    right = len(queue1) - 1
    while (left <= right and right < len(queue) - 1):
        if (sum_part == half_all):
            return answer
            break
        if (sum_part < half_all):
            right += 1
            sum_part += queue[right]
        else:
            sum_part -= queue[left]
            left += 1
        answer += 1
    return -1
