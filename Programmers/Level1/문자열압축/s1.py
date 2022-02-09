s = "aabbaccc"
"""
1. 디버깅으로 오류 케이스 찾을 것!!
- "aaaaaaaaaaaabcd"
2. 처음과 마지막이 고려되었는지 확인!!
"""

def solution(s):
    interval = 1
    tmp_val = -1
    res = 987654321
    tmp_cnt = 0
    Flag = False
    Flag_num = 1
    while interval <= len(s):
        for i in range(0, len(s), interval):
            tmp = s[i: i + interval]
            if tmp != tmp_val and not Flag:
                tmp_cnt += len(tmp)
            elif tmp != tmp_val and Flag:
                tmp_cnt += (len(tmp) + len(str(Flag_num)))
                Flag_num = 1
                Flag = False
            elif tmp == tmp_val and not Flag:
                Flag_num += 1
                Flag = True
            else:
                Flag_num += 1
            tmp_val = tmp
        if Flag_num != 1:
            tmp_cnt += len(str(Flag_num))
        res = min(res, tmp_cnt)
        interval += 1
        Flag = False
        Flag_num = 1
        tmp_val = -1
        tmp_cnt = 0
    return res


print(solution(s))