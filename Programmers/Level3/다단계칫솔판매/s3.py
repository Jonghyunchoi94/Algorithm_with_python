enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    amount = [100 * i for i in amount]

    ref_store = {}

    for i in range(len(enroll)):
        if referral[i] == '-':
            ref_store[i] = -1
        else:
            ref_store[i] = enroll.index(referral[i])
    print(ref_store)

    def find(name, money):
        if name == -1:
            return

        if (money // 10) == 0:
            answer[name] += money
            return

        nmoney = (money // 10)

        answer[name] += (money - nmoney)

        find(ref_store[name], nmoney)

        return

    for s in range(len(seller)):
        find(enroll.index(seller[s]), amount[s])

    return answer

print(solution(enroll, referral, seller, amount))