def checkheight(alp):
    if alp.isupper():
        return ord(alp) - ord('A')
    else:
        return ord(alp)-ord('a')+26

def custom_minus(a,b,flag):
    if flag:
        return a - b
    else:
        return b - a

def solve(timeslist,flag):
    global N,M,T
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    total = 0
    visited = [[True] * M for _ in range(N)]
    x = 0
    y = 0
    timeslist[0][0] = 0
    while total <N*M:
        visited[x][y] = False
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx< N and 0 <= ny <M:
                gap = custom_minus(arr[x][y],arr[nx][ny],flag)
                if abs(gap) <= T:
                    if gap < 0:
                        time_temp = abs(gap)**2
                        
                    else:
                        time_temp = 1
                    timeslist[nx][ny] = min(timeslist[nx][ny],timeslist[x][y]+time_temp)
        next_node_x = -1
        next_node_y = -1
        next_times = INF
        for i in range(N):
            for j in range(M):
                if visited[i][j] and next_times > timeslist[i][j]:
                    next_times = timeslist[i][j]
                    next_node_x = i
                    next_node_y = j
        x = next_node_x
        y = next_node_y
        total += 1
        if next_times == INF:
            break

        



N,M,T,D = map(int,input().split())
arr = [list(map(checkheight,list(input()))) for _ in range(N)]
INF =float('inf')

times = [[INF]*M for _ in range(N)]
reversed_times = [[INF]*M for _ in range(N)]
solve(times,True)
solve(reversed_times,False)
max_height = arr[0][0]

for i in range(N):
    for j in range(M):
        if times[i][j] + reversed_times[i][j] <= D and max_height < arr[i][j]:
            max_height = arr[i][j]
print(max_height)