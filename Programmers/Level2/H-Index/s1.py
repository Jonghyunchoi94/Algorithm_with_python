citations = [3, 0, 6, 1, 5]

def solution(citations):
    answer = 0
    j = 0
    while True:
        data_list = [i - j for i in citations if i - j >= 0]
        if len(data_list) < j:
            answer = j - 1
            break
        j += 1

    return answer

print(solution(citations))