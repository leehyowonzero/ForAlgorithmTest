dx = [0,0,1,-1]
dy = [1,-1,0,0]

def redmove(board, aloc, bloc, turn):
    global answer
    x, y = aloc
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not (0 <= nx < len(board[0]) and 0 <= ny < len(board)):
            continue
        if(board[nx][ny] == 1): #이동가능하면
            board[nx][ny] = 0
            bluemove(board, [nx,ny], bloc, turn + 1)
            board[nx][ny] = 1
    answer = max(answer, turn)
    
def bluemove(board, aloc, bloc, turn):
    global answer
    x, y = bloc
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not (0 <= nx < len(board[0]) and 0 <= ny < len(board)):
            continue
        if(board[nx][ny] == 1): #이동가능하면
            board[nx][ny] = 0
            bluemove(board, aloc, [nx,ny], turn + 1)
            board[nx][ny] = 1
    answer = max(answer, turn)

def solution(board, aloc, bloc):
    answer = -1
    redmove(board, aloc, bloc, 0)
    return answer