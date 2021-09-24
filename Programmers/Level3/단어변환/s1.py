begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]


def difference(before_word, after_word):
    ans = 0
    for i in before_word:
        if i not in after_word:
            ans += 1
    if ans == 1:
        return True

    return False



def solution(begin, target, words):
    answer = 0
    visited = [0] * len(words)
    min_val = 987654321
    if target not in words:
        return answer

    def dfs(word, n):
        nonlocal min_val
        if word == target:
            if n < min_val:
                min_val = n
            return
        else:
            for i in range(len(words)):
                if visited[i] == 0 and difference(word, words[i]):
                    visited[i] = 1
                    dfs(words[i], n + 1)
                    visited[i] = 0
        return
    dfs(begin, 0)
    if min_val == 987654321:
        return answer
    else:
        return min_val

print(solution(begin, target, words))


