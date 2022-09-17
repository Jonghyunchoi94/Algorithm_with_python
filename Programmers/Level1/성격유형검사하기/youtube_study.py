from collections import defaultdict

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

def solution(survey, choices):
    score = defaultdict(int)

    for sv, choice in zip(survey, choices):
        if choice > 4:
            score[sv[1]] += choice - 4
        elif choice < 4:
            score[sv[0]] += 4 - choice

    indice_1 = "R" if score["R"] >= score["T"] else "T"
    indice_2 = "C" if score["C"] >= score["F"] else "F"
    indice_3 = "J" if score["J"] >= score["M"] else "M"
    indice_4 = "A" if score["A"] >= score["N"] else "N"

    answer = indice_1 + indice_2 + indice_3 + indice_4
    return answer

print(solution(survey, choices))