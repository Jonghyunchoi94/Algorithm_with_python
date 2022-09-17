stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

def solution(stones, k):
    start = 1
    end = max(stones)

    people = 1

    while start <= end:
        blank = 0
        Flag = False
        mid = (start + end) // 2

        for stone in stones:
            if stone < mid:
                blank += 1
                if blank == k:
                    Flag = True
                    break
            else:
                blank = 0

        if Flag:
            end = mid - 1
        else:
            people = max(people, mid)
            start = mid + 1


    return people


print(solution(stones, k))