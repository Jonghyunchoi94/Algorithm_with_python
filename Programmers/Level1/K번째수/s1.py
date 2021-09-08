array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for idx in commands:
        data = array[idx[0]-1:idx[1]]
        data.sort()
        val = data[idx[2]-1]
        answer.append(val)
    return answer

print(solution(array, commands))