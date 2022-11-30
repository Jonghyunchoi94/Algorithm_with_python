words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]


from collections import defaultdict

def solution(words, queries):
    answer = [0] * len(queries)

    store_first = defaultdict(set)
    store_last = defaultdict(set)

    for query in queries:
        q = query.strip("?")
        qr = q[::-1]
        temp = ""
        if not q:
            continue

        idx = query.index(q[0])
        if idx == 0:
            for i in range(len(q)):
                store_first[temp].add(q[:i + 1])
                temp += q[i]
        else:
            for i in range(len(qr)):
                store_last[temp].add(qr[:i + 1])
                temp += qr[i]
    print(store_first)
    print(store_last)

    for query in queries:
        ql = len(query)
        for word in words:
            wl = len(word)
            if ql != wl:
                continue





    return answer
print(solution(words, queries))