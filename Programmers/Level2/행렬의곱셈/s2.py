# 완전히 shortcut한 pythonic한 풀이

def productMatrix(X, Y):
    answer = [[sum(a*b for a, b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return answer
