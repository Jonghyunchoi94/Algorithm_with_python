sales = [5, 6, 5, 1, 4]
links = [[2,3], [1,4], [2,5], [1,2]]


def solution(sales, links):
    tree = [[] for _ in range(len(sales) + 1)]

    for i, j in links:
        tree[i].append(j)

    # print(tree)
    def dfs(n):

        answer = []
        if not tree[n]:
            return sales[n - 1], 0

        for i in tree[n]:
            yes, no = dfs(i)
            answer.append((yes, no))

        ny, nn = 0, []
        for i, j in answer:
            ny += min(i, j)

        for i, j in answer:
            nn.append(ny - min(i, j) + i)

        return ny + sales[n - 1], min(nn)
    # print(dfs(1))
    a, b = dfs(1)

    return min(a, b)

print(solution(sales, links))