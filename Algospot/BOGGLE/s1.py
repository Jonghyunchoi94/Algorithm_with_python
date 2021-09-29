import sys
sys.stdin = open('input.txt')

C = int(input())

dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,-1,-1,1]

def hasWord(x, y, word):
    global cnt
    if len(word) == 0:
        cnt += 1
        return

    for k in range(8):
        next_x = x + dx[k]
        next_y = y + dy[k]
        if 0 <= next_x < 5 and 0 <= next_y < 5 and data[next_x][next_y] == word[0]:
            hasWord(next_x, next_y, word[1:])
    return



for case in range(C):
    data = [list(input()) for _ in range(5)]
    N = int(input())
    for _ in range(N):
        cnt = 0
        word = input()
        for i in range(5):
            for j in range(5):
                if data[i][j] == word[0]:
                    hasWord(i, j, word[1:])
        if cnt:
            print('{} {}'.format(word, True))
        else:
            print('{} {}'.format(word, False))
