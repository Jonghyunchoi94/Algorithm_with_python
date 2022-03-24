d = [1,3,2,5,4]
budget = 9

"""
시간초과
완전탐색을 생각하기 전에 더 효율적인 방법이 있는지 
한 번 정도 생각하고 들어가는 것이 중요하다! (무조건적인 완전탐색은 좋지 않다!)


"""

def dfs(money, departure, idx, money_list):
    global answer
    if idx == len(money_list) or money < 0:
        if money == 0:
            answer = max(answer, departure)
        else:
            answer = max(answer, departure - 1)
        return

    dfs(money, departure, idx + 1, money_list)
    dfs(money - money_list[idx], departure + 1, idx + 1, money_list)



def solution(d, budget):
    global answer
    answer = 0
    dfs(budget, 0, 0, d)
    return answer


print(solution(d, budget))