class Node():
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

    # returns the string equivalent of the __repr__() function
    # Refer https://bit.ly/strRepr
    def __str__(self):
        return self.preorder([]).__str__()

    # return a list containing values of the pre order traversal
    def preorder(self, alist):
        if not self:
            return alist
        alist.append(self.data)
        if self.left:
            self.left.preorder(alist)
        if self.right:
            self.right.preorder(alist)

        return alist


def boustrophedon_order(root):
    print(root)

    queue = [root]
    boustro = []
    right_to_left = False
    node_count = 0
    power2 = 2

    while queue:
        node = queue.pop(0)
        if node:
            boustro.append(node.data)
            if right_to_left:
                queue.extend([node.right, node.left])
            else:
                queue.extend([node.left, node.right])

        node_count += 2
        if node_count == power2:
            queue.reverse()
            right_to_left = not right_to_left
            node_count = 0
            power2 = power2 * 2

    print(boustro)
    return boustro


def boustrophedon_order_alt(root):
    level = []  # intermediary level values
    result = []  # accumulates values for all levels
    q = [root]
    levelnum = 1

    while q:
        count = len(q)
        while count:
            node = q.pop(0)
            if node:
                level.append(node.data)
                q.extend([node.left, node.right])
            count -= 1

        result = result + (level if levelnum % 2 else level[::-1])
        level.clear()
        levelnum += 1

    return result


def level_order(root):

    queue = [root]
    res = []

    while queue:
        node = queue.pop(0)

        if node:
            res.append(node.data)
            queue.extend([node.left, node.right])

    return res
