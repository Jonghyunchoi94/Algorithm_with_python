info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]


def solution(info, edges):
    answer = 0
    visited = [0] * len(info)
    visited[0] = 1

    def dfs(wolf, sheep):
        nonlocal answer
        if wolf >= sheep:
            return
        answer = max(answer, sheep)

        for s, e in edges:
            parent = s
            child = e
            animal = info[child]

            if visited[parent] and not visited[child]:
                visited[child] = 1
                if animal == 0:
                    dfs(wolf, sheep + 1)
                else:
                    dfs(wolf + 1, sheep)
                visited[child] = 0

    dfs(0, 1)
    return answer


print(solution(info, edges))