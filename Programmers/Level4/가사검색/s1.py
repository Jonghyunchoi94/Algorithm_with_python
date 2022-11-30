words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]

def solution(words, queries):
    answer = []

    for query in queries:
        l = len(query)
        q = query.strip("?")
        if q:
            ql = len(q)
            idx = query.index(q[0])

        temp = 0

        for word in words:
            if len(word) != l:
                continue

            if (not q) and len(word) == l:
                temp += 1
            else:
                if word[idx: idx + ql] == q:
                    temp += 1

        answer.append(temp)

    return answer

print(solution(words, queries))