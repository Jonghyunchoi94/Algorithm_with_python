sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]



def solution(sales, links):
    answer = 0

    tree = [[] for _ in range(len(sales) + 1)]

    for i, j in links:
        tree[i].append(j)

    print(tree)

    def dfs(n):
        if not tree[n]:
            return sales[n]

        for i in tree[n]:

        return

    return answer

print(solution(sales, links))