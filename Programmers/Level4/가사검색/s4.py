words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]

import sys
sys.setrecursionlimit(10000)

def create_trie(trie, words):
    for word in words:
        temp = trie
        l = len(word)
        for w in word:
            if w in temp:
                temp = temp[w]
                temp['length'].append(l)
            else:
                temp[w] = {}
                temp = temp[w]
                temp['length'] = [l]
    return trie

def search_trie(trie, query, length):
    count = 0
    if query[0] == "?":
        return trie['length'].count(length)
    elif query[0] in trie:
        count += search_trie(trie[query[0]], query[1:], length)

    return count


def solution(words, queries):
    answer = []

    rev_words, len_word = [w[::-1] for w in words], [len(w) for w in words]

    trie = create_trie({}, words)
    reverse_trie = create_trie({}, rev_words)

    for query in queries:
        if query[0] == "?" and query[-1] == "?":
            answer.append(len_word.count(len(query)))
        elif query[0] == "?":
            answer.append(search_trie(reverse_trie, query[::-1], len(query)))
        elif query[-1] == "?":
            answer.append(search_trie(trie, query, len(query)))

    return answer

print(solution(words, queries))