enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

def find(parents, money, number, answer):
    if parents[number] == number or money // 10 == 0:
        answer[number] += money
        return
    send = money // 10
    mine = money - send
    answer[number] += mine
    find(parents, send, parents[number], answer)
    return


def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = [0] * (n + 1)
    d = {}
    parents = [i for i in range(n + 1)]

    for i in range(n):
        d[enroll[i]] = i + 1

    for i in range(n):
        if referral[i] == "-":  # 민호가 추천인
            parents[i + 1] = 0
        else:
            parents[i + 1] = d[referral[i]]
    print(d)
    for i in range(len(seller)):
        print(answer)
        find(parents, amount[i] * 100, d[seller[i]], answer)
    return answer[1:]

print(solution(enroll, referral, seller, amount))