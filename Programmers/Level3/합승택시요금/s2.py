def solution(n, s, a, b, fares):
    Inf=int(1e9)
    money=[[Inf]*(n+1) for _ in range(n+1)]

    for i in range(1,n+1):
        money[i][i]=0

    for i in fares:
        money[i[0]][i[1]]=i[2]
        money[i[1]][i[0]]=i[2]

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(i,n+1):
                temp=min(money[i][j],money[i][k]+money[k][j])
                money[i][j]=money[j][i]=temp

    answer=Inf

    for t in range(1,n+1):
        temp=money[s][t]+money[t][a]+money[t][b]
        answer=min(answer,temp)

    return answer