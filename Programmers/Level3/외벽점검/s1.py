n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]


from copy import deepcopy

def solution(n, weak, dist):
    dist.sort(reverse=True)
    w = deepcopy(weak)
    # l = len(weak)
    interval = 987654321
    people = 0
    for k in range(len(weak)):
        w.append(n + weak[k])
        if w[-1] - w[k + 1] < interval:
            interval = w[-1] - w[k + 1]
            # idx = k
    print(w)
    print(interval)
    for d in range(len(dist)):
        if interval <= 0:
            break

        interval -= dist[d]
        people += 1

    return people

print(solution(n, weak, dist))

