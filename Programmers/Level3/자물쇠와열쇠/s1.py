key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def rotate_90(key):
    answer = [[0] * len(key) for _ in range(len(key))]

    for i in range(len(key)):
        for j in range(len(key)):
            answer[i][j] = key[len(key) - j - 1][i]
    return answer

def rotate_180(key):
    temp = rotate_90(key)
    answer = rotate_90(temp)
    return answer

def rotate_270(key):
    temp1 = rotate_90(key)
    temp2 = rotate_90(temp1)
    answer = rotate_90(temp2)
    return answer


def compareroad(lock, keys, cnt):
    for key in keys:
        temp = 0
        Flag = False
        for i in range(len(key)):
            for j in range(len(key)):
                if lock[i][j] == 2:
                    continue
                if lock[i][j] == key[i][j]:
                    Flag = True
                    break

                if lock[i][j] == 0 and key[i][j] == 1:
                    temp += 1

            if Flag:
                break

        if temp == cnt:
            return True

    return False

def solution(key, lock):
    M = len(key)
    N = len(lock)
    B = (2 * M) + N - 2

    board = [[2] * B for _ in range(B)]

    cnt = 0

    for i in range(M - 1, M + N - 1):
        for j in range(M - 1, M + N - 1):
            board[i][j] = lock[i - M + 1][j - M + 1]
            if lock[i - M + 1][j - M + 1] == 0:
                cnt += 1

    # print(board)
    keys = [key, rotate_90(key), rotate_180(key), rotate_270(key)]

    for i in range(B - M + 1):
        for j in range(B - M + 1):
            temp = [board[k][j: j + M] for k in range(i, i + M)]

            if compareroad(temp, keys, cnt):
                return True
            # print(temp)



    return False

print(solution(key, lock))