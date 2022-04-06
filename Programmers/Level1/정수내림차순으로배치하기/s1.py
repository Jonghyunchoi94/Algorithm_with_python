"""
int(n)으로 바꿔야 하는 이유 long type이기 때문

"""
def solution(n):
    n = int(n)
    return int("".join(sorted(list(str(n)), reverse = True)))