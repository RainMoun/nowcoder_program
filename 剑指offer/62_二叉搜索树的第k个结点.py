# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if k <= 0:
            return None
        lst = []

        def mid_order(pRoot):
            if not pRoot:
                return
            mid_order(pRoot.left)
            lst.append(pRoot.val)
            mid_order(pRoot.right)
        mid_order(pRoot)
        if k <= len(lst):
            return lst[k - 1]
        else:
            return None


if __name__ == '__main__':
    p1 = TreeNode(8)
    p2 = TreeNode(6)
    p3 = TreeNode(10)
    p4 = TreeNode(5)
    p5 = TreeNode(7)
    p6 = TreeNode(9)
    p7 = TreeNode(11)
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p2.right = p5
    p3.left = p6
    p3.left = p7
    s = Solution()
    print(s.KthNode(p1, 8))