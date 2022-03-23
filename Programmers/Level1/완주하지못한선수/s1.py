import collections

# Counter 라이브러리에 대해서 알아보자!

participant = ["a", "a", "b", "c", "c", "d", "e"]
completion = ["a", "b", "c", "d"]
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(collections.Counter(participant))
    print(collections.Counter(completion))
    print(answer)
    print(answer.keys())
    print(list(answer.keys()))
    return list(answer.keys())[0]


print(solution(participant, completion))