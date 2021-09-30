import sys
sys.stdin = open('input.txt')

C = int(input())

dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,-1,-1,1]

def hasWord(y, x, word):
    # 기저사례 선택
    # 0. 입력이 잘못되거나 범위에서 벗어난 경우 실패 처리
    if (not(0 <= y < 5)) or (not(0 <= x < 5)):
        return False
    # 1. 위치 (y,x)에 있는 글자가 원하는 단어의 첫 글자가 아닌 경우 항상 실패
    if data[y][x] != word[0]:
        return False
    # 2. (1번 경우에 해당되지 않을 경우) 원하는 단어가 한 글자인 경우 항상 성공
    if len(word) == 1:
        return True

    for k in range(8):
        next_y = y + dy[k]
        next_x = x + dx[k]
        if hasWord(next_y, next_x, word[1:]):
            return True
    return False

def hasallWord(word):
    for i in range(5):
        for j in range(5):
            if data[i][j] == word[0]:
                ans = hasWord(i, j, word)
                if ans:
                    return 'YES'
    return 'NO'


for case in range(C):
    data = [list(input()) for _ in range(5)]
    N = int(input())
    for _ in range(N):
        word = input()
        print('{} {}'.format(word, hasallWord(word)))
