"""
검색어 word와 웹페이지의 HTML 목록인 pages가 주어졌을 때,
매칭점수가 가장 높은 웹페이지의 index를 구하라.
만약 그런 웹페이지가 여러 개라면 그중 번호가 가장 작은 것을 구하라.

주의사항 :
1. 단어 단위 일치 (aba != ab)

"""
word = "blind"
pages = [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"
]

import re

def solution(word, pages):
    answer = 0
    site_indexing = [0] * len(pages)
    link_cnt = [0] * len(pages)
    base_score = [0] * len(pages)
    link_score = [0] * len(pages)
    total_score = [0] * len(pages)

    for i in range(len(pages)):
        master = re.findall("(content=)(\")(.+)(\")", pages[i])
        site_indexing[i] = master[0][-2]
        word_search = re.findall("(%s+[^a-zA-Z])" % word, pages[i], re.IGNORECASE)
        # r"\b%s\b" %
        print(word_search)
        base_score[i] = len(word_search)
    # print(site_indexing)
    # print(base_score)
    for i in range(len(pages)):
        link = re.findall("(href=)(\")(.+)(\")", pages[i])
        total_cnt = len(link)
        for j in link:
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