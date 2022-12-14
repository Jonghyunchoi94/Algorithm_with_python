import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

res = [0] * 10

def sub(num):
    ans = []
    new_num = int(str(num)[:-1] + "9")
    diff = new_num - num
    if str(num)[-1] == "9":
        return diff, ans
    for i in range(10 - diff, 10):
        ans.append(i)
    return diff, ans

weight = 1
while N > 0:
    diff, subtract = sub(N)

    for i1 in range(10):
        res[i1] += (N // 10 + 1) * weight
    for i2 in subtract:
        res[i2] -= weight
    for i3 in list(str(N)[:-1]):
        res[int(i3)] -= diff * weight

    res[0] -= weight
    N //= 10
    weight *= 10

print(" ".join(map(str, res)))


'''
의문점 : str(N//10)과 str(N)[:-1] 의 차이가 뭘까?

답은 일의자리 수일 때에 있다.

str(N//10) => '0'

str(N)[:-1] => ''

직접 계산해보거나 경험이 있으면 알기 쉽지만 생각만으로는 헷갈리기 쉬운 연산이다.
'''