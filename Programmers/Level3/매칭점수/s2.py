"""
검색어 word와 웹페이지의 HTML 목록인 pages가 주어졌을 때,
매칭점수가 가장 높은 웹페이지의 index를 구하라.
만약 그런 웹페이지가 여러 개라면 그중 번호가 가장 작은 것을 구하라.

주의사항 :
1. 단어 단위 일치 (aba != ab)

"""
word = "Muzi"
pages = [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

import re

def solution(word, pages):
    answer = 0
    site_indexing = [0] * len(pages)
    link_cnt = [0] * len(pages)
    base_score = [0] * len(pages)
    link_score = [0] * len(pages)
    total_score = [0] * len(pages)

    for i in range(len(pages)):
        master = re.findall("(https://)(.+)(\"/>)", pages[i])
        # print(master)
        site_indexing[i] = master[0][-2]

        for f in re.findall(r"[a-zA-Z]+", pages[i].lower()):
            if f == word.lower():
                base_score[i] += 1
    # print(site_indexing)
    # print(base_score)
    for i in range(len(pages)):
        link = re.findall("(<a)(.+)(href=)(.+)(https://)(.+)(\")", pages[i])
        # print(link)
        total_cnt = len(link)
        for j in link:
            if j[-2] in link_cnt:
                link_cnt[site_indexing.index(j[-2])] += 1
                tmp_score = base_score[i] / total_cnt
                link_score[site_indexing.index(j[-2])] += tmp_score
    # print(link_cnt)
    # print(link_score)

    for i in range(len(pages)):
        total_score[i] = base_score[i] + link_score[i]
    # print(total_score)
    compare = -1
    for i, j in enumerate(total_score):
        if j > compare:
            compare = j
            answer = i

    return answer

print(solution(word, pages))