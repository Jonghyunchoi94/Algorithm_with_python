nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
"""
result : [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
문제가 많이 어렵습니다.
일단, 트리에 대해 굉장히 깊게 아는 것이 중요하고 파이썬에 대해 전반적으로 이해가 깊어야 할 듯 합니다.

"""



import sys
sys.setrecursionlimit(10**4)

from collections import defaultdict

class Node:
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y
        self.left = None
        self.right = None

def addNode(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            addNode(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            addNode(parent.right, child)

def preorder(result, node):
    if node is None:
        return
    result.append(node.val)
    preorder(result, node.left)
    preorder(result, node.right)

def postorder(result, node):
    if node is None:
        return
    postorder(result, node.left)
    postorder(result, node.right)
    result.append(node.val)

def solution(nodeinfo):
    answer = [[], []]
    storage = defaultdict(list)
    for i in range(len(nodeinfo)):
        storage[i + 1] = nodeinfo[i]

    sorted_storage = sorted(storage.items(), \
                            key=lambda x: (x[1][1], -x[1][0]), reverse=True)

    tree = []

    for i in sorted_storage:
        tree.append(Node(i[0], i[1][0], i[1][1]))

    root = tree[0]

    for i in range(1, len(tree)):
        addNode(root, tree[i])

    preorder(answer[0], root)
    postorder(answer[1], root)

    return answer


print(solution(nodeinfo))