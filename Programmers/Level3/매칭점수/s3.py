import re


def solution(word, pages):
    webpage = []
    webpageName = []
    webpageGraph = dict()  # 나를 가르키는 외부 링크

    for page in pages:
        url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
        basic_score = 0
        for f in re.findall(r'[a-zA-Z]+', page.lower()):
            if f == word.lower():
                basic_score += 1
        ex_Link = re.findall('<a href="(https://[\S]*)"', page)

        for link in ex_Link:
            if link not in webpageGraph.keys():
                webpageGraph[link] = [url]
            else:
                webpageGraph[link].append(url)

        webpageName.append(url)
        webpage.append([url, basic_score, len(ex_Link)])

    max_Val = 0
    result = 0

    for i in range(len(webpage)):
        url = webpage[i][0]
        score = webpage[i][1]

        if url in webpageGraph.keys():
            for link in webpageGraph[url]:
                a, b, c = webpage[webpageName.index(link)]
                score += (b / c)
        if max_Val < score:
            max_Val = score
            result = i

    return result