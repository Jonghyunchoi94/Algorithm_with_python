queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]


def solution(queue1, queue2):

    sum1, sum2 = sum(queue1), sum(queue2)
    if (sum1 + sum2) % 2:
        return -1
    n = len(queue1)
    l1, r1 = 0, n - 1
    l2, r2 = n, 2 * n - 1

    def get_num(idx):
        idx %= 2 * n
        return queue1[idx] if idx < n else queue2[idx - n]

    answer = 0

    while sum1 != sum2 and answer <= 3 * n:
        answer += 1
        if sum1 > sum2:
            num = get_num(l1)
            sum1 -= num
            sum2 += num
            l1 += 1
            r2 += 1
        else:
            num = get_num(l2)
            sum1 += num
            sum2 -= num
            l2 += 1
            r1 += 1


    return answer if answer <= 3 * n else -1


