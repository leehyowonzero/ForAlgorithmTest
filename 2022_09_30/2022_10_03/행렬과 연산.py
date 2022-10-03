from collections import deque


def show(arr, n, m):
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=' ')
        print()


def solution(rc, operations):
    n = len(rc)
    m = len(rc[0])
    answer = [[] for _ in range(n)]
    dequerc = [deque() for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dequerc[i].append(rc[i][j])
    rcByindex = deque(i for i in range(0, n))
    # print(rcByindex)
    zero_row = 0
    n_row = n - 1
    for operation in operations:
        if (operation == "ShiftRow"):  # 행 밀기
            rcByindex.appendleft(rcByindex.pop())
            zero_row -= 1
            zero_row = (zero_row) % n
            n_row -= 1
            n_row = (n_row) % n
        else:  # 돌리기
            # 0번 행 오른쪽 값 pop
            zero_row_right = dequerc[zero_row].pop()
            n_row_left = dequerc[n_row].popleft()
            for i in range(n_row - 1, n_row - n + 1, -1):
                dequerc[(i + 1) % n].append(dequerc[i].pop())
            dequerc[(zero_row + 1) % n].append(zero_row_right)
            for i in range((zero_row + 1), zero_row + n - 1):
                i = (i + n) % n
                dequerc[i - 1].appendleft(dequerc[i].popleft())
            dequerc[(n_row - 1) % n].appendleft(n_row_left)
    # show(dequerc, n, m)
    for i in range(n):
        for j in range(m):
            answer[i].append(dequerc[rcByindex[i]].popleft())
    return answer
