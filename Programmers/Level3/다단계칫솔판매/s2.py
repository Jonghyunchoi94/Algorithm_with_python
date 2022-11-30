def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    amount = [100 * i for i in amount]

    def find(name, money):
        if name == "-":
            return

        if (money // 10) == 0:
            answer[enroll.index(name)] += money
            return

        nmoney = (money // 10)

        answer[enroll.index(name)] += (money - nmoney)

        find(referral[enroll.index(name)], nmoney)

        return

    for s in range(len(seller)):
        find(seller[s], amount[s])

    return answer