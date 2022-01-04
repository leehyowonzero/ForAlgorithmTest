import sys
from collections import deque

def CheckBombs():   
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                bombs.append((i, j))


def FillBombs():   # 빈자리에 폭탄 설치
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] = 'O'


def explode():      # bombs deque에 들어있는 폭탄 터트림
    while bombs:
        r, c = bombs.popleft()
        board[r][c] = '.'
        if 0 <= r - 1:
            board[r - 1][c] = '.'
        if r + 1 < R:
            board[r + 1][c] = '.'
        if 0 <= c - 1:
            board[r][c - 1] = '.'
        if c + 1 < C:
            board[r][c + 1] = '.'


R, C, N = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

N -= 1  
while N:
    bombs = deque()
    CheckBombs()
    FillBombs()
    N -= 1
    if N == 0:
        break
    explode()
    N -= 1

for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j], end='')
    print()