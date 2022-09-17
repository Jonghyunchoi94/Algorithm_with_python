stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

def solution(stones, k):
    people = 1
    Flag = False
    while True:
        blank = 0

        for stone in stones:
            if stone <= people:
                blank += 1
                if blank == k:
                    Flag = True
                    break
            else:
                blank = 0
        if Flag:
            break

        people += 1
    return people


print(solution(stones, k))