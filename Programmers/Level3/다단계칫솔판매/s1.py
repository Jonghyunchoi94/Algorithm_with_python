enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    amount = [100 * i for i in amount]

    name_store = {}

    for i in range(len(enroll)):
        name_store[enroll[i]] = i



    def find(name, money):
        if name not in name_store:
            return

        if (money // 10) == 0:
            answer[name_store[name]] += money
            return

        nmoney = (money // 10)

        answer[name_store[name]] += (money - nmoney)

        find(referral[name_store[name]], nmoney)

        return

    for s in range(len(seller)):
        find(seller[s], amount[s])

    return answer

print(solution(enroll, referral, seller, amount))