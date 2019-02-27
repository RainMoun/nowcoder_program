# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        lst = [pRoot]
        temp_lst = []
        while lst:
            while lst:
                node = lst[-1]
                lst = lst[: -1]
                if node:
                    temp_lst.append(node.left)
                    temp_lst.append(node.right)
                else:
                    temp_lst.append(None)
                    temp_lst.append(None)
            all_None = 1
            for i in range(len(temp_lst)//2):
                if not temp_lst[i] and not temp_lst[len(temp_lst) - 1 - i]:
                    continue
                if (temp_lst[i] and not temp_lst[len(temp_lst) - 1 - i]) or (not temp_lst[i] and temp_lst[len(temp_lst) - 1 - i]):
                    return False
                if temp_lst[i].val != temp_lst[len(temp_lst) - 1 - i].val:
                    return False
                if temp_lst[i] or temp_lst[len(temp_lst) - 1 - i]:
                    all_None = 0
            if all_None == 1:
                return True
            else:
                lst = temp_lst[:]
                temp_lst = []


p1 = TreeNode(8)
p2 = TreeNode(6)
p3 = TreeNode(6)
p4 = TreeNode(5)
p5 = TreeNode(7)
p6 = TreeNode(7)
p7 = TreeNode(5)
p1.left = p2
p1.right = p3
p2.left = p4
p2.right = p5
p3.left = p6
p3.right = p7
s = Solution()
print(s.isSymmetrical(p1))