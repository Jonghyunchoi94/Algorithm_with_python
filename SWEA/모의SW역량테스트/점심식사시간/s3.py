from collections import defaultdict

a = defaultdict(list)

a[0].append(1)
a[1].append(2)
a[0].append(3)


print(type(a[0]))