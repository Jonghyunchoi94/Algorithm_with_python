survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

def solution(survey, choices):
    answer = [False] * 4
    position = {
        0 : ["R", "T"],
        1 : ["C", "F"],
        2 : ["M", "J"],
        3 : ["A", "N"]
    }

    score = [3, 2, 1, 0, 1, 2, 3]

    mbti = {}

    for m in range(len(survey)):
        if choices[m] < 4:
            if survey[m][0] not in mbti:
                mbti[survey[m][0]] = score[choices[m] - 1]
            else:
                mbti[survey[m][0]] += score[choices[m] - 1]
        else:
            if survey[m][1] not in mbti:
                mbti[survey[m][1]] = score[choices[m] - 1]
            else:
                mbti[survey[m][1]] += score[choices[m] - 1]
    print(position)
    print(mbti)

    for i in position:
        if not mbti.get(position[i][0]):
            mbti[position[i][0]] = 0
        if not mbti.get(position[i][1]):
            mbti[position[i][1]] = 0

        if mbti.get(position[i][0]) > mbti.get(position[i][1]):
            answer[i] = position[i][0]
        elif mbti.get(position[i][1]) > mbti.get(position[i][0]):
            answer[i] = position[i][1]
        else:
            answer[i] = sorted(position[i])[0]

    return "".join(answer)

print(solution(survey, choices))