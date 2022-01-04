from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(r1, c1):
    dq = deque()
    dq.append((r1, c1))
    cow_visited[r1][c1] = True
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            # 범위 체크
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if cow_visited[nx][ny]:  # 방문 체크
                continue
            if (nx, ny) in bridge[x][y]:  # 다리인 경우 pass
                continue
            dq.append((nx, ny))
            cow_visited[nx][ny] = True

n, k, r = map(int, input().split()) 

bridge = [[[] for _ in range(n)] for _ in range(n)]
cow_visited = [[False] * n for _ in range(n)]
count = 0
# 길
for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    bridge[r1 - 1][c1 - 1].append((r2 - 1, c2 - 1))
    bridge[r2 - 1][c2 - 1].append((r1 - 1, c1 - 1))

# 소
cow_list = []
for _ in range(k):
    a, b = map(int, input().split())
    cow_list.append((a - 1, b - 1))

# 1. 소를 한마리씩 돌려가면서 방문 여부 탐색
for i, cow in enumerate(cow_list):
    cow_visited = [[False] * n for _ in range(n)]
    # 2. 현재 소가 정해진 길 없이 가는 경로를 탐색
    bfs(cow[0], cow[1])
    for r2, c2 in cow_list[i + 1:]:
        # 3. 방문을 완료하지 못한 경우 결과 + 1
        if not cow_visited[r2][c2]:
            count += 1
print(count)