user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]

def solution(user_id, banned_id):
    res = []
    case = [[]]
    for ban in banned_id:
        tmp = []
        for user in user_id:
            if len(ban) != len(user):
                continue
            else:
                Flag = True
            for w in range(len(user)):
                if ban[w] == "*" or ban[w] == user[w]:
                    continue
                else:
                    Flag = False
                    break

            if Flag:
                for c in case:
                    if user not in c:
                        tmp.append(c + [user])

        case = tmp

    for s in case:
        if set(s) not in res:
            res.append(set(s))

    return len(res)

print(solution(user_id, banned_id))