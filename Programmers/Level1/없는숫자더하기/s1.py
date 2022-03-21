def solution(numbers):
    answer = 45
    storage = set()
    for i in numbers:
        if i not in storage:
            storage.add(i)
            answer -= i
    return answer