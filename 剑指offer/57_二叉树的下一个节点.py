# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        # write code here
        # 该结点只有左孩子 该结点只有右孩子 该结点有左孩子也有右孩子 该结点为叶节点
        if not pNode:
            return None
        if pNode.right:  # 如果有右孩子
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        else:  # 没有右孩子
            while pNode.next:
                if pNode.next.left == pNode:
                    return pNode.next
                pNode = pNode.next
            return None



p1 = TreeLinkNode(1)
p2 = TreeLinkNode(2)
p3 = TreeLinkNode(3)
p4 = TreeLinkNode(4)
p5 = TreeLinkNode(5)
p1.left = p2
p1.right = p3
p2.left = p4
p2.next = p1
p4.next = p2
p3.next = p1
p3.right = p5
p5.next = p3
s = Solution()
print(s.GetNext(p5))