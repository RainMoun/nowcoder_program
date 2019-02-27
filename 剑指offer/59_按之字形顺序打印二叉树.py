# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        result = [[pRoot.val]]
        lst = [pRoot]
        lst_copy = []
        left_to_right = 0
        while lst:
            while lst:
                now_node = lst[0]
                lst = lst[1:]
                if now_node.left:
                    lst_copy.append(now_node.left)
                if now_node.right:
                    lst_copy.append(now_node.right)
            if not lst_copy:
                break
            if left_to_right == 0:  # 从右向左打印
                left_to_right = 1
                temp_lst = [i.val for i in lst_copy[::-1]]
                result.append(temp_lst)
            else:
                left_to_right = 0
                temp_lst = [i.val for i in lst_copy]
                result.append(temp_lst)
            lst = lst_copy[:]
            lst_copy = []
        return result

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
p3.right = p7
s = Solution()
print(s.Print(p1))