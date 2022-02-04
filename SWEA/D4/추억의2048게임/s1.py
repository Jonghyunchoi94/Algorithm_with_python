import sys
sys.stdin = open('input.txt')

class Solve(object):
    def __init__(self, size, position, data, check):
        self.size = size
        self.position = position
        self.data = data
        self.check = check
    def move(self, i, j, flag):
        if self.position == "up":
            while i > 0:
                if self.data[i - 1][j] == 0:
                    self.data[i - 1][j] = self.data[i][j]
                    self.data[i][j] = 0
                elif self.data[i - 1][j] == self.data[i][j] and \
                        self.check[i - 1][j] == False and flag == False:
                    self.data[i - 1][j] *= 2
                    self.data[i][j] = 0
                    self.check[i - 1][j] = True
                    flag = True
                else:
                    break

                i -= 1
        elif self.position == "down":
            while i <= self.size - 2:
                if self.data[i + 1][j] == 0:
                    self.data[i + 1][j] = self.data[i][j]
                    self.data[i][j] = 0
                elif self.data[i + 1][j] == self.data[i][j] and \
                        self.check[i + 1][j] == False and flag == False:
                    self.data[i + 1][j] *= 2
                    self.data[i][j] = 0
                    self.check[i + 1][j] = True
                    flag = True
                else:
                    break

                i += 1

        elif self.position == "left":
            while j > 0:
                if self.data[i][j - 1] == 0:
                    self.data[i][j - 1] = self.data[i][j]
                    self.data[i][j] = 0
                elif self.data[i][j - 1] == self.data[i][j] and \
                        self.check[i][j - 1] == False and flag == False:
                    self.data[i][j - 1] *= 2
                    self.data[i][j] = 0
                    self.check[i][j - 1] = True
                    flag = True
                else:
                    break

                j -= 1
        elif self.position == "right":
            while j <= self.size - 2:
                if self.data[i][j + 1] == 0:
                    self.data[i][j + 1] = self.data[i][j]
                    self.data[i][j] = 0
                elif self.data[i][j + 1] == self.data[i][j] and \
                        self.check[i][j + 1] == False and flag == False:
                    self.data[i][j + 1] *= 2
                    self.data[i][j] = 0
                    self.check[i][j + 1] = True
                    flag = True
                else:
                    break
                j += 1
        return self.data


T = int(input())

for case in range(T):
    N, S = input().split()
    N = int(N)
    original_data = [list(map(int, input().split())) for _ in range(N)]
    state = [[False] * N for _ in range(N)]

    problem = Solve(N, S, original_data, state)
    if S == "up" or S == "left":
        for i in range(N):
            for j in range(N):
                ans = problem.move(i, j, False)

    elif S == "down" or S == "right":
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                ans = problem.move(i, j, False)

    print("#{}".format(case + 1))
    for i in ans:
        print(" ".join(map(str, i)))







